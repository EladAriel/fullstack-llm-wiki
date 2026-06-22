---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_materialized_view.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP MATERIALIZED VIEW

DROP MATERIALIZED VIEW
7
SQL - Language Statements

DROP MATERIALIZED VIEW
remove a materialized view

```
DROP MATERIALIZED VIEW [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP MATERIALIZED VIEW` drops an existing materialized view. To execute this command you must be the owner of the materialized view.

## Parameters

- Do not throw an error if the materialized view does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of the materialized view to remove.
- Automatically drop objects that depend on the materialized view (such as other materialized views, or regular views), and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the materialized view if any objects depend on it. This is the default.

## Examples

This command will remove the materialized view called `order_summary`:

```
DROP MATERIALIZED VIEW order_summary;
```

## Compatibility

`DROP MATERIALIZED VIEW` is a PostgreSQL extension.

## See Also
