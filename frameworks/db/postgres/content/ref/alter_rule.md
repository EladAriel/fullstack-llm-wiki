---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_rule.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

ALTER RULE

ALTER RULE
7
SQL - Language Statements

ALTER RULE
change the definition of a rule

```
ALTER RULE name ON table_name RENAME TO new_name
```

## Description

`ALTER RULE` changes properties of an existing rule. Currently, the only available action is to change the rule's name.

To use `ALTER RULE`, you must own the table or view that the rule applies to.

## Parameters

- The name of an existing rule to alter.
- The name (optionally schema-qualified) of the table or view that the rule applies to.
- The new name for the rule.

## Examples

To rename an existing rule:

```
ALTER RULE notify_all ON emp RENAME TO notify_me;
```

## Compatibility

`ALTER RULE` is a PostgreSQL language extension, as is the entire query rewrite system.

## See Also
