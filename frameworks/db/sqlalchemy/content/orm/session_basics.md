---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/session_basics.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

==============

# Session Basics

## What does the Session do ?

In the most general sense, the `.Session` establishes all conversations with the database and represents a "holding zone" for all the objects which you've loaded or associated with it during its lifespan. It provides the interface where SELECT and other queries are made that will return and modify ORM-mapped objects.  The ORM objects themselves are maintained inside the `.Session`, inside a structure called the `identity map` - a data structure that maintains unique copies of each object, where "unique" means "only one object with a particular primary key".

The `.Session in its most common pattern of use begins in a mostly stateless form. Once queries are issued or other objects are persisted with it, it requests a connection resource from an engine.Engine` that is associated with the `.Session`, and then establishes a transaction on that connection. This transaction remains in effect until the `.Session is instructed to commit or roll back the transaction.   When the transaction ends, the connection resource associated with the engine.Engine` is `released` to the connection pool managed by the engine.   A new transaction then starts with a new connection checkout.

The ORM objects maintained by a `_orm.Session` are `instrumented such that whenever an attribute or a collection is modified in the Python program, a change event is generated which is recorded by the orm.Session.  Whenever the database is about to be queried, or when the transaction is about to be committed, the orm.Session` first **flushes** all pending changes stored in memory to the database. This is known as the `unit of work` pattern.

When using a `.Session`, it's useful to consider the ORM mapped objects that it maintains as **proxy objects** to database rows, which are local to the transaction being held by the `.Session`.    In order to maintain the state on the objects as matching what's actually in the database, there are a variety of events that will cause objects to re-access the database in order to keep synchronized.   It is possible to "detach" objects from a `.Session`, and to continue using them, though this practice has its caveats.  It's intended that usually, you'd re-associate detached objects with another `.Session` when you want to work with them again, so that they can resume their normal task of representing database state.

## Basics of Using a Session

The most basic `.Session` use patterns are presented here.

### Opening and Closing a Session

The `_orm.Session may be constructed on its own or by using the orm.sessionmaker class.    It typically is passed a single engine.Engine` as a source of connectivity up front.  A typical use may look like:

```
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# an Engine, which the Session will use for connection
# resources
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/")

# create session and add objects
with Session(engine) as session:
    session.add(some_object)
    session.add(some_other_object)
    session.commit()
```

