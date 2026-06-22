---
type: "Framework Learn Page"
framework: "sqlalchemy/alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/api/index.rst"
source_commit: "96fb84812ed7fe3ba1a8d6fd7e8cd1ba9a3c4b37"
source_commit_short: "96fb8481"
source_commit_date: "2026-05-31T12:51:03-04:00"
generated_at: "2026-06-21T11:33:13Z"
generated_filename: "_source_index.md"
---

===========

# API Details

Alembic's internal API has many public integration points that can be used to extend Alembic's functionality as well as to reuse its functionality in new ways.   As the project has grown, more APIs are created and exposed for this purpose.

Direct use of the vast majority of API details discussed here is not needed for rudimentary use of Alembic; the only API that is used normally by end users is the methods provided by the `.Operations` class, which is discussed outside of this subsection, and the parameters that can be passed to the `.EnvironmentContext.configure` method, used when configuring one's `env.py` environment.  However, real-world applications will usually end up using more of the internal API, in particular being able to run commands programmatically, as discussed in the section `/api/commands`.

## Contents

- overview
- runtime
- config
- commands
- operations
- autogenerate
- script
- ddl
- plugins
- exceptions
