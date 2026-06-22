---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/queryguide/api.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

.. include:: queryguide_nav_include.rst

=============================

# ORM API Features for Querying

## ORM Loader Options

Loader options are objects which, when passed to the `_sql.Select.options` method of a `.Select object or similar SQL construct, affect the loading of both column and relationship-oriented attributes. The majority of loader options descend from the orm.Load` hierarchy. For a complete overview of using loader options, see the linked sections below.

> **Seealso:**  * `loading_columns` - details mapper and loading options that affect
   how column and SQL-expression mapped attributes are loaded
 * `loading_toplevel` - details relationship and loading options that
   affect how `_orm.relationship` mapped attributes are loaded

## ORM Execution Options

ORM-level execution options are keyword options that may be associated with a statement execution using either the `_orm.Session.execute.execution_options parameter, which is a dictionary argument accepted by orm.Session methods such as orm.Session.execute and orm.Session.scalars, or by associating them directly with the statement to be invoked itself using the sql.Executable.execution_options` method, which accepts them as arbitrary keyword arguments.

ORM-level options are distinct from the Core level execution options documented at `_engine.Connection.execution_options. It's important to note that the ORM options discussed below are **not** compatible with Core level methods engine.Connection.execution_options or engine.Engine.execution_options`; the options are ignored at this level, even if the `.Engine` or `.Connection is associated with the orm.Session` in use.

Within this section, the `_sql.Executable.execution_options` method style will be illustrated for examples.

#### Populate Existing

The `populate_existing execution option ensures that, for all rows loaded, the corresponding instances in the orm.Session` will be fully refreshed – erasing any existing data within the objects (including pending changes) and replacing with the data loaded from the result.

Example use looks like:

```
>>> stmt = select(User).execution_options(populate_existing=True)
>>> result = session.execute(stmt)
{execsql}SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
...
```

Normally, ORM objects are only loaded once, and if they are matched up to the primary key in a subsequent result row, the row is not applied to the object.  This is both to preserve pending, unflushed changes on the object as well as to avoid the overhead and complexity of refreshing data which is already there.   The `_orm.Session` assumes a default working model of a highly isolated transaction, and to the degree that data is expected to change within the transaction outside of the local changes being made, those use cases would be handled using explicit steps such as this method.

Using `populate_existing`, any set of objects that matches a query can be refreshed, and it also allows control over relationship loader options. E.g. to refresh an instance while also refreshing a related set of objects:

```python
 stmt = (
     select(User)
     .where(User.name.in_(names))
     .execution_options(populate_existing=True)
     .options(selectinload(User.addresses))
 )
 # will refresh all matching User objects as well as the related
 # Address objects
 users = session.execute(stmt).scalars().all()
```

Another use case for `populate_existing` is in support of various attribute loading features that can change how an attribute is loaded on a per-query basis.   Options for which this apply include:

- The `_orm.with_expression` option
- The `_orm.PropComparator.and_` method that can modify what a loader
strategy loads

- The `_orm.contains_eager` option
- The `_orm.with_loader_criteria` option
- The `_orm.load_only` option to select what attributes to refresh
The `populate_existing execution option is equvialent to the orm.Query.populate_existing` method in `1.x style` ORM queries.

> **Seealso:**  `faq_session_identity` - in `/faq/index`
 `session_expire - in the ORM orm.Session`
 documentation

#### Autoflush

This option, when passed as `False, will cause the orm.Session to not invoke the "autoflush" step.  It is equivalent to using the orm.Session.no_autoflush` context manager to disable autoflush:

```
>>> stmt = select(User).execution_options(autoflush=False)
>>> session.execute(stmt)
{execsql}SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
...
```

This option will also work on ORM-enabled `_sql.Update and sql.Delete` queries.

The `autoflush execution option is equvialent to the orm.Query.autoflush` method in `1.x style` ORM queries.

> **Seealso:**  `session_flushing`

#### Fetching Large Result Sets with Yield Per

