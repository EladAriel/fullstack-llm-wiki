---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/appendix-obsolete-pgreceivexlog.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.405721Z"
---
# pg_receivexlog renamed to pg_receivewal

   
     pg_receivexlog
     pg_receivewal
   

   
    PostgreSQL 9.6 and below provided a command named
    pg_receivexlog
    pg_receivexlog
    to fetch write-ahead-log (WAL) files.  This command was renamed to pg_receivewal, see
     for documentation of pg_receivewal and see
    the release notes for PostgreSQL 10 for details
    on this change.
