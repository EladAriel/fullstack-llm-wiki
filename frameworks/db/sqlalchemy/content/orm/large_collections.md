---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/large_collections.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# Working with Large Collections

The default behavior of `_orm.relationship` is to fully load the contents of collections into memory, based on a configured `loader strategy <orm_queryguide_relationship_loaders>` that controls when and how these contents are loaded from the database.  Related collections may be loaded into memory not just when they are accessed, or eagerly loaded, but in most cases will require population when the collection itself is mutated, as well as in cases where the owning object is to be deleted by the unit of work system.

When a related collection is potentially very large, it may not be feasible for such a collection to be populated into memory under any circumstances, as the operation may be overly consuming of time, network and memory resources.

This section includes API features intended to allow `_orm.relationship` to be used with large collections while maintaining adequate performance.

## Write Only Relationships

The **write only** loader strategy is the primary means of configuring a `_orm.relationship` that will remain writeable, but will not load its contents into memory.  A write-only ORM configuration in modern type-annotated Declarative form is illustrated below:

```python
 >>> from decimal import Decimal
 >>> from datetime import datetime

 >>> from sqlalchemy import ForeignKey
 >>> from sqlalchemy import func
 >>> from sqlalchemy.orm import DeclarativeBase
 >>> from sqlalchemy.orm import Mapped
 >>> from sqlalchemy.orm import mapped_column
 >>> from sqlalchemy.orm import relationship
 >>> from sqlalchemy.orm import Session
 >>> from sqlalchemy.orm import WriteOnlyMapped

 >>> class Base(DeclarativeBase):
 ...     pass

 >>> class Account(Base):
 ...     __tablename__ = "account"
 ...     id: Mapped[int] = mapped_column(primary_key=True)
 ...     identifier: Mapped[str]
 ...
 ...     account_transactions: WriteOnlyMapped["AccountTransaction"] = relationship(
 ...         cascade="all, delete-orphan",
 ...         passive_deletes=True,
 ...         order_by="AccountTransaction.timestamp",
 ...     )
 ...
 ...     def __repr__(self):
 ...         return f"Account(identifier={self.identifier!r})"

 >>> class AccountTransaction(Base):
 ...     __tablename__ = "account_transaction"
 ...     id: Mapped[int] = mapped_column(primary_key=True)
 ...     account_id: Mapped[int] = mapped_column(
 ...         ForeignKey("account.id", ondelete="cascade")
 ...     )
 ...     description: Mapped[str]
 ...     amount: Mapped[Decimal]
 ...     timestamp: Mapped[datetime] = mapped_column(default=func.now())
 ...
 ...     def __repr__(self):
 ...         return (
 ...             f"AccountTransaction(amount={self.amount:.2f}, "
 ...             f"timestamp={self.timestamp.isoformat()!r})"
 ...         )
 ...
 ...     __mapper_args__ = {"eager_defaults": True}
```

>>> from sqlalchemy import create_engine >>> from sqlalchemy import event >>> engine = create_engine("sqlite://", echo=True) >>> @event.listens_for(engine, "connect") ... def set_sqlite_pragma(dbapi_connection, connection_record): ...     cursor = dbapi_connection.cursor() ...     cursor.execute("PRAGMA foreign_keys=ON") ...     cursor.close()

>>> Base.metadata.create_all(engine) BEGIN...

Above, the `account_transactions` relationship is configured not using the ordinary `.Mapped` annotation, but instead using the `.WriteOnlyMapped` type annotation, which at runtime will assign the `loader strategy <orm_queryguide_relationship_loaders>` of `lazy="write_only" to the target orm.relationship`. The `.WriteOnlyMapped annotation is an alternative form of the orm.Mapped annotation which indicate the use of the orm.WriteOnlyCollection` collection type on instances of the object.

The above `_orm.relationship` configuration also includes several elements that are specific to what action to take when `Account` objects are deleted, as well as when `AccountTransaction` objects are removed from the `account_transactions` collection.  These elements are:

- `passive_deletes=True` - allows the `unit of work` to forego having
to load the collection when `Account` is deleted; see `passive_deletes`.

- `ondelete="cascade"` configured on the `.ForeignKey` constraint.
This is also detailed at `passive_deletes`.

- `cascade="all, delete-orphan"` - instructs the `unit of work` to
delete `AccountTransaction` objects when they are removed from the collection.  See `cascade_delete_orphan` in the `unitofwork_cascades` document.

.. versionadded:: 2.0  Added "Write only" relationship loaders.

### Creating and Persisting New Write Only Collections

The write-only collection allows for direct assignment of the collection as a whole **only** for `transient` or `pending` objects. With our above mapping, this indicates we can create a new `Account` object with a sequence of `AccountTransaction objects to be added to a orm.Session`.   Any Python iterable may be used as the source of objects to start, where below we use a Python `list`:

```
>>> new_account = Account(
...     identifier="account_01",
...     account_transactions=[
...         AccountTransaction(description="initial deposit", amount=Decimal("500.00")),
...         AccountTransaction(description="transfer", amount=Decimal("1000.00")),
...         AccountTransaction(description="withdrawal", amount=Decimal("-29.50")),
...     ],
... )

>>> with Session(engine) as session:
...     session.add(new_account)
...     session.commit()
{execsql}BEGIN (implicit)
INSERT INTO account (identifier) VALUES (?)
[...] ('account_01',)
INSERT INTO account_transaction (account_id, description, amount, timestamp)
VALUES (?, ?, ?, CURRENT_TIMESTAMP) RETURNING id, timestamp
[... (insertmanyvalues) 1/3 (ordered; batch not supported)] (1, 'initial deposit', 500.0)
INSERT INTO account_transaction (account_id, description, amount, timestamp)
VALUES (?, ?, ?, CURRENT_TIMESTAMP) RETURNING id, timestamp
[insertmanyvalues 2/3 (ordered; batch not supported)] (1, 'transfer', 1000.0)
INSERT INTO account_transaction (account_id, description, amount, timestamp)
VALUES (?, ?, ?, CURRENT_TIMESTAMP) RETURNING id, timestamp
[insertmanyvalues 3/3 (ordered; batch not supported)] (1, 'withdrawal', -29.5)
COMMIT
```

Once an object is database-persisted (i.e. in the `persistent` or `detached` state), the collection has the ability to be extended with new items as well as the ability for individual items to be removed. However, the collection may **no longer be re-assigned with a full replacement collection**, as such an operation requires that the previous collection is fully loaded into memory in order to reconcile the old entries with the new ones:

```
>>> new_account.account_transactions = [
...     AccountTransaction(description="some transaction", amount=Decimal("10.00"))
... ]
Traceback (most recent call last):
...
sqlalchemy.exc.InvalidRequestError: Collection "Account.account_transactions" does not
support implicit iteration; collection replacement operations can't be used
```

### Adding New Items to an Existing Collection

For write-only collections of persistent objects, modifications to the collection using `unit of work` processes may proceed only by using the `.WriteOnlyCollection.add`, `.WriteOnlyCollection.add_all` and `.WriteOnlyCollection.remove` methods:

```
>>> from sqlalchemy import select
>>> session = Session(engine, expire_on_commit=False)
>>> existing_account = session.scalar(select(Account).filter_by(identifier="account_01"))
{execsql}BEGIN (implicit)
SELECT account.id, account.identifier
FROM account
WHERE account.identifier = ?
[...] ('account_01',)
{stop}
>>> existing_account.account_transactions.add_all(
...     [
...         AccountTransaction(description="paycheck", amount=Decimal("2000.00")),
...         AccountTransaction(description="rent", amount=Decimal("-800.00")),
...     ]
... )
>>> session.commit()
{execsql}INSERT INTO account_transaction (account_id, description, amount, timestamp)
VALUES (?, ?, ?, CURRENT_TIMESTAMP) RETURNING id, timestamp
[... (insertmanyvalues) 1/2 (ordered; batch not supported)] (1, 'paycheck', 2000.0)
INSERT INTO account_transaction (account_id, description, amount, timestamp)
VALUES (?, ?, ?, CURRENT_TIMESTAMP) RETURNING id, timestamp
[insertmanyvalues 2/2 (ordered; batch not supported)] (1, 'rent', -800.0)
COMMIT
```

