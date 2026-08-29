---
type: "Framework Learn Page"
framework: "Alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/api/config.rst"
source_commit: "c116cbc0f39d9df2b4ce5f1871043a622ca8774f"
source_commit_short: "c116cbc"
source_commit_date: "2026-08-14T03:25:08-04:00"
generated_at: "2026-08-29T09:39:28.246575Z"
---
.. _alembic.config.toplevel:

# Configuration

**note:** this section discusses the **internal API of Alembic** as
   regards internal configuration constructs.
   This section is only useful for developers who wish to extend the
   capabilities of Alembic.  For documentation on configuration of
   an Alembic environment, please see :doc:`/tutorial`.

The :class:`.Config` object represents the configuration
passed to the Alembic environment.  From an API usage perspective,
it is needed for the following use cases:

* to create a :class:`.ScriptDirectory`, which allows you to work
  with the actual script files in a migration environment
* to create an :class:`.EnvironmentContext`, which allows you to
  actually run the ``env.py`` module within the migration environment
* to programmatically run any of the commands in the :ref:`alembic.command.toplevel`
  module.

The :class:`.Config` is *not* needed for these cases:

* to instantiate a :class:`.MigrationContext` directly - this object
  only needs a SQLAlchemy connection or dialect name.
* to instantiate a :class:`.Operations` object - this object only
  needs a :class:`.MigrationContext`.

**automodule:** alembic.config
    :members: