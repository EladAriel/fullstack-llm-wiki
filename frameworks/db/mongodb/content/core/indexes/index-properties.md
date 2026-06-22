---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-properties.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================

# Index Properties

Index properties affect how the query planner uses an index and how indexed documents are stored. You can specify index properties as optional parameters when you create an index.

The following sections explain the index properties that you can specify when building an index.

> **Note:** Not all index types are compatible with all index properties.

## Case-Insensitive Indexes

`Case-insensitive indexes <index-feature-case-insensitive>` support queries on strings without considering letter case.

## Hidden Indexes

`Hidden indexes <index-type-hidden>` are not visible to the `query planner <query-plans-query-optimization>` and cannot be used to support a query.

You can use hidden indexes to evaluate the potential impact of dropping an index without actually dropping it. If the impact is negative, you can unhide the index instead of having to recreate a dropped index. Hidden indexes are fully maintained and can be used immediately once unhidden.

## Partial Indexes

`Partial indexes <index-type-partial>` only index the documents in a collection that meet a specified filter expression. Partial indexes have lower storage requirements and reduced performance costs for index creation and maintenance.

Partial indexes offer a superset of the functionality of sparse indexes and should be preferred over sparse indexes.

## Sparse Indexes

`Sparse indexes <index-type-sparse>` only contain entries for documents that have the indexed field. These indexes skip documents that do not have the indexed field.

## TTL Indexes

`TTL indexes <index-feature-ttl>` automatically remove documents from a collection after a certain amount of time. Use these indexes for data that only needs to persist for a finite amount of time, like machine generated event data, logs, and session information.

## Unique Indexes

`Unique indexes <index-type-unique>` cause MongoDB to reject duplicate values for the indexed field. These indexes are useful when your documents contain a unique identifier, such as a `userId`.

## Contents

- Case-Insensitive </core/index-case-insensitive>
- Hidden </core/index-hidden>
- Partial </core/index-partial>
- Sparse </core/index-sparse>
- TTL </core/index-ttl>
- Unique </core/index-unique>
