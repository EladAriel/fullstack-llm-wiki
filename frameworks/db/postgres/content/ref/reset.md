---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/reset.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

RESET

RESET
7
SQL - Language Statements

RESET
restore the value of a run-time parameter to the default value

```
RESET configuration_parameter
RESET ALL
```

## Description

`RESET` restores run-time parameters to their default values. `RESET` is an alternative spelling for

```
SET configuration_parameter TO DEFAULT
```

Refer to `sql-set` for details.

The default value is defined as the value that the parameter would have had, if no `SET` had ever been issued for it in the current session. The actual source of this value might be a compiled-in default, the configuration file, command-line options, or per-database or per-user default settings. This is subtly different from defining it as the value that the parameter had at session start, because if the value came from the configuration file, it will be reset to whatever is specified by the configuration file now. See `runtime-config` for details.

The transactional behavior of `RESET` is the same as `SET`: its effects will be undone by transaction rollback.

## Parameters

- Name of a settable run-time parameter. Available parameters are documented in `runtime-config` and on the `sql-set` reference page.
- Resets all settable run-time parameters to default values.

## Examples

Set the `timezone` configuration variable to its default value:

```
RESET timezone;
```

## Compatibility

`RESET` is a PostgreSQL extension.

## See Also
