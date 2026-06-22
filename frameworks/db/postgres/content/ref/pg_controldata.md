---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/pg_controldata.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
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