The items added above are held in a pending queue within the `_orm.Session` until the next flush, at which point they are INSERTed into the database, assuming the added objects were previously `transient`.

### Querying Items

The `_orm.WriteOnlyCollection` does not at any point store a reference to the current contents of the collection, nor does it have any behavior where it would directly emit a SELECT to the database in order to load them; the overriding assumption is that the collection may contain many thousands or millions of rows, and should never be fully loaded into memory as a side effect of any other operation.

Instead, the `_orm.WriteOnlyCollection includes SQL-generating helpers such as orm.WriteOnlyCollection.select`, which will generate a `.Select` construct pre-configured with the correct WHERE / FROM criteria for the current parent row, which can then be further modified in order to SELECT any range of rows desired, as well as invoked using features like `server side cursors <orm_queryguide_yield_per>` for processes that wish to iterate through the full collection in a memory-efficient manner.

The statement generated is illustrated below. Note it also includes ORDER BY criteria, indicated in the example mapping by the `_orm.relationship.order_by parameter of orm.relationship`; this criteria would be omitted if the parameter were not configured:

```
>>> print(existing_account.account_transactions.select())
{printsql}SELECT account_transaction.id, account_transaction.account_id, account_transaction.description,
account_transaction.amount, account_transaction.timestamp
FROM account_transaction
WHERE :param_1 = account_transaction.account_id ORDER BY account_transaction.timestamp
```

We may use this `.Select construct along with the orm.Session` in order to query for `AccountTransaction objects, most easily using the orm.Session.scalars` method that will return a `.Result` that yields ORM objects directly. It's typical, though not required, that the `.Select` would be modified further to limit the records returned; in the example below, additional WHERE criteria to load only "debit" account transactions is added, along with "LIMIT 10" to retrieve only the first ten rows:

```
>>> account_transactions = session.scalars(
...     existing_account.account_transactions.select()
...     .where(AccountTransaction.amount < 0)
...     .limit(10)
... ).all()
{execsql}BEGIN (implicit)
SELECT account_transaction.id, account_transaction.account_id, account_transaction.description,
account_transaction.amount, account_transaction.timestamp
FROM account_transaction
WHERE ? = account_transaction.account_id AND account_transaction.amount < ?
ORDER BY account_transaction.timestamp  LIMIT ? OFFSET ?
[...] (1, 0, 10, 0)
{stop}>>> print(account_transactions)
[AccountTransaction(amount=-29.50, timestamp='...'), AccountTransaction(amount=-800.00, timestamp='...')]
```

### Removing Items

Individual items that are loaded in the `persistent state against the current orm.Session` may be marked for removal from the collection using the `.WriteOnlyCollection.remove` method. The flush process will implicitly consider the object to be already part of the collection when the operation proceeds.   The example below illustrates removal of an individual `AccountTransaction` item, which per `cascade <unitofwork_cascades>` settings results in a DELETE of that row:

```
>>> existing_transaction = account_transactions[0]
>>> existing_account.account_transactions.remove(existing_transaction)
>>> session.commit()
{execsql}DELETE FROM account_transaction WHERE account_transaction.id = ?
[...] (3,)
COMMIT
```

As with any ORM-mapped collection, object removal may proceed either to de-associate the object from the collection while leaving the object present in the database, or may issue a DELETE for its row, based on the `cascade_delete_orphan configuration of the orm.relationship`.

Collection removal without deletion involves setting foreign key columns to NULL for a `one-to-many <relationship_patterns_o2m>` relationship, or deleting the corresponding association row for a `many-to-many <relationships_many_to_many>` relationship.

### Bulk INSERT of New Items

