---
type: "Framework Learn Page"
framework: "sqlalchemy/alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/api/runtime.rst"
source_commit: "96fb84812ed7fe3ba1a8d6fd7e8cd1ba9a3c4b37"
source_commit_short: "96fb8481"
source_commit_date: "2026-05-31T12:51:03-04:00"
generated_at: "2026-06-21T11:33:13Z"
---

=======================

# Runtime Objects

The "runtime" of Alembic involves the `.EnvironmentContext` and `.MigrationContext` objects.   These are the objects that are in play once the `env.py` script is loaded up by a command and a migration operation proceeds.

# The Environment Context

The `.EnvironmentContext` class provides most of the API used within an `env.py` script.  Within `env.py`, the instantiated `.EnvironmentContext` is made available via a special proxy module called `alembic.context`.   That is, you can import `alembic.context` like a regular Python module, and each name you call upon it is ultimately routed towards the current `.EnvironmentContext` in use.

In particular, the key method used within `env.py` is `.EnvironmentContext.configure`, which establishes all the details about how the database will be accessed.

# The Migration Context

The `.MigrationContext` handles the actual work to be performed against a database backend as migration operations proceed.  It is generally not exposed to the end-user, except when the `.EnvironmentContext.configure.on_version_apply` callback hook is used.
