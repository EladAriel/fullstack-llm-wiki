---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/func/func-logical.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## Logical Operators

operator
logical

Boolean
operators
operators, logical

The usual logical operators are available: AND (operator) OR (operator) NOT (operator) conjunction disjunction negation

```
boolean AND boolean boolean
boolean OR boolean boolean
NOT boolean boolean
```

SQL uses a three-valued logic system with true, false, and `null`, which represents unknown. Observe the following truth tables: `a` `b` `a` AND `b` `a` OR `b` TRUE TRUE TRUE TRUE TRUE FALSE FALSE TRUE TRUE NULL NULL TRUE FALSE FALSE FALSE FALSE FALSE NULL FALSE NULL NULL NULL NULL NULL `a` NOT `a` TRUE FALSE FALSE TRUE NULL NULL

The operators `AND` and `OR` are commutative, that is, you can switch the left and right operands without affecting the result. (However, it is not guaranteed that the left operand is evaluated before the right operand. See `syntax-express-eval` for more information about the order of evaluation of subexpressions.)
