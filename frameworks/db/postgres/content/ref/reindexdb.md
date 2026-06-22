---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/reindexdb.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

reindexdb

`reindexdb`
1
Application

reindexdb
reindex a PostgreSQL database

`reindexdb`
`connection-option`
`option`

`-S`
`--schema`

`schema`

`-t`
`--table`

`table`

`-i`
`--index`

`index`

`-s`
`--system`

`dbname`
`-a`
`--all`

## Description

`reindexdb` is a utility for rebuilding indexes in a PostgreSQL database.

`reindexdb` is a wrapper around the SQL command REINDEX. There is no effective difference between reindexing databases via this utility and via other methods for accessing the server.

## Options

`reindexdb` accepts the following command-line arguments: - Reindex all databases. - Use the `CONCURRENTLY` option. See `sql-reindex`, where all the caveats of this option are explained in detail. - Specifies the name of the database to be reindexed, when `-a`/`--all` is not used. If this is not specified, the database name is read from the environment variable `PGDATABASE`. If that is not set, the user name specified for the connection is used. The `dbname` can be a connection string. If so, connection string parameters will override any conflicting command line options. - Echo the commands that `reindexdb` generates and sends to the server. - Recreate `index` only. Multiple indexes can be recreated by writing multiple `-i` switches. - Execute the reindex commands in parallel by running `njobs` commands simultaneously. This option may reduce the processing time but it also increases the load on the database server. `reindexdb` will open `njobs` connections to the database, so make sure your `guc-max-connections` setting is high enough to accommodate all connections. Note that this option is incompatible with the `--system` option. - Do not display progress messages. - Reindex database's system catalogs only. - Reindex `schema` only. Multiple schemas can be reindexed by writing multiple `-S` switches. - Reindex `table` only. Multiple tables can be reindexed by writing multiple `-t` switches. - Specifies the tablespace where indexes are rebuilt. (This name is processed as a double-quoted identifier.) - Print detailed information during processing. - Print the `reindexdb` version and exit. - Show help about `reindexdb` command line arguments, and exit.

`reindexdb` also accepts the following command-line arguments for connection parameters: - Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket. - Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections. - User name to connect as. - Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password. - Force `reindexdb` to prompt for a password before connecting to a database. This option is never essential, since `reindexdb` will automatically prompt for a password if the server demands password authentication. However, `reindexdb` will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing `-W` to avoid the extra connection attempt. - When the `-a`/`--all` is used, connect to this database to gather the list of databases to reindex. If not specified, the `postgres` database will be used, or if that does not exist, `template1` will be used. This can be a connection string. If so, connection string parameters will override any conflicting command line options. Also, connection string parameters other than the database name itself will be re-used when connecting to other databases.

## Environment

- Default connection parameters
- Specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

This utility, like most other PostgreSQL utilities, also uses the environment variables supported by `libpq` (see `libpq-envars`).

## Diagnostics

In case of difficulty, see `sql-reindex` and `app-psql` for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the `libpq` front-end library will apply.

## Examples

To reindex the database `test`:

```
$ reindexdb test
```

To reindex the table `foo` and the index `bar` in a database named `abcd`:

```
$ reindexdb --table=foo --index=bar abcd
```

## See Also
