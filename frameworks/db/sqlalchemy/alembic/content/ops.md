---
type: "Framework Learn Page"
framework: "sqlalchemy/alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/ops.rst"
source_commit: "96fb84812ed7fe3ba1a8d6fd7e8cd1ba9a3c4b37"
source_commit_short: "96fb8481"
source_commit_date: "2026-05-31T12:51:03-04:00"
generated_at: "2026-06-21T11:33:13Z"
---

===================

# Operation Reference

This file provides documentation on Alembic migration directives.

The directives here are used within user-defined migration files, within the `upgrade()` and `downgrade()` functions, as well as any functions further invoked by those.

All directives exist as methods on a class called `.Operations`. When migration scripts are run, this object is made available to the script via the `alembic.op` datamember, which is a proxy to an actual instance of `.Operations`. Currently, `alembic.op` is a real Python module, populated with individual proxies for each method on `.Operations`, so symbols can be imported safely from the `alembic.op` namespace.

The `.Operations` system is also fully extensible.  See `operation_plugins` for details on this.

A key design philosophy to the `alembic.operations.toplevel` methods is that to the greatest degree possible, they internally generate the appropriate SQLAlchemy metadata, typically involving `sqlalchemy.schema.Table` and `sqlalchemy.schema.Constraint` objects.  This so that migration instructions can be given in terms of just the string names and/or flags involved. The exceptions to this rule include the `.Operations.add_column` and `.Operations.create_table` directives, which require full `sqlalchemy.schema.Column` objects, though the table metadata is still generated here.

The functions here all require that a `.MigrationContext` has been configured within the `env.py` script first, which is typically via `.EnvironmentContext.configure`.   Under normal circumstances they are called from an actual migration script, which itself would be invoked by the `.EnvironmentContext.run_migrations` method.
