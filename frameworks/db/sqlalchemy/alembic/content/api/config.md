---
type: "Framework Learn Page"
framework: "sqlalchemy/alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/api/config.rst"
source_commit: "96fb84812ed7fe3ba1a8d6fd7e8cd1ba9a3c4b37"
source_commit_short: "96fb8481"
source_commit_date: "2026-05-31T12:51:03-04:00"
generated_at: "2026-06-21T11:33:13Z"
---

==============

# Configuration

> **Note:** regards internal configuration constructs.
This section is only useful for developers who wish to extend the
capabilities of Alembic.  For documentation on configuration of
an Alembic environment, please see `/tutorial`.

The `.Config` object represents the configuration passed to the Alembic environment.  From an API usage perspective, it is needed for the following use cases:

- to create a `.ScriptDirectory`, which allows you to work
with the actual script files in a migration environment

- to create an `.EnvironmentContext`, which allows you to
actually run the `env.py` module within the migration environment

- to programmatically run any of the commands in the `alembic.command.toplevel`
module.

The `.Config` is not needed for these cases:

- to instantiate a `.MigrationContext` directly - this object
only needs a SQLAlchemy connection or dialect name.

- to instantiate a `.Operations` object - this object only
needs a `.MigrationContext`.
