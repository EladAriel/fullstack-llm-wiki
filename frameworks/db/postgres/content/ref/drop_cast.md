---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_cast.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP CAST

DROP CAST
7
SQL - Language Statements

DROP CAST
remove a cast

```
DROP CAST [ IF EXISTS ] (source_type AS target_type) [ CASCADE | RESTRICT ]
```

## Description

`DROP CAST` removes a previously defined cast.

To be able to drop a cast, you must own the source or the target data type. These are the same privileges that are required to create a cast.

## Parameters

- Do not throw an error if the cast does not exist. A notice is issued in this case.
- The name of the source data type of the cast.
- The name of the target data type of the cast.
- These key words do not have any effect, since there are no dependencies on casts.

## Examples

To drop the cast from type `text` to type `int`:

```
DROP CAST (text AS int);
```

## Compatibility

The `DROP CAST` command conforms to the SQL standard.

## See Also
