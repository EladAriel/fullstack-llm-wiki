---
type: "Framework Learn Page"
framework: "sqlalchemy/alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/api/index.rst"
source_commit: "7b2af57eba318a712b7b4f79c7bc6b3669055636"
source_commit_short: "7b2af57e"
source_commit_date: "2026-07-16T13:04:26-04:00"
generated_at: "2026-07-25T11:47:25Z"
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
