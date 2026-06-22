---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/tutorial/data.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

.. include:: tutorial_nav_include.rst

# Working with Data

In `tutorial_working_with_transactions`, we learned the basics of how to interact with the Python DBAPI and its transactional state.  Then, in `tutorial_working_with_metadata, we learned how to represent database tables, columns, and constraints within SQLAlchemy using the schema.MetaData` and related objects.  In this section we will combine both concepts above to create, select and manipulate data within a relational database.   Our interaction with the database is **always** in terms of a transaction, even if we've set our database driver to use `autocommit <dbapi_autocommit>` behind the scenes.

The components of this section are as follows:

- `tutorial_core_insert` - to get some data into the database, we introduce
and demonstrate the Core `_sql.Insert` construct.   INSERTs from an ORM perspective are described in the next section `tutorial_orm_data_manipulation`.

- `tutorial_selecting_data` - this section will describe in detail
the `_sql.Select construct, which is the most commonly used object in SQLAlchemy.  The sql.Select` construct emits SELECT statements for both Core and ORM centric applications and both use cases will be described here.   Additional ORM use cases are also noted in the later section `tutorial_select_relationships` as well as the `queryguide_toplevel`.

- `tutorial_core_update_delete` - Rounding out the INSERT and SELECTion
of data, this section will describe from a Core perspective the use of the `_sql.Update and sql.Delete` constructs.  ORM-specific UPDATE and DELETE is similarly described in the `tutorial_orm_data_manipulation` section.

## Contents

- data_insert
- data_select
- data_update
