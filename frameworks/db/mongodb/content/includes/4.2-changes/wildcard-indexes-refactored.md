---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/4.2-changes/wildcard-indexes-refactored.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Consider an application that captures user-defined data under the `userMetadata` field and supports querying against that data:

```javascript
{ "userMetadata" : { "likes" : [ "dogs", "cats" ] } }
{ "userMetadata" : { "dislikes" : "pickles" } }
{ "userMetadata" : { "age" : 45 } }
{ "userMetadata" : "inactive" }
```

Administrators want to create indexes to support queries on any subfield of `userMetadata`.

A wildcard index on `userMetadata` can support single-field queries on `userMetadata`, `userMetadata.likes`, `userMetadata.dislikes`, and `userMetadata.age`:

```bash
db.userData.createIndex( { "userMetadata.$**" : 1 } )
```

The index can support the following queries:

```bash
db.userData.find({ "userMetadata.likes" : "dogs" })
db.userData.find({ "userMetadata.dislikes" : "pickles" })
db.userData.find({ "userMetadata.age" : { $gt : 30 } })
db.userData.find({ "userMetadata" : "inactive" })
```

A non-wildcard index on `userMetadata` can only support queries on values of `userMetadata`.

> **Important:** Wildcard indexes are not designed to replace workload-based index
planning. For more information on creating indexes to support
queries, see `create-indexes-to-support-queries`. For
complete documentation on wildcard index limitations, see
`wildcard-index-restrictions`.

The :binary:`~bin.mongod` `featureCompatibilityVersion <view-fcv>` must be `4.2` to create wildcard indexes. For instructions on setting the FCV, see `Setting the FCV <set-fcv>`.