Above, the `_orm.Session is instantiated with an engine.Engine` associated with a particular database URL.   It is then used in a Python context manager (i.e. `with: statement) so that it is automatically closed at the end of the block; this is equivalent to calling the orm.Session.close` method.

The call to `_orm.Session.commit is optional, and is only needed if the work we've done with the orm.Session includes new data to be persisted to the database.  If we were only issuing SELECT calls and did not need to write any changes, then the call to orm.Session.commit` would be unnecessary.

> **Note:**  Note that after `_orm.Session.commit` is called, either explicitly or
 when using a context manager, all objects associated with the
 `.Session` are `expired`, meaning their contents are erased to
 be re-loaded within the next transaction. If these objects are instead
 `detached`, they will be non-functional until re-associated with a
 new `.Session`, unless the `.Session.expire_on_commit`
 parameter is used to disable this behavior. See the
 section `session_committing` for more detail.

### Framing out a begin / commit / rollback block

We may also enclose the `_orm.Session.commit call and the overall "framing" of the transaction within a context manager for those cases where we will be committing data to the database.  By "framing" we mean that if all operations succeed, the orm.Session.commit method will be called, but if any exceptions are raised, the orm.Session.rollback` method will be called so that the transaction is rolled back immediately, before propagating the exception outward.   In Python this is most fundamentally expressed using a `try: / except: / else:` block such as:

```
# verbose version of what a context manager will do
with Session(engine) as session:
    session.begin()
    try:
        session.add(some_object)
        session.add(some_other_object)
    except:
        session.rollback()
        raise
    else:
        session.commit()
```

The long-form sequence of operations illustrated above can be achieved more succinctly by making use of the `_orm.SessionTransaction object returned by the orm.Session.begin` method, which provides a context manager interface for the same sequence of operations:

```
# create session and add objects
with Session(engine) as session:
    with session.begin():
        session.add(some_object)
        session.add(some_other_object)
    # inner context calls session.commit(), if there were no exceptions
# outer context calls session.close()
```

More succinctly, the two contexts may be combined:

```
# create session and add objects
with Session(engine) as session, session.begin():
    session.add(some_object)
    session.add(some_other_object)
# inner context calls session.commit(), if there were no exceptions
# outer context calls session.close()
```

### Using a sessionmaker

The purpose of `_orm.sessionmaker is to provide a factory for orm.Session objects with a fixed configuration.   As it is typical that an application will have an engine.Engine object in module scope, the orm.sessionmaker can provide a factory for orm.Session` objects that are constructed against this engine:

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources, typically in module scope
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/")

# a sessionmaker(), also in the same scope as the engine
Session = sessionmaker(engine)

# we can now construct a Session() without needing to pass the
# engine each time
with Session() as session:
    session.add(some_object)
    session.add(some_other_object)
    session.commit()
# closes the session
```

The `_orm.sessionmaker is analogous to the engine.Engine as a module-level factory for function-level sessions / connections.   As such it also has its own orm.sessionmaker.begin method, analogous to engine.Engine.begin, which returns a orm.Session` object and also maintains a begin/commit/rollback block:

```
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/")

# a sessionmaker(), also in the same scope as the engine
Session = sessionmaker(engine)

# we can now construct a Session() and include begin()/commit()/rollback()
# at once
with Session.begin() as session:
    session.add(some_object)
    session.add(some_other_object)
# commits the transaction, closes the session
```

Where above, the `_orm.Session will both have its transaction committed as well as that the orm.Session` will be closed, when the above `with:` block ends.

When you write your application, the `.sessionmaker factory should be scoped the same as the engine.Engine object created by sa.create_engine`, which is typically at module-level or global scope.  As these objects are both factories, they can be used by any number of functions and threads simultaneously.

> **Seealso:**  `_orm.sessionmaker`
 `_orm.Session`

### Querying

The primary means of querying is to make use of the `_sql.select construct to create a sql.Select object, which is then executed to return a result using methods such as orm.Session.execute and orm.Session.scalars.  Results are then returned in terms of result.Result objects, including sub-variants such as result.ScalarResult`.

A complete guide to SQLAlchemy ORM querying can be found at `queryguide_toplevel`.   Some brief examples follow:

```
from sqlalchemy import select
from sqlalchemy.orm import Session

with Session(engine) as session:
    # query for ``User`` objects
    statement = select(User).filter_by(name="ed")

    # list of ``User`` objects
    user_obj = session.scalars(statement).all()

    # query for individual columns
    statement = select(User.name, User.fullname)

    # list of Row objects
    rows = session.execute(statement).all()
```

.. versionchanged:: 2.0

> **Seealso:** `queryguide_toplevel`

### Adding New or Existing Items

`.Session.add` is used to place instances in the session. For `transient` (i.e. brand new) instances, this will have the effect of an INSERT taking place for those instances upon the next flush. For instances which are `persistent` (i.e. were loaded by this session), they are already present and do not need to be added. Instances which are `detached` (i.e. have been removed from a session) may be re-associated with a session using this method:

```
user1 = User(name="user1")
user2 = User(name="user2")
session.add(user1)
session.add(user2)

session.commit()  # write changes to the database
```

To add a list of items to the session at once, use `.Session.add_all`:

```
session.add_all([item1, item2, item3])
```

The `.Session.add` operation **cascades** along the `save-update` cascade. For more details see the section `unitofwork_cascades`.

### Deleting

The `.Session.delete` method places an instance into the Session's list of objects to be marked as deleted:

```
# mark two objects to be deleted
session.delete(obj1)
session.delete(obj2)

# commit (or flush)
session.commit()
```

`_orm.Session.delete marks an object for deletion, which will result in a DELETE statement emitted for each primary key affected. Before the pending deletes are flushed, objects marked by "delete" are present in the orm.Session.deleted collection.  After the DELETE, they are expunged from the orm.Session`, which becomes permanent after the transaction is committed.

There are various important behaviors related to the `_orm.Session.delete` operation, particularly in how relationships to other objects and collections are handled.    There's more information on how this works in the section `unitofwork_cascades`, but in general the rules are:

- Rows that correspond to mapped objects that are related to a deleted
object via the `_orm.relationship` directive are **not deleted by default**.  If those objects have a foreign key constraint back to the row being deleted, those columns are set to NULL.   This will cause a constraint violation if the columns are non-nullable.

- To change the "SET NULL" into a DELETE of a related object's row, use the
`cascade_delete cascade on the orm.relationship`.

- Rows that are in tables linked as "many-to-many" tables, via the
`_orm.relationship.secondary` parameter, **are** deleted in all cases when the object they refer to is deleted.

- When related objects include a foreign key constraint back to the object
being deleted, and the related collections to which they belong are not currently loaded into memory, the unit of work will emit a SELECT to fetch all related rows, so that their primary key values can be used to emit either UPDATE or DELETE statements on those related rows.  In this way, the ORM without further instruction will perform the function of ON DELETE CASCADE, even if this is configured on Core `_schema.ForeignKeyConstraint` objects.

- The `_orm.relationship.passive_deletes` parameter can be used
to tune this behavior and rely upon "ON DELETE CASCADE" more naturally; when set to True, this SELECT operation will no longer take place, however rows that are locally present will still be subject to explicit SET NULL or DELETE.   Setting `_orm.relationship.passive_deletes` to the string `"all"` will disable **all** related object update/delete.

- When the DELETE occurs for an object marked for deletion, the object
is not automatically removed from collections or object references that refer to it.   When the `_orm.Session is expired, these collections may be loaded again so that the object is no longer present.  However, it is preferable that instead of using orm.Session.delete` for these objects, the object should instead be removed from its collection and then `cascade_delete_orphan` should be used so that it is deleted as a secondary effect of that collection removal.   See the section `session_deleting_from_collections` for an example of this.

> **Seealso:**  `cascade_delete` - describes "delete cascade", which marks related
 objects for deletion when a lead object is deleted.
 `cascade_delete_orphan` - describes "delete orphan cascade", which
 marks related objects for deletion when they are de-associated from their
 lead object.
 `session_deleting_from_collections` - important background on
 `_orm.Session.delete` as involves relationships being refreshed
 in memory.

### Flushing

When the `sqlalchemy.orm.session.Session is used with its default configuration, the flush step is nearly always done transparently. Specifically, the flush occurs before any individual SQL statement is issued as a result of a query.Query` or a `2.0-style orm.Session.execute` call, as well as within the `.Session.commit` call before the transaction is committed. It also occurs before a SAVEPOINT is issued when `.Session.begin_nested` is used.

A `.Session` flush can be forced at any time by calling the `.Session.flush` method:

```
session.flush()
```

The flush which occurs automatically within the scope of certain methods is known as **autoflush**.  Autoflush is defined as a configurable, automatic flush call which occurs at the beginning of methods including:

- `_orm.Session.execute` and other SQL-executing methods, when used
against ORM-enabled SQL constructs, such as `_sql.select` objects that refer to ORM entities and/or ORM-mapped attributes

- When a `_query.Query` is invoked to send SQL to the database
- Within the `.Session.merge` method before querying the database
- When objects are `refreshed <session_expiring>`
- When ORM `lazy load` operations occur against unloaded object
attributes.

There are also points at which flushes occur **unconditionally**; these points are within key transactional boundaries which include:

- Within the process of the `.Session.commit` method
- When `.Session.begin_nested` is called
- When the `.Session.prepare` 2PC method is used.
The **autoflush** behavior, as applied to the previous list of items, can be disabled by constructing a `.Session` or `.sessionmaker` passing the `.Session.autoflush` parameter as `False`:

```
Session = sessionmaker(autoflush=False)
```

Additionally, autoflush can be temporarily disabled within the flow of using a `.Session` using the `.Session.no_autoflush` context manager:

```
with mysession.no_autoflush:
    mysession.add(some_object)
    mysession.flush()
```

**To reiterate:** The flush process **always occurs** when transactional methods such as `.Session.commit` and `.Session.begin_nested` are called, regardless of any "autoflush" settings, when the `.Session` has remaining pending changes to process.

As the `.Session` only invokes SQL to the database within the context of a `DBAPI` transaction, all "flush" operations themselves only occur within a database transaction (subject to the `isolation level <session_transaction_isolation>` of the database transaction), provided that the DBAPI is not in `driver level autocommit <dbapi_autocommit>` mode. This means that assuming the database connection is providing for `atomicity` within its transactional settings, if any individual DML statement inside the flush fails, the entire operation will be rolled back.

When a failure occurs within a flush, in order to continue using that same `_orm.Session`, an explicit call to `.Session.rollback` is required after a flush fails, even though the underlying transaction will have been rolled back already (even if the database driver is technically in driver-level autocommit mode).  This is so that the overall nesting pattern of so-called "subtransactions" is consistently maintained. The FAQ section `faq_session_rollback` contains a more detailed description of this behavior.

> **Seealso:**  `faq_session_rollback` - further background on why
 `_orm.Session.rollback` must be called when a flush fails.

### Get by Primary Key

As the `_orm.Session` makes use of an `identity map which refers to current in-memory objects by primary key, the orm.Session.get` method is provided as a means of locating objects by primary key, first looking within the current identity map and then querying the database for non present values.  Such as, to locate a `User` entity with primary key identity `(5, )`:

```
my_user = session.get(User, 5)
```

The `_orm.Session.get also includes calling forms for composite primary key values, which may be passed as tuples or dictionaries, as well as additional parameters which allow for specific loader and execution options. See orm.Session.get` for the complete parameter list.

> **Seealso:**  `_orm.Session.get`

### Expiring / Refreshing

An important consideration that will often come up when using the `_orm.Session` is that of dealing with the state that is present on objects that have been loaded from the database, in terms of keeping them synchronized with the current state of the transaction.   The SQLAlchemy ORM is based around the concept of an `identity map` such that when an object is "loaded" from a SQL query, there will be a unique Python object instance maintained corresponding to a particular database identity. This means if we emit two separate queries, each for the same row, and get a mapped object back, the two queries will have returned the same Python object:

```
>>> u1 = session.scalars(select(User).where(User.id == 5)).one()
>>> u2 = session.scalars(select(User).where(User.id == 5)).one()
>>> u1 is u2
True
```

Following from this, when the ORM gets rows back from a query, it will **skip the population of attributes** for an object that's already loaded. The design assumption here is to assume a transaction that's perfectly isolated, and then to the degree that the transaction isn't isolated, the application can take steps on an as-needed basis to refresh objects from the database transaction.  The FAQ entry at `faq_session_identity` discusses this concept in more detail.

When an ORM mapped object is loaded into memory, there are three general ways to refresh its contents with new data from the current transaction:

- **the expire() method** - the `_orm.Session.expire` method will
erase the contents of selected or all attributes of an object, such that they will be loaded from the database when they are next accessed, e.g. using a `lazy loading` pattern:

```
session.expire(u1)
u1.some_attribute  # <-- lazy loads from the transaction

..
```

- **the refresh() method** - closely related is the `_orm.Session.refresh`
method, which does everything the `_orm.Session.expire` method does but also emits one or more SQL queries immediately to actually refresh the contents of the object:

```
session.refresh(u1)  # <-- emits a SQL query
u1.some_attribute  # <-- is refreshed from the transaction

..
```

- **the populate_existing() method or execution option** - This is now
an execution option documented at `orm_queryguide_populate_existing; in legacy form it's found on the orm.Query object as the orm.Query.populate_existing` method. This operation in either form indicates that objects being returned from a query should be unconditionally re-populated from their contents in the database:

```
u2 = session.scalars(
    select(User).where(User.id == 5).execution_options(populate_existing=True)
).one()

..
```

Further discussion on the refresh / expire concept can be found at `session_expire`.

> **Seealso:** `session_expire`
`faq_session_identity`

### UPDATE and DELETE with arbitrary WHERE clause

SQLAlchemy 2.0 includes enhanced capabilities for emitting several varieties of ORM-enabled INSERT, UPDATE and DELETE statements.  See the document at `queryguide/dml` for documentation.

> **Seealso:**  `queryguide/dml`
 `orm_queryguide_update_delete_where`

### Auto Begin

The `_orm.Session object features a behavior known as **autobegin**. This indicates that the orm.Session will internally consider itself to be in a "transactional" state as soon as any work is performed with the orm.Session, either involving modifications to the internal state of the orm.Session` with regards to object state changes, or with operations that require database connectivity.

When the `_orm.Session is first constructed, there's no transactional state present.   The transactional state is begun automatically, when a method such as orm.Session.add or orm.Session.execute is invoked, or similarly if a orm.Query is executed to return results (which ultimately uses orm.Session.execute`), or if an attribute is modified on a `persistent` object.

The transactional state can be checked by accessing the `_orm.Session.in_transaction` method, which returns `True` or `False indicating if the "autobegin" step has proceeded. While not normally needed, the orm.Session.get_transaction method will return the actual orm.SessionTransaction` object that represents this transactional state.

The transactional state of the `_orm.Session may also be started explicitly, by invoking the orm.Session.begin method.   When this method is called, the orm.Session is placed into the "transactional" state unconditionally.   orm.Session.begin` may be used as a context manager as described at `session_begin_commit_rollback_block`.

#### Disabling Autobegin to Prevent Implicit Transactions

The "autobegin" behavior may be disabled using the `_orm.Session.autobegin` parameter set to `False. By using this parameter, a orm.Session will require that the orm.Session.begin method is called explicitly. Upon construction, as well as after any of the orm.Session.rollback, orm.Session.commit, or orm.Session.close methods are called, the orm.Session won't implicitly begin any new transactions and will raise an error if an attempt to use the orm.Session is made without first calling orm.Session.begin`:

```
with Session(engine, autobegin=False) as session:
    session.begin()  # <-- required, else InvalidRequestError raised on next call

    session.add(User(name="u1"))
    session.commit()

    session.begin()  # <-- required, else InvalidRequestError raised on next call

    u1 = session.scalar(select(User).filter_by(name="u1"))
```

