---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_publication.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP PUBLICATION

DROP PUBLICATION
7
SQL - Language Statements

DROP PUBLICATION
remove a publication

```
DROP PUBLICATION [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP PUBLICATION` removes an existing publication from the database.

A publication can only be dropped by its owner or a superuser.

## Parameters

- Do not throw an error if the publication does not exist. A notice is issued in this case.
- The name of an existing publication.
- These key words do not have any effect, since there are no dependencies on publications.

## Examples

Drop a publication:

```
DROP PUBLICATION mypublication;
```

## Compatibility

`DROP PUBLICATION` is a PostgreSQL extension.

## See Also
