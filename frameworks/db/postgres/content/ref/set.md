---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/set.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

SET

SET
7
SQL - Language Statements

SET
change a run-time parameter

```
SET [ SESSION | LOCAL ] configuration_parameter { TO | = } { value [, ...] | DEFAULT }
SET [ SESSION | LOCAL ] TIME ZONE { value | LOCAL | DEFAULT }
```

## Description

The `SET` command changes run-time configuration parameters. Many of the run-time parameters listed in `runtime-config` can be changed on-the-fly with `SET`. (Some parameters can only be changed by superusers and users who have been granted `SET` privilege on that parameter. There are also parameters that cannot be changed after server or session start.) `SET` only affects the value used by the current session.

If `SET` (or equivalently `SET SESSION`) is issued within a transaction that is later aborted, the effects of the `SET` command disappear when the transaction is rolled back. Once the surrounding transaction is committed, the effects will persist until the end of the session, unless overridden by another `SET`.

The effects of `SET LOCAL` last only till the end of the current transaction, whether committed or not. A special case is `SET` followed by `SET LOCAL` within a single transaction: the `SET LOCAL` value will be seen until the end of the transaction, but afterwards (if the transaction is committed) the `SET` value will take effect.

The effects of `SET` or `SET LOCAL` are also canceled by rolling back to a savepoint that is earlier than the command.

If `SET LOCAL` is used within a function that has a `SET` option for the same variable (see `sql-createfunction`), the effects of the `SET LOCAL` command disappear at function exit; that is, the value in effect when the function was called is restored anyway. This allows `SET LOCAL` to be used for dynamic or repeated changes of a parameter within a function, while still having the convenience of using the `SET` option to save and restore the caller's value. However, a regular `SET` command overrides any surrounding function's `SET` option; its effects will persist unless rolled back.

In PostgreSQL versions 8.0 through 8.2, the effects of a `SET LOCAL` would be canceled by releasing an earlier savepoint, or by successful exit from a `PL/pgSQL` exception block. This behavior has been changed because it was deemed unintuitive.

## Parameters

- Specifies that the command takes effect for the current session. (This is the default if neither `SESSION` nor `LOCAL` appears.)
- Specifies that the command takes effect for only the current transaction. After `COMMIT` or `ROLLBACK`, the session-level setting takes effect again. Issuing this outside of a transaction block emits a warning and otherwise has no effect.
- Name of a settable configuration parameter. Available parameters are documented in `runtime-config` and below.
- New value of the parameter. Values can be specified as string constants, identifiers, numbers, or comma-separated lists of these, as appropriate for the particular parameter. Values that are neither numbers nor valid identifiers must be quoted. If the parameter accepts a list of values, `NULL` can be written to specify an empty list. `DEFAULT` can be written to specify resetting the parameter to its default value (that is, whatever value it would have had if no `SET` had been executed in the current session).

Besides the configuration parameters documented in `runtime-config`, there are a few that can only be adjusted using the `SET` command or that have a special syntax: - `SET SCHEMA 'value'` is an alias for `SET search_path TO value`. Only one schema can be specified using this syntax. - `SET NAMES 'value'` is an alias for `SET client_encoding TO value`. - Sets the internal seed for the random number generator (the function `random`). Allowed values are floating-point numbers between -1 and 1 inclusive. The seed can also be set by invoking the function `setseed`: ``` SELECT setseed(value); ``` - `SET TIME ZONE 'value'` is an alias for `SET timezone TO 'value'`. The syntax `SET TIME ZONE` allows special syntax for the time zone specification. Here are examples of valid values: `'America/Los_Angeles'` The time zone for Berkeley, California. - The time zone for Italy. - The time zone 7 hours west from UTC (equivalent to PDT). Positive values are east from UTC. - The time zone 8 hours west from UTC (equivalent to PST). - Set the time zone to your local time zone (that is, the server's default value of `timezone`).

Timezone settings given as numbers or intervals are internally translated to POSIX timezone syntax. For example, after `SET TIME ZONE -7`, `SHOW TIME ZONE` would report `+07`.

Time zone abbreviations are not supported by `SET`; see `datatype-timezones` for more information about time zones.

## Notes

The function `set_config` provides equivalent functionality; see `functions-admin-set`. Also, it is possible to UPDATE the pg_settings system view to perform the equivalent of `SET`.

## Examples

Set the schema search path:

```
SET search_path TO my_schema, public;
```

Note that this is not the same as

```
SET search_path TO 'my_schema, public';
```

which would have the effect of setting `search_path` to contain a single, probably-nonexistent schema name.

Set the list of temporary tablespace names to be empty:

```
SET temp_tablespaces TO NULL;
```

Set the style of date to traditional POSTGRES with day before month input convention:

```
SET datestyle TO postgres, dmy;
```

Set the time zone for Berkeley, California:

```
SET TIME ZONE 'America/Los_Angeles';
```

Set the time zone for Italy:

```
SET TIME ZONE 'Europe/Rome';
```

## Compatibility

`SET TIME ZONE` extends syntax defined in the SQL standard. The standard allows only numeric time zone offsets while PostgreSQL allows more flexible time-zone specifications. All other `SET` features are PostgreSQL extensions.

## See Also
