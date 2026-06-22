---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ts-query-collection-csharp.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You query a time series collection the same way you query a standard MongoDB collection.

To return one document from a time series collection, you use a FilterDefinitionBuilder<TDocument> <|api-root|/MongoDB.Driver/MongoDB.Driver.FilterDefinitionBuilder-1.html>_ to create a filter to match a document. You pass the filter to the `Find()` method of the `IMongoCollection<TDocument> class.  The following example creates a FilterDefinition and also uses a ProjectionDefinition to omit the id` field from the results. It returns a `List<BsonDocument>`.

For more information on querying your collection, see :driver:`MongoDB C# Driver documentation </csharp/sync/current/crud/query-documents/find/>`.

> **Tip:** To learn how to optimize queries on your time series collection, see
`tsc-best-practice-optimize-query-performance`.
