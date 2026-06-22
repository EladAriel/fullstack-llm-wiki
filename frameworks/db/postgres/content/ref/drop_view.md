---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_view.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP VIEW

DROP VIEW
7
SQL - Language Statements

DROP VIEW
remove a view

```
DROP VIEW [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP VIEW` drops an existing view. To execute this command you must be the owner of the view.

## Parameters

- Do not throw an error if the view does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of the view to remove.
- Automatically drop objects that depend on the view (such as other views), and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the view if any objects depend on it. This is the default.

## Examples

This command will remove the view called `kinds`:

```
DROP VIEW kinds;
```

## Compatibility

This command conforms to the SQL standard, except that the standard only allows one view to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
