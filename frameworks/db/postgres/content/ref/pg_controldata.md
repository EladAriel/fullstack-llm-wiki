---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/pg_controldata.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

pg_controldata

`pg_controldata`
1
Application

pg_controldata
display control information of a PostgreSQL database cluster

`pg_controldata`
`option`

`-D`
`--pgdata`

`datadir`

## Description

`pg_controldata` prints information initialized during `initdb`, such as the catalog version. It also shows information about write-ahead logging and checkpoint processing. This information is cluster-wide, and not specific to any one database.

This utility can only be run by the user who initialized the cluster because it requires read access to the data directory. You can specify the data directory on the command line, or use the environment variable `PGDATA`.

## Options

- Specifies the directory where the database cluster is stored. - Print the `pg_controldata` version and exit. - Show help about `pg_controldata` command line arguments, and exit.

## Environment

- Default data directory location
- Specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.
