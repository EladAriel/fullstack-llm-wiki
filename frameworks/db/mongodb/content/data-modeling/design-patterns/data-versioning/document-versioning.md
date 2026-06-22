---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/data-versioning/document-versioning.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Keep a History of Document Versions

When your data changes, some applications require that older versions of your data are kept available. In the **Document Versioning Pattern**, older data versions are retained in a separate collection from the current data.

The Document Versioning Pattern lets you keep current documents and their history in the same database, and avoid having to use multiple systems to manage data history.

## About this Task

The Document Versioning Pattern works best if your data meets these criteria:

- Documents are updated infrequently.
- There are few documents that require version tracking.
- Current data and historical data are generally queried separately. In
the Document Versioning Pattern, historical data is stored in a separate collection from the current data, so returning both in the same operation can be expensive.

If the preceding criteria do not fit your use case, consider a different solution or change how you implement the Document Versioning Pattern.

## Before you Begin

In the following example, an insurance company uses the Document Versioning Pattern to track changes to customer policies. Insert the sample document into the `currentPolicies` and `policyRevisions` collections:

```javascript
db.currentPolicies.insertOne(
   {
      policyId: 1,
      customerName: "Michelle",
      revision: 1,
      itemsInsured: [
         "golf clubs",
         "car"
      ],
      dateSet: new Date()
   }
)
```

```javascript
db.policyRevisions.insertOne(
   {
      policyId: 1,
      customerName: "Michelle",
      revision: 1,
      itemsInsured: [
         "golf clubs",
         "car"
      ],
      dateSet: new Date()
   }
)
```

## Steps

With the Document Versioning Pattern, when a policy is updated, the following writes occur:

- The policy is updated in the `currentPolicies` collection. The
`currentPolicies` collection only contains the current data revision of each `policyId`.

- The original policy is written to the `policyRevisions` collection to
keep a record of policy changes.

For example, if the user Michelle wants to add a watch to her policy, the application runs these operations:

## Next Steps

To view a customer's policy history, you can sort the `policyRevisions` collection by revision. Consider if the customer Michelle makes another change to her policy and no longer wants to insure her golf clubs.

## Learn More

- `design-patterns-schema-versioning`
- `data-modeling-schema-design`
- `schema-pattern-group-data`
