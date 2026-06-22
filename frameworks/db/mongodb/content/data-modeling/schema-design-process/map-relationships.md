---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/schema-design-process/map-relationships.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Map Schema Relationships

How you map relationships between data entities affects your application's performance and scalability.

The recommended way to handle related data is to embed it in a sub-document. Embedding related data lets your application query the data it needs with a single read operation and avoid slow :pipeline:`$lookup` operations.

For some use cases, you can use a reference to point to related data in a separate collection.

## About this Task

To determine if you should embed related data or use references, consider the relative importance of the following goals for your application:

Improve queries on related data If your application frequently queries one entity to return data about another entity, embed the data to avoid the need for frequent `$lookup` operations.

Improve data returned from different entities If your application returns data from related entities together, embed the data in a single collection.

Improve update performance If your application frequently updates related data, consider storing the data in its own collection and using a reference to access it. When you use a reference, you reduce your application's write workload by only needing to update the data in a single place.

To learn more about the benefits of embedded data and references, see `data-modeling-decisions`.

## Steps

## Examples

The following examples show how to optimize your schema for different queries depending on the needs of your application.

.. include:: /includes/sample-data-usage.rst

### Optimize Queries for Movies

If your application queries movies for fields such as `title`, embed related information in the `movies` collection. Embedding data returns everything the application needs in a single operation.

The following document optimizes queries on movies:

### Optimize Queries for Movies and Users

If your application returns movie information and user information separately, consider storing movies and users in separate collections. This schema design reduces the work required to return user information, and lets you return only user information without including unneeded fields.

In the following schema, the `movies` collection contains a `userId` field, which is a reference to the `users` collection.

Movies Collection `````````````````

Users Collection ````````````````

## Next Steps

After you map relationships for your application's data, the next step in the schema design process is to apply design patterns to optimize your schema. See `data-modeling-apply-patterns`.

## Learn More

- `databases-and-collections`
- `data-modeling-duplicate-data`
- `data-model-example-keyword-search`
