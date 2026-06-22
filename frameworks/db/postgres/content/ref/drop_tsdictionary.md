---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_tsdictionary.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP TEXT SEARCH DICTIONARY

DROP TEXT SEARCH DICTIONARY
7
SQL - Language Statements

DROP TEXT SEARCH DICTIONARY
remove a text search dictionary

```
DROP TEXT SEARCH DICTIONARY [ IF EXISTS ] name [ CASCADE | RESTRICT ]
```

## Description

`DROP TEXT SEARCH DICTIONARY` drops an existing text search dictionary. To execute this command you must be the owner of the dictionary.

## Parameters

- Do not throw an error if the text search dictionary does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of an existing text search dictionary.
- Automatically drop objects that depend on the text search dictionary, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the text search dictionary if any objects depend on it. This is the default.

## Examples

Remove the text search dictionary `english`:

```
DROP TEXT SEARCH DICTIONARY english;
```

This command will not succeed if there are any existing text search configurations that use the dictionary. Add `CASCADE` to drop such configurations along with the dictionary.

## Compatibility

There is no `DROP TEXT SEARCH DICTIONARY` statement in the SQL standard.

## See Also
