---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_collation.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP COLLATION

DROP COLLATION
7
SQL - Language Statements

DROP COLLATION
remove a collation

```
DROP COLLATION [ IF EXISTS ] name [ CASCADE | RESTRICT ]
```

## Description

`DROP COLLATION` removes a previously defined collation. To be able to drop a collation, you must own the collation.

## Parameters

- Do not throw an error if the collation does not exist. A notice is issued in this case.
- The name of the collation. The collation name can be schema-qualified.
- Automatically drop objects that depend on the collation, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the collation if any objects depend on it. This is the default.

## Examples

To drop the collation named `german`:

```
DROP COLLATION german;
```

## Compatibility

The `DROP COLLATION` command conforms to the SQL standard, apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
