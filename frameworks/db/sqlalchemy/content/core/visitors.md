---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/visitors.rst"
source_commit: "aa1a5575358d3aa14953b04dced02f4763fed2e7"
source_commit_short: "aa1a5575"
source_commit_date: "2026-07-23T18:02:59Z"
generated_at: "2026-07-25T11:50:45Z"
---

# Visitor and Traversal Utilities

The `sqlalchemy.sql.visitors` module consists of classes and functions that serve the purpose of generically **traversing** a Core SQL expression structure.   This is not unlike the Python `ast module in that is presents a system by which a program can operate upon each component of a SQL expression.   Common purposes this serves are locating various kinds of elements such as schema.Table` or `.BindParameter` objects, as well as altering the state of the structure such as replacing certain FROM clauses with others.

> **Note:** is not fully public.    It is subject to change and may additionally not
function as expected for use patterns that aren't considered within
SQLAlchemy's own internals.

The `sqlalchemy.sql.visitors` module is part of the **internals** of SQLAlchemy and it is not usually used by calling application code.  It is however used in certain edge cases such as when constructing caching routines as well as when building out custom SQL expressions using the `Custom SQL Constructs and Compilation Extension <sqlalchemy.ext.compiler_toplevel>`.
