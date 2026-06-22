---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/rollback.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

ROLLBACK

ROLLBACK
7
SQL - Language Statements

ROLLBACK
abort the current transaction

```
ROLLBACK [ WORK | TRANSACTION ] [ AND [ NO ] CHAIN ]
```

## Description

`ROLLBACK` rolls back the current transaction and causes all the updates made by the transaction to be discarded.

## Parameters

chained transactions

- Optional key words. They have no effect.
- If `AND CHAIN` is specified, a new (not aborted) transaction is immediately started with the same transaction characteristics (see `sql-set-transaction`) as the just finished one. Otherwise, no new transaction is started.

## Notes

Use COMMIT to successfully terminate a transaction.

Issuing `ROLLBACK` outside of a transaction block emits a warning and otherwise has no effect. `ROLLBACK AND CHAIN` outside of a transaction block is an error.

## Examples

To abort all changes:

```
ROLLBACK;
```

## Compatibility

The command `ROLLBACK` conforms to the SQL standard. The form `ROLLBACK TRANSACTION` is a PostgreSQL extension.

## See Also
