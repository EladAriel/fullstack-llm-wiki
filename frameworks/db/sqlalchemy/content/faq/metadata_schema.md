---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/faq/metadata_schema.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

=================

# MetaData / Schema

# My program is hanging when I say `table.drop()` / `metadata.drop_all()`

This usually corresponds to two conditions: 1. using PostgreSQL, which is really strict about table locks, and 2. you have a connection still open which contains locks on the table and is distinct from the connection being used for the DROP statement.  Heres the most minimal version of the pattern:

```
connection = engine.connect()
result = connection.execute(mytable.select())

mytable.drop(engine)
```

Above, a connection pool connection is still checked out; furthermore, the result object above also maintains a link to this connection.  If "implicit execution" is used, the result will hold this connection opened until the result object is closed or all rows are exhausted.

The call to `mytable.drop(engine) attempts to emit DROP TABLE on a second connection procured from the engine.Engine` which will lock.

The solution is to close out all connections before emitting DROP TABLE:

```
connection = engine.connect()
result = connection.execute(mytable.select())

# fully read result sets
result.fetchall()

# close connections
connection.close()

# now locks are removed
mytable.drop(engine)
```

# Does SQLAlchemy support ALTER TABLE, CREATE VIEW, CREATE TRIGGER, Schema Upgrade Functionality?

General ALTER support isn't present in SQLAlchemy directly.  For special DDL on an ad-hoc basis, the `.DDL` and related constructs can be used. See `metadata_ddl_toplevel` for a discussion on this subject.

A more comprehensive option is to use schema migration tools, such as Alembic or SQLAlchemy-Migrate; see `schema_migrations` for discussion on this.

# How can I sort Table objects in order of their dependency?

This is available via the `_schema.MetaData.sorted_tables` function:

```
metadata_obj = MetaData()
# ... add Table objects to metadata
ti = metadata_obj.sorted_tables
for t in ti:
    print(t)
```

# How can I get the CREATE TABLE/ DROP TABLE output as a string?

Modern SQLAlchemy has clause constructs which represent DDL operations. These can be rendered to strings like any other SQL expression:

```
from sqlalchemy.schema import CreateTable

print(CreateTable(mytable))
```

To get the string specific to a certain engine:

```
print(CreateTable(mytable).compile(engine))
```

There's also a special form of `_engine.Engine` available via `.create_mock_engine` that allows one to dump an entire metadata creation sequence as a string, using this recipe:

```
from sqlalchemy import create_mock_engine

def dump(sql, *multiparams, **params):
    print(sql.compile(dialect=engine.dialect))

engine = create_mock_engine("postgresql+psycopg2://", dump)
metadata_obj.create_all(engine, checkfirst=False)
```

The [Alembic](https://alembic.sqlalchemy.org) tool also supports an "offline" SQL generation mode that renders database migrations as SQL scripts.

# How can I subclass Table/Column to provide certain behaviors/configurations?

`_schema.Table and schema.Column` are not good targets for direct subclassing. However, there are simple ways to get on-construction behaviors using creation functions, and behaviors related to the linkages between schema objects such as constraint conventions or naming conventions using attachment events. An example of many of these techniques can be seen at [Naming Conventions](https://www.sqlalchemy.org/trac/wiki/UsageRecipes/NamingConventions).
