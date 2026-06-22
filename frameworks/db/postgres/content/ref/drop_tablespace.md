---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_tablespace.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP TABLESPACE

DROP TABLESPACE
7
SQL - Language Statements

DROP TABLESPACE
remove a tablespace

```
DROP TABLESPACE [ IF EXISTS ] name
```

## Description

`DROP TABLESPACE` removes a tablespace from the system.

A tablespace can only be dropped by its owner or a superuser. The tablespace must be empty of all database objects before it can be dropped. It is possible that objects in other databases might still reside in the tablespace even if no objects in the current database are using the tablespace. Also, if the tablespace is listed in the `guc-temp-tablespaces` setting of any active session, the `DROP` might fail due to temporary files residing in the tablespace.

## Parameters

- Do not throw an error if the tablespace does not exist. A notice is issued in this case.
- The name of a tablespace.

## Notes

`DROP TABLESPACE` cannot be executed inside a transaction block.

## Examples

To remove tablespace `mystuff` from the system:

```
DROP TABLESPACE mystuff;
```

## Compatibility

`DROP TABLESPACE` is a PostgreSQL extension.

## See Also
