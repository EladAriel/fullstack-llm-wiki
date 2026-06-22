---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/queryguide/index.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
generated_filename: "_source_index.md"
---

==================

# ORM Querying Guide

This section provides an overview of emitting queries with the SQLAlchemy ORM using `2.0 style` usage.

Readers of this section should be familiar with the SQLAlchemy overview at `unified_tutorial`, and in particular most of the content here expands upon the content at `tutorial_selecting_data`.

> **Admonition:**  In the SQLAlchemy 2.x series, SQL SELECT statements for the ORM are
 constructed using the same `_sql.select` construct as is used in
 Core, which is then invoked in terms of a `_orm.Session` using the
 `_orm.Session.execute method (as are the sql.update` and
 `_sql.delete` constructs now used for the
 `orm_expression_update_delete` feature). However, the legacy
 `_query.Query` object, which performs these same steps as more of an
 "all-in-one" object, continues to remain available as a thin facade over
 this new system, to support applications that were built on the 1.x series
 without the need for wholesale replacement of all queries. For reference on
 this object, see the section `query_api_toplevel`.

## Contents

- select
- inheritance
- dml
- columns
- relationships
- api
- query
