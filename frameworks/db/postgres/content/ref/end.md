---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/end.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

END

END
7
SQL - Language Statements

END
commit the current transaction

```
END [ WORK | TRANSACTION ] [ AND [ NO ] CHAIN ]
```

## Description

`END` commits the current transaction. All changes made by the transaction become visible to others and are guaranteed to be durable if a crash occurs. This command is a PostgreSQL extension that is equivalent to COMMIT.

## Parameters

- Optional key words. They have no effect.
- If `AND CHAIN` is specified, a new transaction is immediately started with the same transaction characteristics (see `sql-set-transaction`) as the just finished one. Otherwise, no new transaction is started.

## Notes

Use ROLLBACK to abort a transaction.

Issuing `END` when not inside a transaction does no harm, but it will provoke a warning message.

## Examples

To commit the current transaction and make all changes permanent:

```
END;
```

## Compatibility

`END` is a PostgreSQL extension that provides functionality equivalent to COMMIT, which is specified in the SQL standard.

## See Also
