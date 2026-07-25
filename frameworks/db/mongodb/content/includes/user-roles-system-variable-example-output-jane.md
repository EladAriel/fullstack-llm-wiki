---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/user-roles-system-variable-example-output-jane.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

`Jane` has the `Sales` and `Operations` roles, and sees these documents:

```javascript
[
   {
      _id: 1,
      allowedRoles: [ 'Sales' ],
      comment: 'For sales team',
      yearlyBudget: 17000,
      salesEventsBudget: 1000
   },
   {
      _id: 2,
      allowedRoles: [ 'Operations' ],
      comment: 'For operations team',
      yearlyBudget: 19000,
      cloudBudget: 12000
   }
]
```

> **Note:** On a sharded cluster, a query can be run on a shard by another server
node on behalf of the user. In those queries, `USER_ROLES` is still
populated with the roles for the user.
