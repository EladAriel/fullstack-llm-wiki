---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_foreign_table.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP FOREIGN TABLE

DROP FOREIGN TABLE
7
SQL - Language Statements

DROP FOREIGN TABLE
remove a foreign table

```
DROP FOREIGN TABLE [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP FOREIGN TABLE` removes a foreign table. Only the owner of a foreign table can remove it.

## Parameters

- Do not throw an error if the foreign table does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of the foreign table to drop.
- Automatically drop objects that depend on the foreign table (such as views), and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the foreign table if any objects depend on it. This is the default.

## Examples

To destroy two foreign tables, `films` and `distributors`:

```
DROP FOREIGN TABLE films, distributors;
```

## Compatibility

This command conforms to ISO/IEC 9075-9 (SQL/MED), except that the standard only allows one foreign table to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
