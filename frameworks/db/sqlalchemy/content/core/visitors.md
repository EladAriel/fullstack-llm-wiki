---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/visitors.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.530578Z"
---
# Visitor and Traversal Utilities

The :mod:`sqlalchemy.sql.visitors` module consists of classes and functions
that serve the purpose of generically **traversing** a Core SQL expression
structure.   This is not unlike the Python ``ast`` module in that is presents
a system by which a program can operate upon each component of a SQL
expression.   Common purposes this serves are locating various kinds of
elements such as :class:`_schema.Table` or :class:`.BindParameter` objects,
as well as altering the state of the structure such as replacing certain FROM
clauses with others.

**note:** the :mod:`sqlalchemy.sql.visitors` module is an internal API and
   is not fully public.    It is subject to change and may additionally not
   function as expected for use patterns that aren't considered within
   SQLAlchemy's own internals.

The :mod:`sqlalchemy.sql.visitors` module is part of the **internals** of
SQLAlchemy and it is not usually used by calling application code.  It is
however used in certain edge cases such as when constructing caching routines
as well as when building out custom SQL expressions using the
:ref:`Custom SQL Constructs and Compilation Extension <sqlalchemy.ext.compiler_toplevel>`.

**automodule:** sqlalchemy.sql.visitors
   :members:
   :private-members:
