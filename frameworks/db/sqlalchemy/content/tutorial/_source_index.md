---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/tutorial/index.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
generated_filename: "_source_index.md"
---

============================

# SQLAlchemy Unified Tutorial

> **Admonition:**  The SQLAlchemy Unified Tutorial is integrated between the Core and ORM
 components of SQLAlchemy and serves as a unified introduction to SQLAlchemy
 as a whole. For users of SQLAlchemy within the 1.x series, in the
 `2.0 style` of working, the ORM uses Core-style querying with the
 `_sql.select` construct, and transactional semantics between Core
 connections and ORM sessions are equivalent. Take note of the blue border
 styles for each section, that will tell you how "ORM-ish" a particular
 topic is!
 Users who are already familiar with SQLAlchemy, and especially those
 looking to migrate existing applications to work under the SQLAlchemy 2.0
 series within the 1.4 transitional phase should check out the
 `migration_20_toplevel` document as well.
 For the newcomer, this document has a **lot** of detail, however by the
 end they will be considered an **Alchemist**.

SQLAlchemy is presented as two distinct APIs, one building on top of the other. These APIs are known as **Core** and **ORM**.

# Tutorial Overview

The tutorial will present both concepts in the natural order that they should be learned, first with a mostly-Core-centric approach and then spanning out into more ORM-centric concepts.

The major sections of this tutorial are as follows:

## Contents

- engine
- dbapi_transactions
- metadata
- data
- orm_data_manipulation
- orm_related_objects
- further_reading

- `tutorial_engine` - all SQLAlchemy applications start with an
`_engine.Engine` object; here's how to create one.

- `tutorial_working_with_transactions` - the usage API of the
`_engine.Engine and its related objects engine.Connection and result.Result are presented here. This content is Core-centric however ORM users will want to be familiar with at least the result.Result` object.

- `tutorial_working_with_metadata` - SQLAlchemy's SQL abstractions as well
as the ORM rely upon a system of defining database schema constructs as Python objects.   This section introduces how to do that from both a Core and an ORM perspective.

- `tutorial_working_with_data` - here we learn how to create, select,
update and delete data in the database.   The so-called `CRUD` operations here are given in terms of SQLAlchemy Core with links out towards their ORM counterparts.  The SELECT operation that is introduced in detail at `tutorial_selecting_data` applies equally well to Core and ORM.

- `tutorial_orm_data_manipulation` covers the persistence framework of the
ORM; basically the ORM-centric ways to insert, update and delete, as well as how to handle transactions.

- `tutorial_orm_related_objects` introduces the concept of the
`_orm.relationship` construct and provides a brief overview of how it's used, with links to deeper documentation.

- `tutorial_further_reading` lists a series of major top-level
documentation sections which fully document the concepts introduced in this tutorial.

## Version Check

This tutorial is written using a system called [doctest](https://docs.python.org/3/library/doctest.html). All of the code excerpts written with a `>>>` are actually run as part of SQLAlchemy's test suite, and the reader is invited to work with the code examples given in real time with their own Python interpreter.

If running the examples, it is advised that the reader performs a quick check to verify that we are on  **version 2.1** of SQLAlchemy:

```pycon+sql
 >>> import sqlalchemy
 >>> sqlalchemy.__version__  # doctest: +SKIP
 2.1.0
```
