---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/queryguide/query.rst"
source_commit: "aa1a5575358d3aa14953b04dced02f4763fed2e7"
source_commit_short: "aa1a5575"
source_commit_date: "2026-07-23T18:02:59Z"
generated_at: "2026-07-25T11:50:45Z"
---

================

# Legacy Query API

> **Admonition:**  This page contains the Python generated documentation for the
 `_query.Query` construct, which for many years was the sole SQL
 interface when working with the SQLAlchemy ORM.  As of version 2.0, an all
 new way of working is now the standard approach, where the same
 `_sql.select` construct that works for Core works just as well for the
 ORM, providing a consistent interface for building queries.
 For any application that is built on the SQLAlchemy ORM prior to the
 2.0 API, the `_query.Query` API will usually represents the vast
 majority of database access code within an application, and as such the
 majority of the `_query.Query` API is
 **not being removed from SQLAlchemy**.  The `_query.Query` object
 behind the scenes now translates itself into a 2.0 style `_sql.select`
 object when the `_query.Query` object is executed, so it now is
 just a very thin adapter API.
 For a guide to migrating an application based on `_query.Query`
 to 2.0 style, see `migration_20_query_usage`.
 For an introduction to writing SQL for ORM objects in the 2.0 style,
 start with the `unified_tutorial`.  Additional reference for 2.0 style
 querying is at `queryguide_toplevel`.

# The Query Object

`_query.Query` is produced in terms of a given `.Session`, using the `.Session.query` method:

```
q = session.query(SomeMappedClass)
```

Following is the full interface for the `_query.Query` object.

# ORM-Specific Query Constructs

This section has moved to `queryguide_additional`.
