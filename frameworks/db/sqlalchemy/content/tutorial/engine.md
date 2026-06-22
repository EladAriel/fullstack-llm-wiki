---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/tutorial/engine.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

.. include:: tutorial_nav_include.rst

# Establishing Connectivity - the Engine

The start of any SQLAlchemy application is an object called the `_engine.Engine`.   This object acts as a central source of connections to a particular database, providing both a factory as well as a holding space called a `connection pool <pooling_toplevel>` for these database connections.   The engine is typically a global object created just once for a particular database server, and is configured using a URL string which will describe how it should connect to the database host or backend.

For this tutorial we will use an in-memory-only SQLite database. This is an easy way to test things without needing to have an actual pre-existing database set up.  The `_engine.Engine is created by using the sa.create_engine` function:

```pycon+sql
 >>> from sqlalchemy import create_engine
 >>> engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
```

The main argument to `_sa.create_engine` is a string URL, above passed as the string `"sqlite+pysqlite:///:memory:". This string indicates to the engine.Engine` three important facts:

1. What kind of database are we communicating with?   This is the `sqlite`
portion above, which links in SQLAlchemy to an object known as the `dialect`.

2. What `DBAPI` are we using?  The Python `DBAPI` is a third party
driver that SQLAlchemy uses to interact with a particular database.  In this case, we're using the name `pysqlite`, which in modern Python use is the [sqlite3](https://docs.python.org/library/sqlite3.html) standard library interface for SQLite. If omitted, SQLAlchemy will use a default `DBAPI` for the particular database selected.

3. How do we locate the database?   In this case, our URL includes the phrase
`/:memory:`, which is an indicator to the `sqlite3` module that we will be using an **in-memory-only** database.   This kind of database is perfect for experimenting as it does not require any server nor does it need to create new files.

We have also specified a parameter `_sa.create_engine.echo, which will instruct the engine.Engine` to log all of the SQL it emits to a Python logger that will write to standard out.   This flag is a shorthand way of setting up `Python logging more formally <dbengine_logging>` and is useful for experimentation in scripts.   Many of the SQL examples will include this SQL logging output beneath a `[SQL]` link that when clicked, will reveal the full SQL interaction.