.. versionadded:: 2.0 Added `_orm.Session.autobegin`, allowing

### Committing

`.Session.commit` is used to commit the current transaction.   At its core this indicates that it emits `COMMIT` on all current database connections that have a transaction in progress; from a `DBAPI` perspective this means the `connection.commit()` DBAPI method is invoked on each DBAPI connection.

When there is no transaction in place for the `.Session`, indicating that no operations were invoked on this `.Session` since the previous call to `.Session.commit`, the method will begin and commit an internal-only "logical" transaction, that does not normally affect the database unless pending flush changes were detected, but will still invoke event handlers and object expiration rules.

The `_orm.Session.commit` operation unconditionally issues `.Session.flush` before emitting COMMIT on relevant database connections. If no pending changes are detected, then no SQL is emitted to the database. This behavior is not configurable and is not affected by the `.Session.autoflush` parameter.

Subsequent to that, assuming the `_orm.Session is bound to an engine.Engine, orm.Session.commit will then COMMIT the actual database transaction that is in place, if one was started.   After the commit, the engine.Connection` object associated with that transaction is closed, causing its underlying DBAPI connection to be `released back to the connection pool associated with the engine.Engine to which the orm.Session` is bound.

For a `_orm.Session` that's bound to multiple engines (e.g. as described at `Partitioning Strategies <session_partitioning>), the same COMMIT steps will proceed for each engine.Engine / engine.Connection` that is in play within the "logical" transaction being committed.  These database transactions are uncoordinated with each other unless `two-phase features <session_twophase>` are enabled.

