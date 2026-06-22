---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_property_graph.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP PROPERTY GRAPH

DROP PROPERTY GRAPH
7
SQL - Language Statements

DROP PROPERTY GRAPH
remove an SQL-property graph

```
DROP PROPERTY GRAPH [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP PROPERTY GRAPH` drops an existing property graph. To execute this command you must be the owner of the property graph.

## Parameters

- Do not throw an error if the property graph does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of the property graph to remove.
- Automatically drop objects that depend on the property graph, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the property graph if any objects depend on it. This is the default.

## Examples

```
DROP PROPERTY GRAPH g1;
```

## Compatibility

`DROP PROPERTY GRAPH` conforms to ISO/IEC 9075-16 (SQL/PGQ), except that the standard only allows one property graph to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
