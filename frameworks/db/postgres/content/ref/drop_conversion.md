---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_conversion.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

DROP CONVERSION

DROP CONVERSION
7
SQL - Language Statements

DROP CONVERSION
remove a conversion

```
DROP CONVERSION [ IF EXISTS ] name [ CASCADE | RESTRICT ]
```

## Description

`DROP CONVERSION` removes a previously defined conversion. To be able to drop a conversion, you must own the conversion.

## Parameters

- Do not throw an error if the conversion does not exist. A notice is issued in this case.
- The name of the conversion. The conversion name can be schema-qualified.
- These key words do not have any effect, since there are no dependencies on conversions.

## Examples

To drop the conversion named `myname`:

```
DROP CONVERSION myname;
```

## Compatibility

There is no `DROP CONVERSION` statement in the SQL standard, but a `DROP TRANSLATION` statement that goes along with the `CREATE TRANSLATION` statement that is similar to the `CREATE CONVERSION` statement in PostgreSQL.

## See Also