The `yield_per execution option is an integer value which will cause the engine.Result` to buffer only a limited number of rows and/or ORM objects at a time, before making data available to the client.

Normally, the ORM will fetch **all** rows immediately, constructing ORM objects for each and assembling those objects into a single buffer, before passing this buffer to the `_engine.Result` object as a source of rows to be returned. The rationale for this behavior is to allow correct behavior for features such as joined eager loading, uniquifying of results, and the general case of result handling logic that relies upon the identity map maintaining a consistent state for every object in a result set as it is fetched.

The purpose of the `yield_per` option is to change this behavior so that the ORM result set is optimized for iteration through very large result sets (e.g. > 10K rows), where the user has determined that the above patterns don't apply. When `yield_per is used, the ORM will instead batch ORM results into sub-collections and yield rows from each sub-collection individually as the engine.Result object is iterated, so that the Python interpreter doesn't need to declare very large areas of memory which is both time consuming and leads to excessive memory use. The option affects both the way the database cursor is used as well as how the ORM constructs rows and objects to be passed to the engine.Result`.

> **Tip:**  From the above, it follows that the `_engine.Result` must be
 consumed in an iterable fashion, that is, using iteration such as
 `for row in result` or using partial row methods such as
 `_engine.Result.fetchmany or engine.Result.partitions`.
 Calling `_engine.Result.all` will defeat the purpose of using
 `yield_per`.

Using `yield_per is equivalent to making use of both the engine.Connection.execution_options.stream_results execution option, which selects for server side cursors to be used by the backend if supported, and the engine.Result.yield_per method on the returned engine.Result` object, which establishes a fixed size of rows to be fetched as well as a corresponding limit to how many ORM objects will be constructed at once.

> **Tip:**  `yield_per` is now available as a Core execution option as well,
 described in detail at `engine_stream_results`.  This section details
 the use of `yield_per` as an execution option with an ORM
 `_orm.Session`.  The option behaves as similarly as possible
 in both contexts.

When used with the ORM, `yield_per` must be established either via the `.Executable.execution_options method on the given statement or by passing it to the orm.Session.execute.execution_options parameter of orm.Session.execute or other similar orm.Session method such as orm.Session.scalars`.  Typical use for fetching ORM objects is illustrated below:

```
>>> stmt = select(User).execution_options(yield_per=10)
>>> for user_obj in session.scalars(stmt):
...     print(user_obj)
{execsql}SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
[...] ()
{stop}User(id=1, name='spongebob', fullname='Spongebob Squarepants')
User(id=2, name='sandy', fullname='Sandy Cheeks')
...
>>> # ... rows continue ...
```

The above code is equivalent to the example below, which uses `_engine.Connection.execution_options.stream_results and engine.Connection.execution_options.max_row_buffer Core-level execution options in conjunction with the engine.Result.yield_per method of engine.Result`:

```
# equivalent code
>>> stmt = select(User).execution_options(stream_results=True, max_row_buffer=10)
>>> for user_obj in session.scalars(stmt).yield_per(10):
...     print(user_obj)
{execsql}SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
[...] ()
{stop}User(id=1, name='spongebob', fullname='Spongebob Squarepants')
User(id=2, name='sandy', fullname='Sandy Cheeks')
...
>>> # ... rows continue ...
```

`yield_per is also commonly used in combination with the engine.Result.partitions` method, which will iterate rows in grouped partitions. The size of each partition defaults to the integer value passed to `yield_per`, as in the below example:

```
>>> stmt = select(User).execution_options(yield_per=10)
>>> for partition in session.scalars(stmt).partitions():
...     for user_obj in partition:
...         print(user_obj)
{execsql}SELECT user_account.id, user_account.name, user_account.fullname
FROM user_account
[...] ()
{stop}User(id=1, name='spongebob', fullname='Spongebob Squarepants')
User(id=2, name='sandy', fullname='Sandy Cheeks')
...
>>> # ... rows continue ...
```

The `yield_per` execution option **is not compatible** with `"subquery" eager loading <subquery_eager_loading>` loading or `"joined" eager loading <joined_eager_loading>` when using collections. It is potentially compatible with `"select in" eager loading <selectin_eager_loading>` , provided the database driver supports multiple, independent cursors.

Additionally, the `yield_per execution option is not compatible with the engine.Result.unique` method; as this method relies upon storing a complete set of identities for all rows, it would necessarily defeat the purpose of using `yield_per` which is to handle an arbitrarily large number of rows.

.. versionchanged:: 1.4.6  An exception is raised when ORM rows are fetched

When using the legacy `_orm.Query` object with `1.x style ORM use, the orm.Query.yield_per` method will have the same result as that of the `yield_per` execution option.

> **Seealso:**  `engine_stream_results`

#### Identity Token

The "identity token" is an arbitrary value that can be associated within the `identity key` of newly loaded objects.   This element exists first and foremost to support extensions which perform per-row "sharding", where objects may be loaded from any number of replicas of a particular database table that nonetheless have overlapping primary key values. The primary consumer of "identity token" is the `horizontal_sharding_toplevel` extension, which supplies a general framework for persisting objects among multiple "shards" of a particular database table.

The `identity_token execution option may be used on a per-query basis to directly affect this token.   Using it directly, one can populate a orm.Session` with multiple instances of an object that have the same primary key and source table, but different "identities".

One such example is to populate a `_orm.Session` with objects that come from same-named tables in different schemas, using the `schema_translating` feature which can affect the choice of schema within the scope of queries.  Given a mapping as:

```python
 from sqlalchemy.orm import DeclarativeBase
 from sqlalchemy.orm import Mapped
 from sqlalchemy.orm import mapped_column

 class Base(DeclarativeBase):
     pass

 class MyTable(Base):
     __tablename__ = "my_table"

     id: Mapped[int] = mapped_column(primary_key=True)
     name: Mapped[str]
