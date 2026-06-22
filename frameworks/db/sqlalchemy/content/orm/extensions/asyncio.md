---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/extensions/asyncio.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# Asynchronous I/O (asyncio)

Support for Python asyncio.    Support for Core and ORM usage is included, using asyncio-compatible dialects.

.. versionadded:: 1.4

> **Warning:** installation notes on **all** platforms.

> **Seealso:**  `change_3414` - initial feature announcement
 `examples_asyncio` - example scripts illustrating working examples
 of Core and ORM use within the asyncio extension.

## Asyncio Platform Installation Notes

The asyncio extension depends upon the [greenlet](https://pypi.org/project/greenlet/) library. This dependency is **not installed by default**.

To install SQLAlchemy while ensuring the `greenlet` dependency is present, the `[asyncio]` [setuptools extra](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-setuptools-extras) may be installed as follows, which will include also instruct `pip` to install `greenlet`:

```text
pip install sqlalchemy[asyncio]
```

Note that installation of `greenlet` on platforms that do not have a pre-built wheel file means that `greenlet` will be built from source, which requires that Python's development libraries also be present.

.. versionchanged:: 2.1  `greenlet` is no longer installed by default; to

## Synopsis - Core

For Core use, the `_asyncio.create_async_engine function creates an instance of asyncio.AsyncEngine which then offers an async version of the traditional engine.Engine API.   The asyncio.AsyncEngine delivers an asyncio.AsyncConnection via its asyncio.AsyncEngine.connect and asyncio.AsyncEngine.begin methods which both deliver asynchronous context managers.   The asyncio.AsyncConnection can then invoke statements using either the asyncio.AsyncConnection.execute method to deliver a buffered engine.Result, or the asyncio.AsyncConnection.stream method to deliver a streaming server-side asyncio.AsyncResult`:

```pycon+sql
 >>> import asyncio

 >>> from sqlalchemy import Column
 >>> from sqlalchemy import MetaData
 >>> from sqlalchemy import select
 >>> from sqlalchemy import String
 >>> from sqlalchemy import Table
 >>> from sqlalchemy.ext.asyncio import create_async_engine

 >>> meta = MetaData()
 >>> t1 = Table("t1", meta, Column("name", String(50), primary_key=True))

 >>> async def async_main() -> None:
 ...     engine = create_async_engine("sqlite+aiosqlite://", echo=True)
 ...
 ...     async with engine.begin() as conn:
 ...         await conn.run_sync(meta.drop_all)
 ...         await conn.run_sync(meta.create_all)
 ...
 ...         await conn.execute(
 ...             t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
 ...         )
 ...
 ...     async with engine.connect() as conn:
 ...         # select a Result, which will be delivered with buffered
 ...         # results
 ...         result = await conn.execute(select(t1).where(t1.c.name == "some name 1"))
 ...
 ...         print(result.fetchall())
 ...
 ...     # for AsyncEngine created in function scope, close and
 ...     # clean-up pooled connections
 ...     await engine.dispose()

 >>> asyncio.run(async_main())
 {execsql}BEGIN (implicit)
 ...
 CREATE TABLE t1 (
     name VARCHAR(50) NOT NULL,
     PRIMARY KEY (name)
 )
 ...
 INSERT INTO t1 (name) VALUES (?)
 [...] [('some name 1',), ('some name 2',)]
 COMMIT
 BEGIN (implicit)
 SELECT t1.name
 FROM t1
 WHERE t1.name = ?
 [...] ('some name 1',)
 [('some name 1',)]
 ROLLBACK
```

Above, the `_asyncio.AsyncConnection.run_sync method may be used to invoke special DDL functions such as schema.MetaData.create_all` that don't include an awaitable hook.

> **Tip:** using `await when using the asyncio.AsyncEngine` object in a
scope that will go out of context and be garbage collected, as illustrated in the
`async_main` function in the above example.  This ensures that any
connections held open by the connection pool will be properly disposed
within an awaitable context.   Unlike when using blocking IO, SQLAlchemy
cannot properly dispose of these connections within methods like `__del__`
or weakref finalizers as there is no opportunity to invoke `await`.
Failing to explicitly dispose of the engine when it falls out of scope
may result in warnings emitted to standard out resembling the form
`RuntimeError: Event loop is closed` within garbage collection.

The `_asyncio.AsyncConnection also features a "streaming" API via the asyncio.AsyncConnection.stream method that returns an asyncio.AsyncResult` object.  This result object uses a server-side cursor and provides an async/await API, such as an async iterator:

```
async with engine.connect() as conn:
    async_result = await conn.stream(select(t1))

    async for row in async_result:
        print("row: %s" % (row,))
```

## Synopsis - ORM

Using `2.0 style querying, the asyncio.AsyncSession` class provides full ORM functionality.

Within the default mode of use, special care must be taken to avoid `lazy loading` or other expired-attribute access involving ORM relationships and column attributes; the next section `asyncio_orm_avoid_lazyloads` details this.

> **Warning:**  A single instance of `_asyncio.AsyncSession` is **not safe for
 use in multiple, concurrent tasks**.  See the sections
 `asyncio_concurrency` and `session_faq_threadsafe` for background.

The example below illustrates a complete example including mapper and session configuration:

```pycon+sql
 >>> from __future__ import annotations

 >>> import asyncio
 >>> import datetime
 >>> from typing import List

 >>> from sqlalchemy import ForeignKey
 >>> from sqlalchemy import func
 >>> from sqlalchemy import select
 >>> from sqlalchemy.ext.asyncio import AsyncAttrs
 >>> from sqlalchemy.ext.asyncio import async_sessionmaker
 >>> from sqlalchemy.ext.asyncio import AsyncSession
 >>> from sqlalchemy.ext.asyncio import create_async_engine
 >>> from sqlalchemy.orm import DeclarativeBase
 >>> from sqlalchemy.orm import Mapped
 >>> from sqlalchemy.orm import mapped_column
 >>> from sqlalchemy.orm import relationship
 >>> from sqlalchemy.orm import selectinload

 >>> class Base(AsyncAttrs, DeclarativeBase):
 ...     pass

 >>> class B(Base):
 ...     __tablename__ = "b"
 ...
 ...     id: Mapped[int] = mapped_column(primary_key=True)
 ...     a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
 ...     data: Mapped[str]

 >>> class A(Base):
 ...     __tablename__ = "a"
 ...
 ...     id: Mapped[int] = mapped_column(primary_key=True)
 ...     data: Mapped[str]
 ...     create_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
 ...     bs: Mapped[List[B]] = relationship()

 >>> async def insert_objects(async_session: async_sessionmaker[AsyncSession]) -> None:
 ...     async with async_session() as session:
 ...         async with session.begin():
 ...             session.add_all(
 ...                 [
 ...                     A(bs=[B(data="b1"), B(data="b2")], data="a1"),
 ...                     A(bs=[], data="a2"),
 ...                     A(bs=[B(data="b3"), B(data="b4")], data="a3"),
 ...                 ]
 ...             )

 >>> async def select_and_update_objects(
 ...     async_session: async_sessionmaker[AsyncSession],
 ... ) -> None:
 ...     async with async_session() as session:
 ...         stmt = select(A).order_by(A.id).options(selectinload(A.bs))
 ...
 ...         result = await session.execute(stmt)
 ...
 ...         for a in result.scalars():
 ...             print(a, a.data)
 ...             print(f"created at: {a.create_date}")
 ...             for b in a.bs:
 ...                 print(b, b.data)
 ...
 ...         result = await session.execute(select(A).order_by(A.id).limit(1))
 ...
 ...         a1 = result.scalars().one()
 ...
 ...         a1.data = "new data"
 ...
 ...         await session.commit()
 ...
 ...         # access attribute subsequent to commit; this is what
 ...         # expire_on_commit=False allows
 ...         print(a1.data)
 ...
 ...         # alternatively, AsyncAttrs may be used to access any attribute
 ...         # as an awaitable (new in 2.0.13)
 ...         for b1 in await a1.awaitable_attrs.bs:
 ...             print(b1, b1.data)

 >>> async def async_main() -> None:
 ...     engine = create_async_engine("sqlite+aiosqlite://", echo=True)
 ...
 ...     # async_sessionmaker: a factory for new AsyncSession objects.
 ...     # expire_on_commit - don't expire objects after transaction commit
 ...     async_session = async_sessionmaker(engine, expire_on_commit=False)
 ...
 ...     async with engine.begin() as conn:
 ...         await conn.run_sync(Base.metadata.create_all)
 ...
 ...     await insert_objects(async_session)
 ...     await select_and_update_objects(async_session)
 ...
 ...     # for AsyncEngine created in function scope, close and
 ...     # clean-up pooled connections
 ...     await engine.dispose()

 >>> asyncio.run(async_main())
 {execsql}BEGIN (implicit)
 ...
 CREATE TABLE a (
     id INTEGER NOT NULL,
     data VARCHAR NOT NULL,
     create_date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
     PRIMARY KEY (id)
 )
 ...
 CREATE TABLE b (
     id INTEGER NOT NULL,
     a_id INTEGER NOT NULL,
     data VARCHAR NOT NULL,
     PRIMARY KEY (id),
     FOREIGN KEY(a_id) REFERENCES a (id)
 )
 ...
 COMMIT
 BEGIN (implicit)
 INSERT INTO a (data) VALUES (?) RETURNING id, create_date
 [...] ('a1',)
 ...
 INSERT INTO b (a_id, data) VALUES (?, ?) RETURNING id
 [...] (1, 'b2')
 ...
 COMMIT
 BEGIN (implicit)
 SELECT a.id, a.data, a.create_date
 FROM a ORDER BY a.id
 [...] ()
 SELECT b.a_id, b.id, b.data
 FROM b
 WHERE b.a_id IN (?, ?, ?)
 [...] (1, 2, 3)
 <A object at ...> a1
 created at: ...
 <B object at ...> b1
 <B object at ...> b2
 <A object at ...> a2
 created at: ...
 <A object at ...> a3
 created at: ...
 <B object at ...> b3
 <B object at ...> b4
 SELECT a.id, a.data, a.create_date
 FROM a ORDER BY a.id
 LIMIT ? OFFSET ?
 [...] (1, 0)
 UPDATE a SET data=? WHERE a.id = ?
 [...] ('new data', 1)
 COMMIT
 new data
 <B object at ...> b1
 <B object at ...> b2
```

In the example above, the `_asyncio.AsyncSession is instantiated using the optional asyncio.async_sessionmaker helper, which provides a factory for new asyncio.AsyncSession objects with a fixed set of parameters, which here includes associating it with an asyncio.AsyncEngine` against particular database URL. It is then passed to other methods where it may be used in a Python asynchronous context manager (i.e. `async with: statement) so that it is automatically closed at the end of the block; this is equivalent to calling the asyncio.AsyncSession.close` method.

### Using AsyncSession with Concurrent Tasks

The `_asyncio.AsyncSession` object is a **mutable, stateful object** which represents a **single, stateful database transaction in progress**. Using concurrent tasks with asyncio, with APIs such as `asyncio.gather() for example, should use a **separate** asyncio.AsyncSession` **per individual task**.

See the section `session_faq_threadsafe for a general description of the orm.Session and asyncio.AsyncSession` with regards to how they should be used with concurrent workloads.

### Preventing Implicit IO when Using AsyncSession

Using traditional asyncio, the application needs to avoid any points at which IO-on-attribute access may occur.   Techniques that can be used to help this are below, many of which are illustrated in the preceding example.

- Attributes that are lazy-loading relationships, deferred columns or
expressions, or are being accessed in expiration scenarios can take advantage of the  `_asyncio.AsyncAttrs` mixin.  This mixin, when added to a specific class or more generally to the Declarative `Base superclass, provides an accessor asyncio.AsyncAttrs.awaitable_attrs` which delivers any attribute as an awaitable:

```
from __future__ import annotations

from typing import List

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship

class Base(AsyncAttrs, DeclarativeBase):
    pass

class A(Base):
    __tablename__ = "a"

    # ... rest of mapping ...

    bs: Mapped[List[B]] = relationship()

class B(Base):
    __tablename__ = "b"

    # ... rest of mapping ...

Accessing the ``A.bs`` collection on newly loaded instances of ``A`` when
eager loading is not in use will normally use :term:`lazy loading`, which in
order to succeed will usually emit IO to the database, which will fail under
asyncio as no implicit IO is allowed. To access this attribute directly under
asyncio without any prior loading operations, the attribute can be accessed
as an awaitable by indicating the :attr:`_asyncio.AsyncAttrs.awaitable_attrs`
prefix::

a1 = (await session.scalars(select(A))).one()
for b1 in await a1.awaitable_attrs.bs:
    print(b1)

The :class:`_asyncio.AsyncAttrs` mixin provides a succinct facade over the
internal approach that's also used by the
:meth:`_asyncio.AsyncSession.run_sync` method.

.. versionadded:: 2.0.13

.. seealso::

  :class:`_asyncio.AsyncAttrs`
```

- Collections can be replaced with **write only collections** that will never
emit IO implicitly, by using the `write_only_relationship` feature in SQLAlchemy 2.0. Using this feature, collections are never read from, only queried using explicit SQL calls.  See the example `async_orm_writeonly.py` in the `examples_asyncio` section for an example of write-only collections used with asyncio.

When using write only collections, the program's behavior is simple and easy to predict regarding collections. However, the downside is that there is not any built-in system for loading many of these collections all at once, which instead would need to be performed manually.  Therefore, many of the bullets below address specific techniques when using traditional lazy-loaded relationships with asyncio, which requires more care.

- If not using `_asyncio.AsyncAttrs`, relationships can be declared
with `lazy="raise"` so that by default they will not attempt to emit SQL. In order to load collections, `eager loading` would be used instead.

- The most useful eager loading strategy is the
`_orm.selectinload` eager loader, which is employed in the previous example in order to eagerly load the `A.bs` collection within the scope of the `await session.execute()` call:

```
  stmt = select(A).options(selectinload(A.bs))
```

- When constructing new objects, **collections are always assigned a default,
empty collection**, such as a list in the above example:

```
  A(bs=[], data="a2")

This allows the ``.bs`` collection on the above ``A`` object to be present and
readable when the ``A`` object is flushed; otherwise, when the ``A`` is
flushed, ``.bs`` would be unloaded and would raise an error on access.
```

- The `_asyncio.AsyncSession` is configured using
`_orm.Session.expire_on_commit set to False, so that we may access attributes on an object subsequent to a call to asyncio.AsyncSession.commit`, as in the line at the end where we access an attribute:

```
  # create AsyncSession with expire_on_commit=False
  async_session = AsyncSession(engine, expire_on_commit=False)

  # sessionmaker version
  async_session = async_sessionmaker(engine, expire_on_commit=False)

  async with async_session() as session:
      result = await session.execute(select(A).order_by(A.id))

      a1 = result.scalars().first()

      # commit would normally expire all attributes
      await session.commit()

      # access attribute subsequent to commit; this is what
      # expire_on_commit=False allows
      print(a1.data)
```

Other guidelines include:

- Methods like `_asyncio.AsyncSession.expire` should be avoided in favor of
`_asyncio.AsyncSession.refresh; **if** expiration is absolutely needed. Expiration should generally **not** be needed as orm.Session.expire_on_commit` should normally be set to `False` when using asyncio.

- A lazy-loaded relationship **can be loaded explicitly under asyncio** using
`_asyncio.AsyncSession.refresh, **if** the desired attribute name is passed explicitly to orm.Session.refresh.attribute_names`, e.g.:

```
# assume a_obj is an A that has lazy loaded A.bs collection
a_obj = await async_session.get(A, [1])

# force the collection to load by naming it in attribute_names
await async_session.refresh(a_obj, ["bs"])

# collection is present
print(f"bs collection: {a_obj.bs}")

It's of course preferable to use eager loading up front in order to have
collections already set up without the need to lazy-load.

.. versionadded:: 2.0.4 Added support for
 :meth:`_asyncio.AsyncSession.refresh` and the underlying
 :meth:`_orm.Session.refresh` method to force lazy-loaded relationships
 to load, if they are named explicitly in the
 :paramref:`_orm.Session.refresh.attribute_names` parameter.
 In previous versions, the relationship would be silently skipped even
 if named in the parameter.
```

- Avoid using the `all` cascade option documented at `unitofwork_cascades`
in favor of listing out the desired cascade features explicitly.   The `all` cascade option implies among others the `cascade_refresh_expire` setting, which means that the `.AsyncSession.refresh method will expire the attributes on related objects, but not necessarily refresh those related objects assuming eager loading is not configured within the orm.relationship`, leaving them in an expired state.

- Appropriate loader options should be employed for `_orm.deferred`
columns, if used at all, in addition to that of `_orm.relationship` constructs as noted above.  See `orm_queryguide_column_deferral` for background on deferred column loading.

- The "dynamic" relationship loader strategy described at
`dynamic_relationship is not compatible by default with the asyncio approach. It can be used directly only if invoked within the asyncio.AsyncSession.run_sync` method described at `session_run_sync`, or by using its `.statement` attribute to obtain a normal select:

```
  user = await session.get(User, 42)
  addresses = (await session.scalars(user.addresses.statement)).all()
  stmt = user.addresses.statement.where(Address.email_address.startswith("patrick"))
  addresses_filter = (await session.scalars(stmt)).all()

The :ref:`write only <write_only_relationship>` technique, introduced in
version 2.0 of SQLAlchemy, is fully compatible with asyncio and should be
preferred.

.. seealso::

:ref:`migration_20_dynamic_loaders` - notes on migration to 2.0 style
```

- If using asyncio with a database that does not support RETURNING, such as
MySQL 8, server default values such as generated timestamps will not be available on newly flushed objects unless the `_orm.Mapper.eager_defaults` option is used. In SQLAlchemy 2.0, this behavior is applied automatically to backends like PostgreSQL, SQLite and MariaDB which use RETURNING to fetch new values when rows are INSERTed.

### Running Synchronous Methods and Functions under asyncio

As an alternative means of integrating traditional SQLAlchemy "lazy loading" within an asyncio event loop, an **optional** method known as `_asyncio.AsyncSession.run_sync` is provided which will run any Python function inside of a greenlet, where traditional synchronous programming concepts will be translated to use `await when they reach the database driver.   A hypothetical approach here is an asyncio-oriented application can package up database-related methods into functions that are invoked using asyncio.AsyncSession.run_sync`.

Altering the above example, if we didn't use `_orm.selectinload` for the `A.bs` collection, we could accomplish our treatment of these attribute accesses within a separate function:

```
import asyncio

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

def fetch_and_update_objects(session):
    """run traditional sync-style ORM code in a function that will be
    invoked within an awaitable.

    """

    # the session object here is a traditional ORM Session.
    # all features are available here including legacy Query use.

    stmt = select(A)

    result = session.execute(stmt)
    for a1 in result.scalars():
        print(a1)

        # lazy loads
        for b1 in a1.bs:
            print(b1)

    # legacy Query use
    a1 = session.query(A).order_by(A.id).first()

    a1.data = "new data"

async def async_main():
    engine = create_async_engine(
        "postgresql+asyncpg://scott:tiger@localhost/test",
        echo=True,
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with AsyncSession(engine) as session:
        async with session.begin():
            session.add_all(
                [
                    A(bs=[B(), B()], data="a1"),
                    A(bs=[B()], data="a2"),
                    A(bs=[B(), B()], data="a3"),
                ]
            )

        await session.run_sync(fetch_and_update_objects)

        await session.commit()

    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()

asyncio.run(async_main())
```

The above approach of running certain functions within a "sync" runner has some parallels to an application that runs a SQLAlchemy application on top of an event-based programming library such as `gevent`.  The differences are as follows:

1. unlike when using `gevent`, we can continue to use the standard Python
asyncio event loop, or any custom event loop, without the need to integrate into the `gevent` event loop.

2. There is no "monkeypatching" whatsoever.   The above example makes use of
a real asyncio driver and the underlying SQLAlchemy connection pool is also using the Python built-in `asyncio.Queue` for pooling connections.

3. The program can freely switch between async/await code and contained
functions that use sync code with virtually no performance penalty.  There is no "thread executor" or any additional waiters or synchronization in use.

4. The underlying network drivers are also using pure Python asyncio
concepts, no third party networking libraries as `gevent` and `eventlet` provides are in use.

## Using events with the asyncio extension

The SQLAlchemy `event system <event_toplevel>` is not directly exposed by the asyncio extension, meaning there is not yet an "async" version of a SQLAlchemy event handler.

However, as the asyncio extension surrounds the usual synchronous SQLAlchemy API, regular "synchronous" style event handlers are freely available as they would be if asyncio were not used.

As detailed below, there are two current strategies to register events given asyncio-facing APIs:

- Events can be registered at the instance level (e.g. a specific
`_asyncio.AsyncEngine` instance) by associating the event with the `sync attribute that refers to the proxied object. For example to register the events.PoolEvents.connect event against an asyncio.AsyncEngine instance, use its asyncio.AsyncEngine.sync_engine` attribute as target. Targets include:

`_asyncio.AsyncEngine.sync_engine`

`_asyncio.AsyncConnection.sync_connection`

`_asyncio.AsyncConnection.sync_engine`

`_asyncio.AsyncSession.sync_session`

- To register an event at the class level, targeting all instances of the same type (e.g.
all `_asyncio.AsyncSession instances), use the corresponding sync-style class. For example to register the ormevents.SessionEvents.before_commit event against the asyncio.AsyncSession class, use the orm.Session` class as the target.

- To register at the `_orm.sessionmaker` level, combine an explicit
`_orm.sessionmaker with an asyncio.async_sessionmaker using asyncio.async_sessionmaker.sync_session_class, and associate events with the orm.sessionmaker`.

When working within an event handler that is within an asyncio context, objects like the `_engine.Connection` continue to work in their usual "synchronous" way without requiring `await` or `async usage; when messages are ultimately received by the asyncio database adapter, the calling style is transparently adapted back into the asyncio calling style.  For events that are passed a DBAPI level connection, such as events.PoolEvents.connect`, the object is a `pep-249` compliant "connection" object which will adapt sync-style calls into the asyncio driver.

### Examples of Event Listeners with Async Engines / Sessions / Sessionmakers

Some examples of sync style event handlers associated with async-facing API constructs are illustrated below:

- **Core Events on AsyncEngine**
In this example, we access the `_asyncio.AsyncEngine.sync_engine attribute of asyncio.AsyncEngine` as the target for `.ConnectionEvents` and `.PoolEvents`:

```
import asyncio

from sqlalchemy import event
from sqlalchemy import text
from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine("postgresql+asyncpg://scott:tiger@localhost:5432/test")

# connect event on instance of Engine
@event.listens_for(engine.sync_engine, "connect")
def my_on_connect(dbapi_con, connection_record):
    print("New DBAPI connection:", dbapi_con)
    cursor = dbapi_con.cursor()

    # sync style API use for adapted DBAPI connection / cursor
    cursor.execute("select 'execute from event'")
    print(cursor.fetchone()[0])

# before_execute event on all Engine instances
@event.listens_for(Engine, "before_execute")
def my_before_execute(
    conn,
    clauseelement,
    multiparams,
    params,
    execution_options,
):
    print("before execute!")

async def go():
    async with engine.connect() as conn:
        await conn.execute(text("select 1"))
    await engine.dispose()

asyncio.run(go())

Output:

.. sourcecode:: text

New DBAPI connection: <AdaptedConnection <asyncpg.connection.Connection object at 0x7f33f9b16960>>
execute from event
before execute!
```

- **ORM Events on AsyncSession**
In this example, we access `_asyncio.AsyncSession.sync_session as the target for orm.SessionEvents`:

```
import asyncio

from sqlalchemy import event
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import Session

engine = create_async_engine("postgresql+asyncpg://scott:tiger@localhost:5432/test")

session = AsyncSession(engine)

# before_commit event on instance of Session
@event.listens_for(session.sync_session, "before_commit")
def my_before_commit(session):
    print("before commit!")

    # sync style API use on Session
    connection = session.connection()

    # sync style API use on Connection
    result = connection.execute(text("select 'execute from event'"))
    print(result.first())

# after_commit event on all Session instances
@event.listens_for(Session, "after_commit")
def my_after_commit(session):
    print("after commit!")

async def go():
    await session.execute(text("select 1"))
    await session.commit()

    await session.close()
    await engine.dispose()

asyncio.run(go())

Output:

.. sourcecode:: text

before commit!
execute from event
after commit!
```

- **ORM Events on async_sessionmaker**
For this use case, we make a `_orm.sessionmaker as the event target, then assign it to the asyncio.async_sessionmaker using the asyncio.async_sessionmaker.sync_session_class` parameter:

```
import asyncio

from sqlalchemy import event
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import sessionmaker

sync_maker = sessionmaker()
maker = async_sessionmaker(sync_session_class=sync_maker)

@event.listens_for(sync_maker, "before_commit")
def before_commit(session):
    print("before commit")

async def main():
    async_session = maker()

    await async_session.commit()

asyncio.run(main())

Output:

.. sourcecode:: text

before commit
```

### Using awaitable-only driver methods in connection pool and other events

As discussed in the above section, event handlers such as those oriented around the `.PoolEvents` event handlers receive a sync-style "DBAPI" connection, which is a wrapper object supplied by SQLAlchemy asyncio dialects to adapt the underlying asyncio "driver" connection into one that can be used by SQLAlchemy's internals.    A special use case arises when the user-defined implementation for such an event handler needs to make use of the ultimate "driver" connection directly, using awaitable only methods on that driver connection.  One such example is the `.set_type_codec()` method supplied by the asyncpg driver.

To accommodate this use case, SQLAlchemy's `.AdaptedConnection` class provides a method `.AdaptedConnection.run_async that allows an awaitable function to be invoked within the "synchronous" context of an event handler or other SQLAlchemy internal.  This method is directly analogous to the asyncio.AsyncConnection.run_sync` method that allows a sync-style method to run under async.

`.AdaptedConnection.run_async` should be passed a function that will accept the innermost "driver" connection as a single argument, and return an awaitable that will be invoked by the `.AdaptedConnection.run_async` method.  The given function itself does not need to be declared as `async`; it's perfectly fine for it to be a Python `lambda:`, as the return awaitable value will be invoked after being returned:

```
from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine(...)

@event.listens_for(engine.sync_engine, "connect")
def register_custom_types(dbapi_connection, *args):
    dbapi_connection.run_async(
        lambda connection: connection.set_type_codec(
            "MyCustomType",
            encoder,
            decoder,  # ...
        )
    )
```

Above, the object passed to the `register_custom_types` event handler is an instance of `.AdaptedConnection`, which provides a DBAPI-like interface to an underlying async-only driver-level connection object. The `.AdaptedConnection.run_async` method then provides access to an awaitable environment where the underlying driver level connection may be acted upon.

.. versionadded:: 1.4.30

## Using multiple asyncio event loops

An application that makes use of multiple event loops, for example in the uncommon case of combining asyncio with multithreading, should not share the same `_asyncio.AsyncEngine` with different event loops when using the default pool implementation.

If an `_asyncio.AsyncEngine is be passed from one event loop to another, the method asyncio.AsyncEngine.dispose()` should be called before it's reused on a new event loop. Failing to do so may lead to a `RuntimeError` along the lines of `Task <Task pending ...> got Future attached to a different loop`

If the same engine must be shared between different loop, it should be configured to disable pooling using `sqlalchemy.pool.NullPool`, preventing the Engine from using any connection more than once:

```
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.pool import NullPool

engine = create_async_engine(
    "postgresql+asyncpg://user:pass@host/dbname",
    poolclass=NullPool,
)
```

## Using asyncio scoped session

The "scoped session" pattern used in threaded SQLAlchemy with the `.scoped_session object is also available in asyncio, using an adapted version called asyncio.async_scoped_session`.

> **Tip:** for new development as it relies upon mutable global state that must also be
explicitly torn down when work within the thread or task is complete.
Particularly when using asyncio, it's likely a better idea to pass the
`_asyncio.AsyncSession` directly to the awaitable functions that need
it.

When using `_asyncio.async_scoped_session`, as there's no "thread-local" concept in the asyncio context, the "scopefunc" parameter must be provided to the constructor. The example below illustrates using the `asyncio.current_task()` function for this purpose:

```
from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    async_scoped_session,
    async_sessionmaker,
)

async_session_factory = async_sessionmaker(
    some_async_engine,
    expire_on_commit=False,
)
AsyncScopedSession = async_scoped_session(
    async_session_factory,
    scopefunc=current_task,
)
some_async_session = AsyncScopedSession()
```

> **Warning:** is invoked **an arbitrary number of times** within a task, once for each
time the underlying `_asyncio.AsyncSession` is accessed. The function
should therefore be **idempotent** and lightweight, and should not attempt
to create or mutate any state, such as establishing callbacks, etc.

> **Warning:** the `_asyncio.async_scoped_session.remove` method is called from
within the outermost awaitable, to ensure the key is removed from the
registry when the task is complete, otherwise the task handle as well as
the `_asyncio.AsyncSession` will remain in memory, essentially
creating a memory leak.  See the following example which illustrates
the correct use of `_asyncio.async_scoped_session.remove`.

`_asyncio.async_scoped_session` includes **proxy behavior** similar to that of `.scoped_session, which means it can be treated as a asyncio.AsyncSession` directly, keeping in mind that the usual `await keywords are necessary, including for the asyncio.async_scoped_session.remove` method:

```
async def some_function(some_async_session, some_object):
    # use the AsyncSession directly
    some_async_session.add(some_object)

    # use the AsyncSession via the context-local proxy
    await AsyncScopedSession.commit()

    # "remove" the current proxied AsyncSession for the local context
    await AsyncScopedSession.remove()
```

.. versionadded:: 1.4.19

## Using the Inspector to inspect schema objects

SQLAlchemy does not yet offer an asyncio version of the `_reflection.Inspector` (introduced at `metadata_reflection_inspector), however the existing interface may be used in an asyncio context by leveraging the asyncio.AsyncConnection.run_sync method of asyncio.AsyncConnection`:

```
import asyncio

from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import create_async_engine

engine = create_async_engine("postgresql+asyncpg://scott:tiger@localhost/test")

def use_inspector(conn):
    inspector = inspect(conn)
    # use the inspector
    print(inspector.get_view_names())
    # return any value to the caller
    return inspector.get_table_names()

async def async_main():
    async with engine.connect() as conn:
        tables = await conn.run_sync(use_inspector)

asyncio.run(async_main())
```

> **Seealso:**  `metadata_reflection`
 `inspection_toplevel`

## Engine API Documentation

## Result Set API Documentation

The `_asyncio.AsyncResult object is an async-adapted version of the result.Result object.  It is only returned when using the asyncio.AsyncConnection.stream or asyncio.AsyncSession.stream` methods, which return a result object that is on top of an active database cursor.

## ORM Session API Documentation
