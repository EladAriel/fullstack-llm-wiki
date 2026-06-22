---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_tsparser.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP TEXT SEARCH PARSER

DROP TEXT SEARCH PARSER
7
SQL - Language Statements

DROP TEXT SEARCH PARSER
remove a text search parser

```
DROP TEXT SEARCH PARSER [ IF EXISTS ] name [ CASCADE | RESTRICT ]
```

## Description

`DROP TEXT SEARCH PARSER` drops an existing text search parser. You must be a superuser to use this command.

## Parameters

- Do not throw an error if the text search parser does not exist. A notice is issued in this case.
- The name (optionally schema-qualified) of an existing text search parser.
- Automatically drop objects that depend on the text search parser, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the text search parser if any objects depend on it. This is the default.

## Examples

Remove the text search parser `my_parser`:

```
DROP TEXT SEARCH PARSER my_parser;
```

This command will not succeed if there are any existing text search configurations that use the parser. Add `CASCADE` to drop such configurations along with the parser.

## Compatibility

There is no `DROP TEXT SEARCH PARSER` statement in the SQL standard.

## See Also
