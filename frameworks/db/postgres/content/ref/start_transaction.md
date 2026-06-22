---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/start_transaction.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

START TRANSACTION

START TRANSACTION
7
SQL - Language Statements

START TRANSACTION
start a transaction block

```
START TRANSACTION [ transaction_mode [, ...] ]

where transaction_mode is one of:

    ISOLATION LEVEL { SERIALIZABLE | REPEATABLE READ | READ COMMITTED | READ UNCOMMITTED }
    READ WRITE | READ ONLY
    [ NOT ] DEFERRABLE
```

## Description

This command begins a new transaction block. If the isolation level, read/write mode, or deferrable mode is specified, the new transaction has those characteristics, as if SET TRANSACTION was executed. This is the same as the BEGIN command.

## Parameters

Refer to `sql-set-transaction` for information on the meaning of the parameters to this statement.

## Compatibility

In the standard, it is not necessary to issue `START TRANSACTION` to start a transaction block: any SQL command implicitly begins a block. PostgreSQL's behavior can be seen as implicitly issuing a `COMMIT` after each command that does not follow `START TRANSACTION` (or `BEGIN`), and it is therefore often called autocommit. Other relational database systems might offer an autocommit feature as a convenience.

The `DEFERRABLE` `transaction_mode` is a PostgreSQL language extension.

The SQL standard requires commas between successive `transaction_modes`, but for historical reasons PostgreSQL allows the commas to be omitted.

See also the compatibility section of `sql-set-transaction`.

## See Also
