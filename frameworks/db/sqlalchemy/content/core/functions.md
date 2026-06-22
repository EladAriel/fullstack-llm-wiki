---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/functions.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

=========================

# SQL and Generic Functions

SQL functions are invoked by using the `_sql.func` namespace. See the tutorial at `tutorial_functions for background on how to use the sql.func` object to render SQL functions in statements.

> **Seealso:**  `tutorial_functions` - in the `unified_tutorial`

## Function API

The base API for SQL functions, which provides for the `_sql.func` namespace as well as classes that may be used for extensibility.

## Selected "Known" Functions

These are `.GenericFunction implementations for a selected set of common SQL functions that set up the expected return type for each function automatically.  The are invoked in the same way as any other member of the sql.func` namespace:

```
select(func.count("*")).select_from(some_table)
```

Note that any name not known to `_sql.func` generates the function name as is - there is no restriction on what SQL functions can be called, known or unknown to SQLAlchemy, built-in or user defined. The section here only describes those functions where SQLAlchemy already knows what argument and return types are in use.
