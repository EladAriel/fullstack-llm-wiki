---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_language.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP LANGUAGE

DROP LANGUAGE
7
SQL - Language Statements

DROP LANGUAGE
remove a procedural language

```
DROP [ PROCEDURAL ] LANGUAGE [ IF EXISTS ] name [ CASCADE | RESTRICT ]
```

## Description

`DROP LANGUAGE` removes the definition of a previously registered procedural language. You must be a superuser or the owner of the language to use `DROP LANGUAGE`.

As of PostgreSQL 9.1, most procedural languages have been made into extensions, and should therefore be removed with DROP EXTENSION not `DROP LANGUAGE`.

## Parameters

- Do not throw an error if the language does not exist. A notice is issued in this case.
- The name of an existing procedural language.
- Automatically drop objects that depend on the language (such as functions in the language), and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the language if any objects depend on it. This is the default.

## Examples

This command removes the procedural language `plsample`:

```
DROP LANGUAGE plsample;
```

## Compatibility

There is no `DROP LANGUAGE` statement in the SQL standard.

## See Also
