---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/appendix-obsolete-pgresetxlog.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## `pg_resetxlog` renamed to `pg_resetwal`

pg_resetxlog
pg_resetwal

PostgreSQL 9.6 and below provided a command named `pg_resetxlog` pg_resetxlog to reset the write-ahead-log (WAL) files. This command was renamed to `pg_resetwal`, see `app-pgresetwal` for documentation of `pg_resetwal` and see the release notes for PostgreSQL 10 for details on this change.