Other connection-interaction patterns are available as well, by binding the `_orm.Session to a engine.Connection` directly; in this case, it's assumed that an externally-managed transaction is present, and a real COMMIT will not be emitted automatically in this case; see the section `session_external_transaction` for background on this pattern.

Finally, all objects within the `_orm.Session` are `expired as the transaction is closed out. This is so that when the instances are next accessed, either through attribute access or by them being present in the result of a SELECT, they receive the most recent state. This behavior may be controlled by the orm.Session.expire_on_commit` flag, which may be set to `False` when this behavior is undesirable.

> **Seealso:**  `session_autobegin`

### Rolling Back

`.Session.rollback` rolls back the current transaction, if any. When there is no transaction in place, the method passes silently.

With a default configured session, the post-rollback state of the session, subsequent to a transaction having been begun either via `autobegin <session_autobegin> or by calling the orm.Session.begin` method explicitly, is as follows:

- Database transactions are rolled back.  For a `_orm.Session`
bound to a single `_engine.Engine, this means ROLLBACK is emitted for at most a single engine.Connection that's currently in use. For orm.Session objects bound to multiple engine.Engine objects, ROLLBACK is emitted for all engine.Connection` objects that were checked out.

- Database connections are `released`.  This follows the same connection-related
behavior noted in `session_committing, where engine.Connection objects obtained from engine.Engine` objects are closed, causing the DBAPI connections to be `released to the connection pool within the engine.Engine.   New connections are checked out from the engine.Engine` if and when a new transaction begins.

