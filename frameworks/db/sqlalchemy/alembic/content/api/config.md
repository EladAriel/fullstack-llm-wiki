---
type: "Framework Learn Page"
framework: "sqlalchemy/alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/api/config.rst"
source_commit: "7b2af57eba318a712b7b4f79c7bc6b3669055636"
source_commit_short: "7b2af57e"
source_commit_date: "2026-07-16T13:04:26-04:00"
generated_at: "2026-07-25T11:47:25Z"
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
