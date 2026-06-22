---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_extension.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP EXTENSION

DROP EXTENSION
7
SQL - Language Statements

DROP EXTENSION
remove an extension

```
DROP EXTENSION [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP EXTENSION` removes extensions from the database. Dropping an extension causes its member objects, and other explicitly dependent routines (see `sql-alterroutine`, the `DEPENDS ON EXTENSION extension_name` action), to be dropped as well.

You must own the extension to use `DROP EXTENSION`.

## Parameters

- Do not throw an error if the extension does not exist. A notice is issued in this case.
- The name of an installed extension.
- Automatically drop objects that depend on the extension, and in turn all objects that depend on those objects (see `ddl-depend`).
- This option prevents the specified extensions from being dropped if other objects, besides these extensions, their members, and their explicitly dependent routines, depend on them. This is the default.

## Examples

To remove the extension `hstore` from the current database:

```
DROP EXTENSION hstore;
```

This command will fail if any of `hstore`'s objects are in use in the database, for example if any tables have columns of the `hstore` type. Add the `CASCADE` option to forcibly remove those dependent objects as well.

## Compatibility

`DROP EXTENSION` is a PostgreSQL extension.

## See Also