- For a `_orm.Session`
that's bound directly to a `_engine.Connection` as described at `session_external_transaction, rollback behavior on this engine.Connection would follow the behavior specified by the orm.Session.join_transaction_mode` parameter, which could involve rolling back savepoints or emitting a real ROLLBACK.

- Objects which were initially in the `pending` state when they were added
to the `sqlalchemy.orm.session.Session` within the lifespan of the transaction are expunged, corresponding to their INSERT statement being rolled back. The state of their attributes remains unchanged.

- Objects which were marked as `deleted` within the lifespan of the
transaction are promoted back to the `persistent` state, corresponding to their DELETE statement being rolled back. Note that if those objects were first `pending` within the transaction, that operation takes precedence instead.

- All objects not expunged are fully expired - this is regardless of the
`_orm.Session.expire_on_commit` setting.

With that state understood, the `_orm.Session` may safely continue usage after a rollback occurs.

.. versionchanged:: 1.4

When a `_orm.Session.flush fails, typically for reasons like primary key, foreign key, or "not nullable" constraint violations, a ROLLBACK is issued automatically (it's currently not possible for a flush to continue after a partial failure). However, the orm.Session goes into a state known as "inactive" at this point, and the calling application must always call the orm.Session.rollback method explicitly so that the orm.Session` can go back into a usable state (it can also be simply closed and discarded). See the FAQ entry at `faq_session_rollback` for further discussion.

> **Seealso:** `session_autobegin`

### Closing

The `.Session.close` method issues a `.Session.expunge_all` which removes all ORM-mapped objects from the session, and `releases any transactional/connection resources from the engine.Engine` object(s) to which it is bound.   When connections are returned to the connection pool, transactional state is rolled back as well.

By default, when the `_orm.Session is closed, it is essentially in the original state as when it was first constructed, and **may be used again**. In this sense, the orm.Session.close method is more like a "reset" back to the clean state and not as much like a "database close" method. In this mode of operation the method orm.Session.reset is an alias to orm.Session.close` and behaves in the same way.

The default behavior of `_orm.Session.close can be changed by setting the parameter orm.Session.close_resets_only` to `False, indicating that the orm.Session cannot be reused after the method orm.Session.close has been called. In this mode of operation the orm.Session.reset method will allow multiple "reset" of the session, behaving like orm.Session.close when orm.Session.close_resets_only` is set to `True`.

.. versionadded:: 2.0.22

It's recommended that the scope of a `_orm.Session be limited by a call to orm.Session.close at the end, especially if the orm.Session.commit or orm.Session.rollback methods are not used.    The orm.Session may be used as a context manager to ensure that orm.Session.close` is called:

```
with Session(engine) as session:
    result = session.execute(select(User))

# closes session automatically
```

.. versionchanged:: 1.4

## Session Frequently Asked Questions

By this point, many users already have questions about sessions. This section presents a mini-FAQ (note that we have also a `real FAQ </faq/index>`) of the most basic issues one is presented with when using a `.Session`.

