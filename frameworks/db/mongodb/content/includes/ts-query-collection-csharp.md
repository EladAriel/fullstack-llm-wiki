---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ts-query-collection-csharp.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You query a time series collection the same way you query a standard MongoDB collection.

To return one document from a time series collection, you use a FilterDefinitionBuilder<TDocument> <|api-root|/MongoDB.Driver/MongoDB.Driver.FilterDefinitionBuilder-1.html>_ to create a filter to match a document. You pass the filter to the `Find()` method of the `IMongoCollection<TDocument> class.  The following example creates a FilterDefinition and also uses a ProjectionDefinition to omit the id` field from the results. It returns a `List<BsonDocument>`.

For more information on querying your collection, see :driver:`MongoDB .NET/C# Driver documentation </csharp/sync/current/crud/query-documents/find/>`.

> **Tip:** To learn how to optimize queries on your time series collection, see
`tsc-best-practice-optimize-query-performance`.
