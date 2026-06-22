---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/show.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

SHOW

SHOW
7
SQL - Language Statements

SHOW
show the value of a run-time parameter

```
SHOW name
SHOW ALL
```

## Description

`SHOW` will display the current setting of run-time parameters. These variables can be set using the `SET` statement, by editing the `postgresql.conf` configuration file, through the `PGOPTIONS` environmental variable (when using `libpq` or a `libpq`-based application), or through command-line flags when starting the `postgres` server. See `runtime-config` for details.

## Parameters

- The name of a run-time parameter. Available parameters are documented in `runtime-config` and on the `sql-set` reference page. In addition, there are a few parameters that can be shown but not set: `SERVER_VERSION` Shows the server's version number.
- Shows the server-side character set encoding. At present, this parameter can be shown but not set, because the encoding is determined at database creation time.
- True if the current role has superuser privileges.

`ALL`

Show the values of all configuration parameters, with descriptions.

## Notes

The function `current_setting` produces equivalent output; see `functions-admin-set`. Also, the pg_settings system view produces the same information.

## Examples

Show the current setting of the parameter `DateStyle`:

```
SHOW DateStyle;
 DateStyle
-----------
 ISO, MDY
(1 row)
```

Show the current setting of the parameter `geqo`:

```
SHOW geqo;
 geqo
------
 on
(1 row)
```

Show all settings:

```
SHOW ALL;
            name         | setting |                description
-------------------------+---------+-------------------------------------------------
 allow_system_table_mods | off     | Allows modifications of the structure of ...
    .
    .
    .
 xmloption               | content | Sets whether XML data in implicit parsing ...
 zero_damaged_pages      | off     | Continues processing past damaged page headers.
(196 rows)
```

## Compatibility

The `SHOW` command is a PostgreSQL extension.

## See Also
