---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/dropdb.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

dropdb

`dropdb`
1
Application

dropdb
remove a PostgreSQL database

`dropdb`
`connection-option`
`option`
`dbname`

## Description

`dropdb` destroys an existing PostgreSQL database. The user who executes this command must be a database superuser or the owner of the database.

`dropdb` is a wrapper around the SQL command DROP DATABASE. There is no effective difference between dropping databases via this utility and via other methods for accessing the server.

## Options

`dropdb` accepts the following command-line arguments: - Specifies the name of the database to be removed. - Echo the commands that `dropdb` generates and sends to the server. - Attempt to terminate all existing connections to the target database before dropping it. See `sql-dropdatabase` for more information on this option. - Issues a verification prompt before doing anything destructive. - Print the `dropdb` version and exit. - Do not throw an error if the database does not exist. A notice is issued in this case. - Show help about `dropdb` command line arguments, and exit.

`dropdb` also accepts the following command-line arguments for connection parameters: - Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix domain socket. - Specifies the TCP port or local Unix domain socket file extension on which the server is listening for connections. - User name to connect as. - Never issue a password prompt. If the server requires password authentication and a password is not available by other means such as a `.pgpass` file, the connection attempt will fail. This option can be useful in batch jobs and scripts where no user is present to enter a password. - Force `dropdb` to prompt for a password before connecting to a database. This option is never essential, since `dropdb` will automatically prompt for a password if the server demands password authentication. However, `dropdb` will waste a connection attempt finding out that the server wants a password. In some cases it is worth typing `-W` to avoid the extra connection attempt. - Specifies the name of the database to connect to in order to drop the target database. If not specified, the `postgres` database will be used; if that does not exist (or is the database being dropped), `template1` will be used. This can be a connection string. If so, connection string parameters will override any conflicting command line options.

## Environment

- Default connection parameters
- Specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

This utility, like most other PostgreSQL utilities, also uses the environment variables supported by `libpq` (see `libpq-envars`).

## Diagnostics

In case of difficulty, see `sql-dropdatabase` and `app-psql` for discussions of potential problems and error messages. The database server must be running at the targeted host. Also, any default connection settings and environment variables used by the `libpq` front-end library will apply.

## Examples

To destroy the database `demo` on the default database server:

```
$ dropdb demo
```

To destroy the database `demo` using the server on host `eden`, port 5000, with verification and a peek at the underlying command:

```
$ dropdb -p 5000 -h eden -i -e demo
Database "demo" will be permanently deleted.
Are you sure? (y/n) y
DROP DATABASE demo;
```

## See Also
