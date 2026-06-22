---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_type.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP TYPE

DROP TYPE
7
SQL - Language Statements

DROP TYPE
remove a data type

```
DROP TYPE [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP TYPE` removes a user-defined data type. Only the owner of a type can remove it.

## Parameters

- Do not throw an error if the type does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of the data type to remove.
- Automatically drop objects that depend on the type (such as table columns, functions, and operators), and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the type if any objects depend on it. This is the default.

## Examples

To remove the data type `box`:

```
DROP TYPE box;
```

## Compatibility

This command is similar to the corresponding command in the SQL standard, apart from the `IF EXISTS` option, which is a PostgreSQL extension. But note that much of the `CREATE TYPE` command and the data type extension mechanisms in PostgreSQL differ from the SQL standard.

## See Also
