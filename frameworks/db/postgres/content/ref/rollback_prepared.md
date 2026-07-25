---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/rollback_prepared.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

ROLLBACK PREPARED

ROLLBACK PREPARED
7
SQL - Language Statements

ROLLBACK PREPARED
cancel a transaction that was earlier prepared for two-phase commit

```
ROLLBACK PREPARED transaction_id
```

## Description

`ROLLBACK PREPARED` rolls back a transaction that is in prepared state.

## Parameters

- The transaction identifier of the transaction that is to be rolled back.

## Notes

To roll back a prepared transaction, you must be either the same user that executed the transaction originally, or a superuser. But you do not have to be in the same session that executed the transaction.

This command cannot be executed inside a transaction block. The prepared transaction is rolled back immediately.

All currently available prepared transactions are listed in the pg_prepared_xacts system view.

## Examples

Roll back the transaction identified by the transaction identifier `foobar`:

```
ROLLBACK PREPARED 'foobar';
```

## Compatibility

`ROLLBACK PREPARED` is a PostgreSQL extension. It is intended for use by external transaction management systems, some of which are covered by standards (such as X/Open XA), but the SQL side of those systems is not standardized.

## See Also
