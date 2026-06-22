---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_tstemplate.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP TEXT SEARCH TEMPLATE

DROP TEXT SEARCH TEMPLATE
7
SQL - Language Statements

DROP TEXT SEARCH TEMPLATE
remove a text search template

```
DROP TEXT SEARCH TEMPLATE [ IF EXISTS ] name [ CASCADE | RESTRICT ]
```

## Description

`DROP TEXT SEARCH TEMPLATE` drops an existing text search template. You must be a superuser to use this command.

## Parameters

- Do not throw an error if the text search template does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of an existing text search template.
- Automatically drop objects that depend on the text search template, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the text search template if any objects depend on it. This is the default.

## Examples

Remove the text search template `thesaurus`:

```
DROP TEXT SEARCH TEMPLATE thesaurus;
```

This command will not succeed if there are any existing text search dictionaries that use the template. Add `CASCADE` to drop such dictionaries along with the template.

## Compatibility

There is no `DROP TEXT SEARCH TEMPLATE` statement in the SQL standard.

## See Also
