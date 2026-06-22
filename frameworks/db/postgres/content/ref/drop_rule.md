---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_rule.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP RULE

DROP RULE
7
SQL - Language Statements

DROP RULE
remove a rewrite rule

```
DROP RULE [ IF EXISTS ] name ON table_name [ CASCADE | RESTRICT ]
```

## Description

`DROP RULE` drops a rewrite rule.

## Parameters

- Do not throw an error if the rule does not exist. A notice is issued in this case.
- The name of the rule to drop.
- The name (optionally schema-qualified) of the table or view that the rule applies to.
- Automatically drop objects that depend on the rule, and in turn all objects that depend on those objects (see `ddl-depend`).
- Refuse to drop the rule if any objects depend on it. This is the default.

## Examples

To drop the rewrite rule `newrule`:

```
DROP RULE newrule ON mytable;
```

## Compatibility

`DROP RULE` is a PostgreSQL language extension, as is the entire query rewrite system.

## See Also