### When do I make a `.sessionmaker`?

Just one time, somewhere in your application's global scope. It should be looked upon as part of your application's configuration. If your application has three .py files in a package, you could, for example, place the `.sessionmaker line in your _init__.py` file; from that point on your other modules say "from mypackage import Session". That way, everyone else just uses `.Session()`, and the configuration of that session is controlled by that central point.

If your application starts up, does imports, but does not know what database it's going to be connecting to, you can bind the `.Session` at the "class" level to the engine later on, using `.sessionmaker.configure`.

In the examples in this section, we will frequently show the `.sessionmaker` being created right above the line where we actually invoke `.Session`. But that's just for example's sake!  In reality, the `.sessionmaker` would be somewhere at the module level.   The calls to instantiate `.Session` would then be placed at the point in the application where database conversations begin.

### When do I construct a `.Session`, when do I commit it, and when do I close it?

A `.Session` is typically constructed at the beginning of a logical operation where database access is potentially anticipated.

The `.Session`, whenever it is used to talk to the database, begins a database transaction as soon as it starts communicating. This transaction remains in progress until the `.Session` is rolled back, committed, or closed.   The `.Session` will begin a new transaction if it is used again, subsequent to the previous transaction ending; from this it follows that the `.Session` is capable of having a lifespan across many transactions, though only one at a time.   We refer to these two concepts as **transaction scope** and **session scope**.

It's usually not very hard to determine the best points at which to begin and end the scope of a `.Session`, though the wide variety of application architectures possible can introduce challenging situations.

Some sample scenarios include:

- Web applications.  In this case, it's best to make use of the SQLAlchemy
integrations provided by the web framework in use.  Or otherwise, the basic pattern is create a `_orm.Session at the start of a web request, call the orm.Session.commit method at the end of web requests that do POST, PUT, or DELETE, and then close the session at the end of web request.  It's also usually a good idea to set orm.Session.expire_on_commit to False so that subsequent access to objects that came from a orm.Session` within the view layer do not need to emit new SQL queries to refresh the objects, if the transaction has been committed already.

- A background daemon which spawns off child forks
would want to create a `.Session` local to each child process, work with that `.Session` through the life of the "job" that the fork is handling, then tear it down when the job is completed.

- For a command-line script, the application would create a single, global
`.Session` that is established when the program begins to do its work, and commits it right as the program is completing its task.

- For a GUI interface-driven application, the scope of the `.Session`
may best be within the scope of a user-generated event, such as a button push.  Or, the scope may correspond to explicit user interaction, such as the user "opening" a series of records, then "saving" them.

As a general rule, the application should manage the lifecycle of the session externally to functions that deal with specific data.  This is a fundamental separation of concerns which keeps data-specific operations agnostic of the context in which they access and manipulate that data.

E.g. **don't do this**:

```
### this is the **wrong way to do it** ###

class ThingOne:
    def go(self):
        session = Session()
        try:
            session.execute(update(FooBar).values(x=5))
            session.commit()
        except:
            session.rollback()
            raise

class ThingTwo:
    def go(self):
        session = Session()
        try:
            session.execute(update(Widget).values(q=18))
            session.commit()
        except:
            session.rollback()
            raise

def run_my_program():
    ThingOne().go()
    ThingTwo().go()
```

