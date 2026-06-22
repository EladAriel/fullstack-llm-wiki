---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/pg_isready.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

pg_isready

`pg_isready`
1
Application

pg_isready
check the connection status of a PostgreSQL server

`pg_isready`
`connection-option`
`option`

## Description

`pg_isready` is a utility for checking the connection status of a PostgreSQL database server. The exit status specifies the result of the connection check.

## Options

- Specifies the name of the database to connect to. The `dbname` can be a connection string. If so, connection string parameters will override any conflicting command line options.
- Specifies the host name of the machine on which the server is running. If the value begins with a slash, it is used as the directory for the Unix-domain socket.
- Specifies the TCP port or the local Unix-domain socket file extension on which the server is listening for connections. Defaults to the value of the `PGPORT` environment variable or, if not set, to the port specified at compile time, usually 5432.
- Do not display status message. This is useful when scripting.
- The maximum number of seconds to wait when attempting connection before returning that the server is not responding. Setting to 0 disables. The default is 3 seconds.
- Connect to the database as the user `username` instead of the default.
- Print the `pg_isready` version and exit.
- Show help about `pg_isready` command line arguments, and exit.

## Exit Status

`pg_isready` returns `0` to the shell if the server is accepting connections normally, `1` if the server is rejecting connections (for example during startup), `2` if there was no response to the connection attempt, and `3` if no attempt was made (for example due to invalid parameters).

## Environment

`pg_isready`, like most other PostgreSQL utilities, also uses the environment variables supported by `libpq` (see `libpq-envars`).

The environment variable `PG_COLOR` specifies whether to use color in diagnostic messages. Possible values are `always`, `auto` and `never`.

## Notes

It is not necessary to supply correct user name, password, or database name values to obtain the server status; however, if incorrect values are provided, the server will log a failed connection attempt.

## Examples

Standard Usage:

```
$ pg_isready
/tmp:5432 - accepting connections
$ echo $?
0
```

Running with connection parameters to a PostgreSQL cluster in startup:

```
$ pg_isready -h localhost -p 5433
localhost:5433 - rejecting connections
$ echo $?
1
```

Running with connection parameters to a non-responsive PostgreSQL cluster:

```
$ pg_isready -h someremotehost
someremotehost:5432 - no response
$ echo $?
2
```
