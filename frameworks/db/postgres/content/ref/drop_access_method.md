---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_access_method.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

DROP ACCESS METHOD

DROP ACCESS METHOD
7
SQL - Language Statements

DROP ACCESS METHOD
remove an access method

```
DROP ACCESS METHOD [ IF EXISTS ] name [ CASCADE | RESTRICT ]
```

## Description

`DROP ACCESS METHOD` removes an existing access method. Only superusers can drop access methods.

## Parameters

- Do not throw an error if the access method does not exist. A notice is issued in this case.
- The name of an existing access method.
- Automatically drop objects that depend on the access method (such as operator classes, operator families, and indexes), and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the access method if any objects depend on it. This is the default.

## Examples

Drop the access method `heptree`:

```
DROP ACCESS METHOD heptree;
```

## Compatibility

`DROP ACCESS METHOD` is a PostgreSQL extension.

## See Also