The `.WriteOnlyCollection can generate DML constructs such as dml.Insert` objects, which may be used in an ORM context to produce bulk insert behavior.  See the section `orm_queryguide_bulk_insert` for an overview of ORM bulk inserts.

#### One to Many Collections

For a **regular one to many collection only**, the `.WriteOnlyCollection.insert method will produce an dml.Insert` construct which is pre-established with VALUES criteria corresponding to the parent object.  As this VALUES criteria is entirely against the related table, the statement can be used to INSERT new rows that will at the same time become new records in the related collection:

```
>>> session.execute(
...     existing_account.account_transactions.insert(),
...     [
...         {"description": "transaction 1", "amount": Decimal("47.50")},
...         {"description": "transaction 2", "amount": Decimal("-501.25")},
...         {"description": "transaction 3", "amount": Decimal("1800.00")},
...         {"description": "transaction 4", "amount": Decimal("-300.00")},
...     ],
... )
{execsql}BEGIN (implicit)
INSERT INTO account_transaction (account_id, description, amount, timestamp) VALUES (?, ?, ?, CURRENT_TIMESTAMP)
[...] [(1, 'transaction 1', 47.5), (1, 'transaction 2', -501.25), (1, 'transaction 3', 1800.0), (1, 'transaction 4', -300.0)]
<...>
{stop}
>>> session.commit()
COMMIT
```

> **Seealso:**  `orm_queryguide_bulk_insert` - in the `queryguide_toplevel`
 `relationship_patterns_o2m` - at `relationship_patterns`

#### Many to Many Collections

For a **many to many collection**, the relationship between two classes involves a third table that is configured using the `_orm.relationship.secondary parameter of orm.relationship`. To bulk insert rows into a collection of this type using `.WriteOnlyCollection`, the new records may be bulk-inserted separately first, retrieved using RETURNING, and those records then passed to the `.WriteOnlyCollection.add_all` method where the unit of work process will proceed to persist them as part of the collection.

Supposing a class `BankAudit` referred to many `AccountTransaction` records using a many-to-many table:

```
>>> from sqlalchemy import Table, Column
>>> audit_to_transaction = Table(
...     "audit_transaction",
...     Base.metadata,
...     Column("audit_id", ForeignKey("audit.id", ondelete="CASCADE"), primary_key=True),
...     Column(
...         "transaction_id",
...         ForeignKey("account_transaction.id", ondelete="CASCADE"),
...         primary_key=True,
...     ),
... )
>>> class BankAudit(Base):
...     __tablename__ = "audit"
...     id: Mapped[int] = mapped_column(primary_key=True)
...     account_transactions: WriteOnlyMapped["AccountTransaction"] = relationship(
...         secondary=audit_to_transaction, passive_deletes=True
...     )
```

>>> Base.metadata.create_all(engine) BEGIN...

To illustrate the two operations, we add more `AccountTransaction` objects using bulk insert, which we retrieve using RETURNING by adding `returning(AccountTransaction)` to the bulk INSERT statement (note that we could just as easily use existing `AccountTransaction` objects as well):

```
>>> new_transactions = session.scalars(
...     existing_account.account_transactions.insert().returning(AccountTransaction),
...     [
...         {"description": "odd trans 1", "amount": Decimal("50000.00")},
...         {"description": "odd trans 2", "amount": Decimal("25000.00")},
...         {"description": "odd trans 3", "amount": Decimal("45.00")},
...     ],
... ).all()
{execsql}BEGIN (implicit)
INSERT INTO account_transaction (account_id, description, amount, timestamp) VALUES
(?, ?, ?, CURRENT_TIMESTAMP), (?, ?, ?, CURRENT_TIMESTAMP), (?, ?, ?, CURRENT_TIMESTAMP)
RETURNING id, account_id, description, amount, timestamp
[...] (1, 'odd trans 1', 50000.0, 1, 'odd trans 2', 25000.0, 1, 'odd trans 3', 45.0)
{stop}
```

With a list of `AccountTransaction objects ready, the orm.WriteOnlyCollection.add_all` method is used to associate many rows at once with a new `BankAudit` object:

