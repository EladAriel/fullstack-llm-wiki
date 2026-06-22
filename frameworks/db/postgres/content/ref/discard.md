---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/discard.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DISCARD

DISCARD
7
SQL - Language Statements

DISCARD
discard session state

```
DISCARD { ALL | PLANS | SEQUENCES | TEMPORARY | TEMP }
```

## Description

`DISCARD` releases internal resources associated with a database session. This command is useful for partially or fully resetting the session's state. There are several subcommands to release different types of resources; the `DISCARD ALL` variant subsumes all the others, and also resets additional state.

## Parameters

- Releases all cached query plans, forcing re-planning to occur the next time the associated prepared statement is used.
- Discards all cached sequence-related state, including `currval()`/`lastval()` information and any preallocated sequence values that have not yet been returned by `nextval()`. (See `sql-createsequence` for a description of preallocated sequence values.)
- Drops all temporary tables created in the current session.
- Releases all temporary resources associated with the current session and resets the session to its initial state. Currently, this has the same effect as executing the following sequence of statements:

```
CLOSE ALL;
SET SESSION AUTHORIZATION DEFAULT;
RESET ALL;
DEALLOCATE ALL;
UNLISTEN *;
SELECT pg_advisory_unlock_all();
DISCARD PLANS;
DISCARD TEMP;
DISCARD SEQUENCES;
```

## Notes

`DISCARD ALL` cannot be executed inside a transaction block.

## Compatibility

`DISCARD` is a PostgreSQL extension.
