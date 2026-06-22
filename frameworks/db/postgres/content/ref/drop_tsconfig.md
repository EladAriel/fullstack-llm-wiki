---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_tsconfig.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP TEXT SEARCH CONFIGURATION

DROP TEXT SEARCH CONFIGURATION
7
SQL - Language Statements

DROP TEXT SEARCH CONFIGURATION
remove a text search configuration

```
DROP TEXT SEARCH CONFIGURATION [ IF EXISTS ] name [ CASCADE | RESTRICT ]
```

## Description

`DROP TEXT SEARCH CONFIGURATION` drops an existing text search configuration. To execute this command you must be the owner of the configuration.

## Parameters

- Do not throw an error if the text search configuration does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of an existing text search configuration.
- Automatically drop objects that depend on the text search configuration, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the text search configuration if any objects depend on it. This is the default.

## Examples

Remove the text search configuration `my_english`:

```
DROP TEXT SEARCH CONFIGURATION my_english;
```

This command will not succeed if there are any existing indexes that reference the configuration in `to_tsvector` calls. Add `CASCADE` to drop such indexes along with the text search configuration.

## Compatibility

There is no `DROP TEXT SEARCH CONFIGURATION` statement in the SQL standard.

## See Also