```

The default "schema" name for the class above is `None, meaning, no schema qualification will be written into SQL statements.  However, if we make use of engine.Connection.execution_options.schema_translate_map`, mapping `None` to an alternate schema, we can place instances of `MyTable` into two different schemas:

```python
 engine = create_engine(
     "postgresql+psycopg://scott:tiger@localhost/test",
 )

 with Session(
     engine.execution_options(schema_translate_map={None: "test_schema"})
 ) as sess:
     sess.add(MyTable(name="this is schema one"))
     sess.commit()

 with Session(
     engine.execution_options(schema_translate_map={None: "test_schema_2"})
 ) as sess:
     sess.add(MyTable(name="this is schema two"))
     sess.commit()
```

The above two blocks create a `_orm.Session` object linked to a different schema translate map each time, and an instance of `MyTable` is persisted into both `test_schema.my_table` as well as `test_schema_2.my_table`.

The `_orm.Session` objects above are independent.  If we wanted to persist both objects in one transaction, we would need to use the `horizontal_sharding_toplevel` extension to do this.

However, we can illustrate querying for these objects in one session as follows:

```python
 with Session(engine) as sess:
     obj1 = sess.scalar(
         select(MyTable)
         .where(MyTable.id == 1)
         .execution_options(
             schema_translate_map={None: "test_schema"},
             identity_token="test_schema",
         )
     )
     obj2 = sess.scalar(
         select(MyTable)
         .where(MyTable.id == 1)
         .execution_options(
             schema_translate_map={None: "test_schema_2"},
             identity_token="test_schema_2",
         )
     )
