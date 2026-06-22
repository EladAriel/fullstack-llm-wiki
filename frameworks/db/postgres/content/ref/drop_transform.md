---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_transform.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP TRANSFORM

DROP TRANSFORM
7
SQL - Language Statements

DROP TRANSFORM
remove a transform

```
DROP TRANSFORM [ IF EXISTS ] FOR type_name LANGUAGE lang_name [ CASCADE | RESTRICT ]
```

## Description

`DROP TRANSFORM` removes a previously defined transform.

To be able to drop a transform, you must own the type and the language. These are the same privileges that are required to create a transform.

## Parameters

- Do not throw an error if the transform does not exist. A notice is issued in this case.
- The name of the data type of the transform.
- The name of the language of the transform.
- Automatically drop objects that depend on the transform, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the transform if any objects depend on it. This is the default.

## Examples

To drop the transform for type `hstore` and language `plpython3u`:

```
DROP TRANSFORM FOR hstore LANGUAGE plpython3u;
```

## Compatibility

This form of `DROP TRANSFORM` is a PostgreSQL extension. See `sql-createtransform` for details.

## See Also
