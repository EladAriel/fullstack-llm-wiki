---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/vacuumlo.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

vacuumlo

`vacuumlo`
1
Application

vacuumlo
remove orphaned large objects from a PostgreSQL database

`vacuumlo`
`option`
`dbname`

## Description

`vacuumlo` is a simple utility program that will remove any orphaned large objects from a PostgreSQL database. An orphaned large object (LO) is considered to be any LO whose OID does not appear in any `oid` or `lo` data column of the database.

If you use this, you may also be interested in the `lo_manage` trigger in the `lo` module. `lo_manage` is useful to try to avoid creating orphaned LOs in the first place.

All databases named on the command line are processed.

## Options

`vacuumlo` accepts the following command-line arguments: - Remove no more than `limit` large objects per transaction (default 1000). Since the server acquires a lock per LO removed, removing too many LOs in one transaction risks exceeding `guc-max-locks-per-transaction`. Set the limit to zero if you want all removals done in a single transaction. - Don't remove anything, just show what would be done. - Write a lot of progress messages. - Print the `vacuumlo` version and exit. - Show help about `vacuumlo` command line arguments, and exit.

`vacuumlo` also accepts the following command-line arguments for connection parameters: - Database server's host. - Database server's port. - User name to connect as. - Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password. - Force `vacuumlo` to prompt for a password before connecting to a database. This option is never essential, since `vacuumlo` will automatically prompt for a password if the server demands password authentication. However, `vacuumlo` will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing `-W` to avoid the extra connection attempt.

## Environment

- Default connection parameters.

This utility, like most other PostgreSQL utilities, also uses the environment variables supported by `libpq` (see `libpq-envars`).

The environment variable `PG_COLOR` specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

## Notes

`vacuumlo` works by the following method: First, `vacuumlo` builds a temporary table which contains all of the OIDs of the large objects in the selected database. It then scans through all columns in the database that are of type `oid` or `lo`, and removes matching entries from the temporary table. (Note: Only types with these names are considered; in particular, domains over them are not considered.) The remaining entries in the temporary table identify orphaned LOs. These are removed.

## Author

Peter Mount peter@retep.org.uk
