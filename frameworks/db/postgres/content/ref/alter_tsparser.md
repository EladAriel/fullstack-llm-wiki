---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_tsparser.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

ALTER TEXT SEARCH PARSER

ALTER TEXT SEARCH PARSER
7
SQL - Language Statements

ALTER TEXT SEARCH PARSER
change the definition of a text search parser

```
ALTER TEXT SEARCH PARSER name RENAME TO new_name
ALTER TEXT SEARCH PARSER name SET SCHEMA new_schema
```

## Description

`ALTER TEXT SEARCH PARSER` changes the definition of a text search parser. Currently, the only supported functionality is to change the parser's name.

You must be a superuser to use `ALTER TEXT SEARCH PARSER`.

## Parameters

- The name (optionally schema-qualified) of an existing text search parser.
- The new name of the text search parser.
- The new schema for the text search parser.

## Compatibility

There is no `ALTER TEXT SEARCH PARSER` statement in the SQL standard.

## See Also
