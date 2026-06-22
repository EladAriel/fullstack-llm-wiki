---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_opclass.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

ALTER OPERATOR CLASS

ALTER OPERATOR CLASS
7
SQL - Language Statements

ALTER OPERATOR CLASS
change the definition of an operator class

```
ALTER OPERATOR CLASS name USING index_method
    RENAME TO new_name

ALTER OPERATOR CLASS name USING index_method
    OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }

ALTER OPERATOR CLASS name USING index_method
    SET SCHEMA new_schema
```

## Description

`ALTER OPERATOR CLASS` changes the definition of an operator class.

You must own the operator class to use `ALTER OPERATOR CLASS`. To alter the owner, you must be able to `SET ROLE` to the new owning role, and that role must have `CREATE` privilege on the operator class's schema. (These restrictions enforce that altering the owner doesn't do anything you couldn't do by dropping and recreating the operator class. However, a superuser can alter ownership of any operator class anyway.)

## Parameters

- The name (optionally schema-qualified) of an existing operator class.
- The name of the index method this operator class is for.
- The new name of the operator class.
- The new owner of the operator class.
- The new schema for the operator class.

## Compatibility

There is no `ALTER OPERATOR CLASS` statement in the SQL standard.

## See Also
