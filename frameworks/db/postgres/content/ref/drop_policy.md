---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_policy.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

DROP POLICY

DROP POLICY
7
SQL - Language Statements

DROP POLICY
remove a row-level security policy from a table

```
DROP POLICY [ IF EXISTS ] name ON table_name [ CASCADE | RESTRICT ]
```

## Description

`DROP POLICY` removes the specified policy from the table. Note that if the last policy is removed for a table and the table still has row-level security enabled via `ALTER TABLE`, then the default-deny policy will be used. `ALTER TABLE ... DISABLE ROW LEVEL SECURITY` can be used to disable row-level security for a table, whether policies for the table exist or not.

## Parameters

- Do not throw an error if the policy does not exist. A notice is issued in this case.
- The name of the policy to drop.
- The name (optionally schema-qualified) of the table that the policy is on.
- These key words do not have any effect, since there are no dependencies on policies.

## Examples

To drop the policy called `p1` on the table named `my_table`:

```
DROP POLICY p1 ON my_table;
```

## Compatibility

`DROP POLICY` is a PostgreSQL extension.

## See Also
