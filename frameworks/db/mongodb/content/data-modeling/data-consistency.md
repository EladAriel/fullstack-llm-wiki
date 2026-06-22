---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/data-consistency.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================

# Data Consistency

MongoDB gives you the flexibility to normalize or duplicate your data to optimize your application. If you duplicate data in your schema, you must decide how to keep duplicated data consistent across multiple collections. Some applications require duplicated data to be made consistent immediately, whereas other applications can tolerate reading stale data.

## Use Cases

There are multiple ways to enforce data consistency in your application:

The best way to enforce data consistency depends on your application. To learn more about the benefits and implementation for each approach, refer to the corresponding documentation pages.

## Tasks

To enforce data consistency in your application, see the following pages:

- `enforce-consistency-transactions`
- `enforce-consistency-embedding`
## Details

The following factors can affect how you enforce data consistency.

### Data Staleness

Consider how important it is that your application returns the most up-to-date data. Some applications can return data that is minutes or hours stale with no impact to the user.

For example, in an e-commerce application, a user needs to know immediately whether or not an item is available. This information is ideally kept as consistent as possible, even if it requires frequent updates.

In contrast, analytic queries are typically expected to read slightly stale data. It is not critical to keep analytic data completely consistent.

Your application's tolerance for stale data affects how to best keep data consistent. Frequently updating data in multiple collections reduces the risk that a user reads stale data. However, frequent updates can negatively impact your application's performance. When you enforce data consistency, balance user needs with performance impact.

### Referential Integrity

Referential integrity ensures that when an object is deleted, all references to that object are also deleted.

For example, an application has a `products` collection and a `warehouse` collection that contains references to the `products` collection. When a product is deleted from the `products` collection, the corresponding reference in the `warehouse` collection should also be deleted.

If your schema requires referential integrity, incorporate logic into your application to keep references consistent. At minimum, your application logic should prevent errors when attempting to query a reference that does not exist.

## Learn More

- `schema-validation-overview`
- `data-modeling-atomic-operation`
- `Production Considerations for Transactions <production-considerations>`
## Contents

- Use Transactions </data-modeling/enforce-consistency/transactions>
- Use Embedding </data-modeling/enforce-consistency/embed-data>
