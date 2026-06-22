---
type: "Framework Learn Page"
framework: "sqlalchemy/alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/api/commands.rst"
source_commit: "96fb84812ed7fe3ba1a8d6fd7e8cd1ba9a3c4b37"
source_commit_short: "96fb8481"
source_commit_date: "2026-05-31T12:51:03-04:00"
generated_at: "2026-06-21T11:33:13Z"
---

=========

# Commands

> **Note:** as regards its command invocation system.
This section is only useful for developers who wish to extend the
capabilities of Alembic.  For documentation on using Alembic commands,
please see `/tutorial`.

Alembic commands are all represented by functions in the `alembic.command.toplevel` package.  They all accept the same style of usage, being sent the `.Config` object as the first argument.

Commands can be run programmatically, by first constructing a `.Config` object, as in:

```
from alembic.config import Config
from alembic import command
alembic_cfg = Config("/path/to/yourapp/alembic.ini")
command.upgrade(alembic_cfg, "head")
```

In many cases, and perhaps more often than not, an application will wish to call upon a series of Alembic commands and/or other features.  It is usually a good idea to link multiple commands along a single connection and transaction, if feasible.  This can be achieved using the `.Config.attributes` dictionary in order to share a connection:

```
with engine.begin() as connection:
    alembic_cfg.attributes['connection'] = connection
    command.upgrade(alembic_cfg, "head")
```

This recipe requires that `env.py` consumes this connection argument; see the example in `connection_sharing` for details.

To write small API functions that make direct use of database and script directory information, rather than just running one of the built-in commands, use the `.ScriptDirectory` and `.MigrationContext` classes directly.
