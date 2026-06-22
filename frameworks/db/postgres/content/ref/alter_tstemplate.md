---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_tstemplate.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

ALTER TEXT SEARCH TEMPLATE

ALTER TEXT SEARCH TEMPLATE
7
SQL - Language Statements

ALTER TEXT SEARCH TEMPLATE
change the definition of a text search template

```
ALTER TEXT SEARCH TEMPLATE name RENAME TO new_name
ALTER TEXT SEARCH TEMPLATE name SET SCHEMA new_schema
```

## Description

`ALTER TEXT SEARCH TEMPLATE` changes the definition of a text search template. Currently, the only supported functionality is to change the template's name.

You must be a superuser to use `ALTER TEXT SEARCH TEMPLATE`.

## Parameters

- The name (optionally schema-qualified) of an existing text search template.
- The new name of the text search template.
- The new schema for the text search template.

## Compatibility

There is no `ALTER TEXT SEARCH TEMPLATE` statement in the SQL standard.

## See Also
