---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/output-upgrade-check.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

## Error Output

The upgrade check can return the following errors when it encounters incompatibilities in your data:

### Index Key Exceed Limit

```none
Document Error: key for index '<indexName>' (<indexSpec>) too long on document: <doc>
```

To resolve, remove the document. Ensure that the query to remove the document does not specify a condition on the invalid field or field.

### Documents with Illegal Field Names

```none
Document Error: document is no longer valid in 2.6 because <errmsg>: <doc>
```

To resolve, remove the document and re-insert with the appropriate corrections.

### Index Specification Invalid

```none
Index Error: invalid index spec for index '<indexName>': <indexSpec>
```

To resolve, remove the invalid index and recreate with a valid index specification.

### Missing `_id` Index

```none
Collection Error: lack of _id index on collection: <collectionName>
```

To resolve, create a unique index on `_id`.

## Warning Output

```none
Warning: upgradeCheck only supports V1 indexes. Skipping index: <indexSpec>
```

To resolve, remove the invalid index and recreate the index omitting the version specification, or reindex the collection. Reindex operation may be expensive for collections that have a large amount of data and/or a large number of indexes.
