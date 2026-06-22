---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_server.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP SERVER

DROP SERVER
7
SQL - Language Statements

DROP SERVER
remove a foreign server descriptor

```
DROP SERVER [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP SERVER` removes an existing foreign server descriptor. To execute this command, the current user must be the owner of the server.

## Parameters

- Do not throw an error if the server does not exist. A notice is issued in this case.
- The name of an existing server.
- Automatically drop objects that depend on the server (such as user mappings), and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the server if any objects depend on it. This is the default.

## Examples

Drop a server `foo` if it exists:

```
DROP SERVER IF EXISTS foo;
```

## Compatibility

`DROP SERVER` conforms to ISO/IEC 9075-9 (SQL/MED). The `IF EXISTS` clause is a PostgreSQL extension.

## See Also