```

Both `obj1` and `obj2` are distinct from each other.  However, they both refer to primary key id 1 for the `MyTable` class, yet are distinct. This is how the `identity_token comes into play, which we can see in the inspection of each object, where we look at orm.InstanceState.key` to view the two distinct identity tokens:

```
>>> from sqlalchemy import inspect
>>> inspect(obj1).key
(<class '__main__.MyTable'>, (1,), 'test_schema')
>>> inspect(obj2).key
(<class '__main__.MyTable'>, (1,), 'test_schema_2')
```

The above logic takes place automatically when using the `horizontal_sharding_toplevel` extension.

.. versionadded:: 2.0.0rc1 - added the `identity_token` ORM level execution

> **Seealso:**  `examples_sharding` - in the `examples_toplevel` section.
 See the script `separate_schema_translates.py` for a demonstration of
 the above use case using the full sharding API.

# Inspecting entities and columns from ORM-enabled SELECT and DML statements

The `_sql.select construct, as well as the sql.insert, sql.update and sql.delete` constructs (for the latter DML constructs, as of SQLAlchemy 1.4.33), all support the ability to inspect the entities in which these statements are created against, as well as the columns and datatypes that would be returned in a result set.

For a `.Select` object, this information is available from the `.Select.column_descriptions` attribute. This attribute operates in the same way as the legacy `.Query.column_descriptions` attribute. The format returned is a list of dictionaries:

```
>>> from pprint import pprint
>>> user_alias = aliased(User, name="user2")
>>> stmt = select(User, User.id, user_alias)
>>> pprint(stmt.column_descriptions)
[{'aliased': False,
  'entity': <class 'User'>,
  'expr': <class 'User'>,
  'name': 'User',
  'type': <class 'User'>},
 {'aliased': False,
  'entity': <class 'User'>,
  'expr': <....InstrumentedAttribute object at ...>,
  'name': 'id',
  'type': Integer()},
 {'aliased': True,
  'entity': <AliasedClass ...; User>,
  'expr': <AliasedClass ...; User>,
  'name': 'user2',
  'type': <class 'User'>}]
```

When `.Select.column_descriptions` is used with non-ORM objects such as plain `.Table` or `.Column` objects, the entries will contain basic information about individual columns returned in all cases:

```
>>> stmt = select(user_table, address_table.c.id)
>>> pprint(stmt.column_descriptions)
[{'expr': Column('id', Integer(), table=<user_account>, primary_key=True, nullable=False),
  'name': 'id',
  'type': Integer()},
 {'expr': Column('name', String(), table=<user_account>, nullable=False),
  'name': 'name',
  'type': String()},
 {'expr': Column('fullname', String(), table=<user_account>),
  'name': 'fullname',
  'type': String()},
 {'expr': Column('id', Integer(), table=<address>, primary_key=True, nullable=False),
  'name': 'id_1',
  'type': Integer()}]
```

.. versionchanged:: 1.4.33 The `.Select.column_descriptions` attribute now returns

For `_sql.insert`, `.update` and `.delete` constructs, there are two separate attributes. One is `.UpdateBase.entity_description` which returns information about the primary ORM entity and database table which the DML construct would be affecting:

```
>>> from sqlalchemy import update
>>> stmt = update(User).values(name="somename").returning(User.id)
>>> pprint(stmt.entity_description)
{'entity': <class 'User'>,
 'expr': <class 'User'>,
 'name': 'User',
 'table': Table('user_account', ...),
 'type': <class 'User'>}
```

> **Tip:** `"table"` which is actually the **table to be inserted, updated or
deleted** by the statement, which is **not** always the same as the SQL
"selectable" to which the class may be mapped. For example, in a
joined-table inheritance scenario, `"table"` will refer to the local table
for the given entity.

The other is `.UpdateBase.returning_column_descriptions` which delivers information about the columns present in the RETURNING collection in a manner roughly similar to that of `.Select.column_descriptions`:

```
>>> pprint(stmt.returning_column_descriptions)
[{'aliased': False,
  'entity': <class 'User'>,
  'expr': <sqlalchemy.orm.attributes.InstrumentedAttribute ...>,
  'name': 'id',
  'type': Integer()}]
```

.. versionadded:: 1.4.33 Added the `.UpdateBase.entity_description`

# Additional ORM API Constructs

>>> session.close() >>> conn.close() ROLLBACK
