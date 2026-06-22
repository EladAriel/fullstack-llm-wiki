---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/visitors.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# Visitor and Traversal Utilities

The `sqlalchemy.sql.visitors` module consists of classes and functions that serve the purpose of generically **traversing** a Core SQL expression structure.   This is not unlike the Python `ast module in that is presents a system by which a program can operate upon each component of a SQL expression.   Common purposes this serves are locating various kinds of elements such as schema.Table` or `.BindParameter` objects, as well as altering the state of the structure such as replacing certain FROM clauses with others.

> **Note:** is not fully public.    It is subject to change and may additionally not
function as expected for use patterns that aren't considered within
SQLAlchemy's own internals.

The `sqlalchemy.sql.visitors` module is part of the **internals** of SQLAlchemy and it is not usually used by calling application code.  It is however used in certain edge cases such as when constructing caching routines as well as when building out custom SQL expressions using the `Custom SQL Constructs and Compilation Extension <sqlalchemy.ext.compiler_toplevel>`.