```
>>> bank_audit = BankAudit()
>>> session.add(bank_audit)
>>> bank_audit.account_transactions.add_all(new_transactions)
>>> session.commit()
{execsql}INSERT INTO audit DEFAULT VALUES
[...] ()
INSERT INTO audit_transaction (audit_id, transaction_id) VALUES (?, ?)
[...] [(1, 10), (1, 11), (1, 12)]
COMMIT
```

> **Seealso:**  `orm_queryguide_bulk_insert` - in the `queryguide_toplevel`
 `relationships_many_to_many` - at `relationship_patterns`

### Bulk UPDATE and DELETE of Items

In a similar way in which `.WriteOnlyCollection` can generate `.Select` constructs with WHERE criteria pre-established, it can also generate `.Update` and `.Delete` constructs with that same WHERE criteria, to allow criteria-oriented UPDATE and DELETE statements against the elements in a large collection.

#### One To Many Collections

As is the case with INSERT, this feature is most straightforward with **one to many collections**.

In the example below, the `.WriteOnlyCollection.update` method is used to generate an UPDATE statement is emitted against the elements in the collection, locating rows where the "amount" is equal to `-800` and adding the amount of `200` to them:

```
>>> session.execute(
...     existing_account.account_transactions.update()
...     .values(amount=AccountTransaction.amount + 200)
...     .where(AccountTransaction.amount == -800),
... )
{execsql}BEGIN (implicit)
UPDATE account_transaction SET amount=(account_transaction.amount + ?)
WHERE ? = account_transaction.account_id AND account_transaction.amount = ?
[...] (200, 1, -800)
{stop}<...>
```

In a similar way, `.WriteOnlyCollection.delete` will produce a DELETE statement that is invoked in the same way:

```
>>> session.execute(
...     existing_account.account_transactions.delete().where(
...         AccountTransaction.amount.between(0, 30)
...     ),
... )
{execsql}DELETE FROM account_transaction WHERE ? = account_transaction.account_id
AND account_transaction.amount BETWEEN ? AND ? RETURNING id
[...] (1, 0, 30)
<...>
{stop}
```

#### Many to Many Collections

> **Tip:**  The techniques here involve multi-table UPDATE expressions, which are
 slightly more advanced.

For bulk UPDATE and DELETE of **many to many collections**, in order for an UPDATE or DELETE statement to relate to the primary key of the parent object, the association table must be explicitly part of the UPDATE/DELETE statement, which requires either that the backend includes supports for non-standard SQL syntaxes, or extra explicit steps when constructing the UPDATE or DELETE statement.

For backends that support multi-table versions of UPDATE, the `.WriteOnlyCollection.update` method should work without extra steps for a many-to-many collection, as in the example below where an UPDATE is emitted against `AccountTransaction` objects in terms of the many-to-many `BankAudit.account_transactions` collection:

```
>>> session.execute(
...     bank_audit.account_transactions.update().values(
...         description=AccountTransaction.description + " (audited)"
...     )
... )
{execsql}UPDATE account_transaction SET description=(account_transaction.description || ?)
FROM audit_transaction WHERE ? = audit_transaction.audit_id
AND account_transaction.id = audit_transaction.transaction_id RETURNING id
[...] (' (audited)', 1)
{stop}<...>
```

The above statement automatically makes use of "UPDATE..FROM" syntax, supported by SQLite and others, to name the additional `audit_transaction` table in the WHERE clause.

To UPDATE or DELETE a many-to-many collection where multi-table syntax is not available, the many-to-many criteria may be moved into SELECT that for example may be combined with IN to match rows. The `.WriteOnlyCollection` still helps us here, as we use the `.WriteOnlyCollection.select method to generate this SELECT for us, making use of the sql.Select.with_only_columns` method to produce a `scalar subquery`:

