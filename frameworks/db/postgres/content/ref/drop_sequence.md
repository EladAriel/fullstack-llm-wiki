---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_sequence.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP SEQUENCE

DROP SEQUENCE
7
SQL - Language Statements

DROP SEQUENCE
remove a sequence

```
DROP SEQUENCE [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]
```

## Description

`DROP SEQUENCE` removes sequence number generators. A sequence can only be dropped by its owner or a superuser.

## Parameters

- Do not throw an error if the sequence does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of a sequence.
- Automatically drop objects that depend on the sequence, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the sequence if any objects depend on it. This is the default.

## Examples

To remove the sequence `serial`:

```
DROP SEQUENCE serial;
```

## Compatibility

`DROP SEQUENCE` conforms to the SQL standard, except that the standard only allows one sequence to be dropped per command, and apart from the `IF EXISTS` option, which is a PostgreSQL extension.

## See Also
