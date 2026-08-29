---
type: "Framework Learn Page"
framework: "Alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/api/ddl.rst"
source_commit: "c116cbc0f39d9df2b4ce5f1871043a622ca8774f"
source_commit_short: "c116cbc"
source_commit_date: "2026-08-14T03:25:08-04:00"
generated_at: "2026-08-29T09:39:28.244465Z"
---
.. _alembic.ddl.toplevel:

# DDL Internals

These are some of the constructs used to generate migration
instructions.  The APIs here build off of the :class:`sqlalchemy.schema.DDLElement`
and :ref:`sqlalchemy.ext.compiler_toplevel` systems.

For programmatic usage of Alembic's migration directives, the easiest
route is to use the higher level functions given by :ref:`alembic.operations.toplevel`.

**automodule:** alembic.ddl
    :members:
    :undoc-members:

**automodule:** alembic.ddl.base
    :members:
    :undoc-members:

**automodule:** alembic.ddl.impl
    :members:
    :undoc-members:

# MySQL

**automodule:** alembic.ddl.mysql
    :members:
    :undoc-members:
    :show-inheritance:

# MS-SQL

**automodule:** alembic.ddl.mssql
    :members:
    :undoc-members:
    :show-inheritance:

# Postgresql

**automodule:** alembic.ddl.postgresql
    :members:
    :undoc-members:
    :show-inheritance:

# SQLite

**automodule:** alembic.ddl.sqlite
    :members:
    :undoc-members:
    :show-inheritance: