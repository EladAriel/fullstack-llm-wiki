---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/appendix-obsolete-refint.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

## refint Extension Removed

refint

PostgreSQL 19 and below shipped an extension named `refint` (part of the `spi` contrib module) that provided the trigger functions `check_primary_key` and `check_foreign_key` as an early way to enforce referential integrity. This functionality was long superseded by the built-in foreign key mechanism (see `ddl-constraints-fk`), and the extension was removed in PostgreSQL 20.
