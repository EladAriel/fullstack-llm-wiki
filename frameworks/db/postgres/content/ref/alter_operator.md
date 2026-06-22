---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_operator.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

ALTER OPERATOR

ALTER OPERATOR
7
SQL - Language Statements

ALTER OPERATOR
change the definition of an operator

```
ALTER OPERATOR name ( { left_type | NONE } , right_type )
    OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }

ALTER OPERATOR name ( { left_type | NONE } , right_type )
    SET SCHEMA new_schema

ALTER OPERATOR name ( { left_type | NONE } , right_type )
    SET ( {  RESTRICT = { res_proc | NONE }
           | JOIN = { join_proc | NONE }
           | COMMUTATOR = com_op
           | NEGATOR = neg_op
           | HASHES
           | MERGES
          } [, ... ] )
```

## Description

`ALTER OPERATOR` changes the definition of an operator.

You must own the operator to use `ALTER OPERATOR`. To alter the owner, you must be able to `SET ROLE` to the new owning role, and that role must have `CREATE` privilege on the operator's schema. (These restrictions enforce that altering the owner doesn't do anything you couldn't do by dropping and recreating the operator. However, a superuser can alter ownership of any operator anyway.)

## Parameters

- The name (optionally schema-qualified) of an existing operator.
- The data type of the operator's left operand; write `NONE` if the operator has no left operand.
- The data type of the operator's right operand.
- The new owner of the operator.
- The new schema for the operator.
- The restriction selectivity estimator function for this operator; write NONE to remove existing selectivity estimator.
- The join selectivity estimator function for this operator; write NONE to remove existing selectivity estimator.
- The commutator of this operator. Can only be changed if the operator does not have an existing commutator.
- The negator of this operator. Can only be changed if the operator does not have an existing negator.
- Indicates this operator can support a hash join. Can only be enabled and not disabled.
- Indicates this operator can support a merge join. Can only be enabled and not disabled.

## Notes

Refer to `xoper` and `xoper-optimization` for further information.

Since commutators come in pairs that are commutators of each other, `ALTER OPERATOR SET COMMUTATOR` will also set the commutator of the `com_op` to be the target operator. Likewise, `ALTER OPERATOR SET NEGATOR` will also set the negator of the `neg_op` to be the target operator. Therefore, you must own the commutator or negator operator as well as the target operator.

## Examples

Change the owner of a custom operator `a @@ b` for type `text`:

```
ALTER OPERATOR @@ (text, text) OWNER TO joe;
```

Change the restriction and join selectivity estimator functions of a custom operator `a && b` for type `int[]`:

```
ALTER OPERATOR && (int[], int[]) SET (RESTRICT = _int_contsel, JOIN = _int_contjoinsel);
```

Mark the `&&` operator as being its own commutator:

```
ALTER OPERATOR && (int[], int[]) SET (COMMUTATOR = &&);
```

## Compatibility

There is no `ALTER OPERATOR` statement in the SQL standard.

## See Also