Keep the lifecycle of the session (and usually the transaction) **separate and external**.  The example below illustrates how this might look, and additionally makes use of a Python context manager (i.e. the `with: keyword) in order to manage the scope of the orm.Session` and its transaction automatically:

```
### this is a **better** (but not the only) way to do it ###

class ThingOne:
    def go(self, session):
        session.execute(update(FooBar).values(x=5))

class ThingTwo:
    def go(self, session):
        session.execute(update(Widget).values(q=18))

def run_my_program():
    with Session() as session:
        with session.begin():
            ThingOne().go(session)
            ThingTwo().go(session)
```

.. versionchanged:: 1.4 The `_orm.Session` may be used as a context

### Is the Session a cache?

Yeee...no. It's somewhat used as a cache, in that it implements the `identity map` pattern, and stores objects keyed to their primary key. However, it doesn't do any kind of query caching. This means, if you say `session.scalars(select(Foo).filter_by(name='bar'))`, even if `Foo(name='bar')` is right there, in the identity map, the session has no idea about that. It has to issue SQL to the database, get the rows back, and then when it sees the primary key in the row, then it can look in the local identity map and see that the object is already there. It's only when you say `query.get({some primary key})` that the `sqlalchemy.orm.session.Session` doesn't have to issue a query.

Additionally, the Session stores object instances using a weak reference by default. This also defeats the purpose of using the Session as a cache.

The `.Session` is not designed to be a global object from which everyone consults as a "registry" of objects. That's more the job of a **second level cache**.   SQLAlchemy provides a pattern for implementing second level caching using [dogpile.cache](https://dogpilecache.readthedocs.io/), via the `examples_caching` example.

### How can I get the `sqlalchemy.orm.session.Session` for a certain object?

Use the `.Session.object_session` classmethod available on `sqlalchemy.orm.session.Session`:

```
session = Session.object_session(someobject)
```

The newer `core_inspection_toplevel` system can also be used:

```
from sqlalchemy import inspect

session = inspect(someobject).session
```

### Is the Session thread-safe?  Is AsyncSession safe to share in concurrent tasks?

The `.Session` is a **mutable, stateful** object that represents a **single database transaction**.   An instance of `.Session` therefore **cannot be shared among concurrent threads or asyncio tasks without careful synchronization**. The `.Session` is intended to be used in a **non-concurrent** fashion, that is, a particular instance of `.Session` should be used in only one thread or task at a time.

When using the `_asyncio.AsyncSession` object from SQLAlchemy's `asyncio <asyncio_toplevel> extension, this object is only a thin proxy on top of a orm.Session, and the same rules apply; it is an **unsynchronized, mutable, stateful object**, so it is **not** safe to use a single instance of asyncio.AsyncSession` in multiple asyncio tasks at once.

An instance of `.Session or asyncio.AsyncSession represents a single logical database transaction, referencing only a single engine.Connection` at a time for a particular `.Engine` or `.AsyncEngine` to which the object is bound (note that these objects both support being bound to multiple engines at once, however in this case there will still be only one connection per engine in play within the scope of a transaction).

A database connection within a transaction is also a stateful object that is intended to be operated upon in a non-concurrent, sequential fashion. Commands are issued on the connection in a sequence, which are handled by the database server in the exact order in which they are emitted.   As the `_orm.Session emits commands upon this connection and receives results, the orm.Session` itself is transitioning through internal state changes that align with the state of commands and data present on this connection; states which include if a transaction were begun, committed, or rolled back, what SAVEPOINTs if any are in play, as well as fine-grained synchronization of the state of individual database rows with local ORM-mapped objects.

When designing database applications for concurrency, the appropriate model is that each concurrent task / thread works with its own database transaction. This is why when discussing the issue of database concurrency, the standard terminology used is **multiple, concurrent transactions**.   Within traditional RDMS there is no analogue for a single database transaction that is receiving and processing multiple commands concurrently.

The concurrency model for SQLAlchemy's `_orm.Session and asyncio.AsyncSession` is therefore **Session per thread, AsyncSession per task**.  An application that uses multiple threads, or multiple tasks in asyncio such as when using an API like `asyncio.gather() would want to ensure that each thread has its own orm.Session, each asyncio task has its own asyncio.AsyncSession`.

The best way to ensure this use is by using the `standard context manager pattern <session_getting>  locally within the top level Python function that is inside the thread or task, which will ensure the lifespan of the orm.Session or asyncio.AsyncSession` is maintained within a local scope.

For applications that benefit from having a "global" `.Session` where it's not an option to pass the `.Session` object to specific functions and methods which require it, the `.scoped_session` approach can provide for a "thread local" `.Session` object; see the section `unitofwork_contextual` for background.   Within the asyncio context, the `.async_scoped_session` object is the asyncio analogue for `.scoped_session`, however is more challenging to configure as it requires a custom "context" function.
