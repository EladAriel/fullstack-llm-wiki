---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/deallocate.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DEALLOCATE

prepared statements
removing

DEALLOCATE
7
SQL - Language Statements

DEALLOCATE
deallocate a prepared statement

```
DEALLOCATE [ PREPARE ] { name | ALL }
```

## Description

`DEALLOCATE` is used to deallocate a previously prepared SQL statement. If you do not explicitly deallocate a prepared statement, it is deallocated when the session ends.

For more information on prepared statements, see `sql-prepare`.

## Parameters

- This key word is ignored.
- The name of the prepared statement to deallocate.
- Deallocate all prepared statements.

## Compatibility

The SQL standard includes a `DEALLOCATE` statement, but it is only for use in embedded SQL.

## See Also