```
>>> from sqlalchemy import update
>>> subq = bank_audit.account_transactions.select().with_only_columns(AccountTransaction.id)
>>> session.execute(
...     update(AccountTransaction)
...     .values(description=AccountTransaction.description + " (audited)")
...     .where(AccountTransaction.id.in_(subq))
... )
{execsql}UPDATE account_transaction SET description=(account_transaction.description || ?)
WHERE account_transaction.id IN (SELECT account_transaction.id
FROM audit_transaction
WHERE ? = audit_transaction.audit_id AND account_transaction.id = audit_transaction.transaction_id)
RETURNING id
[...] (' (audited)', 1)
<...>
```

### Write Only Collections - API Documentation

## Dynamic Relationship Loaders

The dynamic relationship strategy allows configuration of a `_orm.relationship which when accessed on an instance will return a legacy orm.Query object in place of the collection. The orm.Query can then be modified further so that the database collection may be iterated based on filtering criteria. The returned orm.Query object is an instance of orm.AppenderQuery, which combines the loading and iteration behavior of orm.Query along with rudimentary collection mutation methods such as orm.AppenderQuery.append and orm.AppenderQuery.remove`.

The "dynamic" loader strategy may be configured with type-annotated Declarative form using the `_orm.DynamicMapped` annotation class:

```
from sqlalchemy.orm import DynamicMapped

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    posts: DynamicMapped[Post] = relationship()
```

Above, the `User.posts` collection on an individual `User object will return the orm.AppenderQuery object, which is a subclass of orm.Query` that also supports basic collection mutation operations:

```
jack = session.get(User, id)

# filter Jack's blog posts
posts = jack.posts.filter(Post.headline == "this is a post")

# apply array slices
posts = jack.posts[5:20]
```

The dynamic relationship supports limited write operations, via the `_orm.AppenderQuery.append and orm.AppenderQuery.remove` methods:

```
oldpost = jack.posts.filter(Post.headline == "old post").one()
jack.posts.remove(oldpost)

jack.posts.append(Post("new post"))
```

Since the read side of the dynamic relationship always queries the database, changes to the underlying collection will not be visible until the data has been flushed.  However, as long as "autoflush" is enabled on the `.Session` in use, this will occur automatically each time the collection is about to emit a query.

### Dynamic Relationship Loaders - API

## Setting RaiseLoad

A "raise"-loaded relationship will raise an `sqlalchemy.exc.InvalidRequestError` where the attribute would normally emit a lazy load:

```
class MyClass(Base):
    __tablename__ = "some_table"

    # ...

    children: Mapped[List[MyRelatedClass]] = relationship(lazy="raise")
```

Above, attribute access on the `children collection will raise an exception if it was not previously populated.  This includes read access but for collections will also affect write access, as collections can't be mutated without first loading them.  The rationale for this is to ensure that an application is not emitting any unexpected lazy loads within a certain context. Rather than having to read through SQL logs to determine that all necessary attributes were eager loaded, the "raise" strategy will cause unloaded attributes to raise immediately if accessed.  The raise strategy is also available on a query option basis using the orm.raiseload` loader option.

> **Seealso:**  `prevent_lazy_with_raiseload`

## Using Passive Deletes

An important aspect of collection management in SQLAlchemy is that when an object that refers to a collection is deleted, SQLAlchemy needs to consider the objects that are inside this collection. Those objects will need to be de-associated from the parent, which for a one-to-many collection would mean that foreign key columns are set to NULL, or based on `cascade <unitofwork_cascades>` settings, may instead want to emit a DELETE for these rows.

The `unit of work process only considers objects on a row-by-row basis, meaning a DELETE operation implies that all rows within a collection must be fully loaded into memory inside the flush process. This is not feasible for large collections, so we instead seek to rely upon the database's own capability to update or delete the rows automatically using foreign key ON DELETE rules, instructing the unit of work to forego actually needing to load these rows in order to handle them. The unit of work can be instructed to work in this manner by configuring orm.relationship.passive_deletes on the orm.relationship` construct; the foreign key constraints in use must also be correctly configured.

For further detail on a complete "passive delete" configuration, see the section `passive_deletes`.
