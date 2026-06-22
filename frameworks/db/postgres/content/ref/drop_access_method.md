---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_access_method.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
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
