---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/query-optimization.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# Query Optimization

Query optimization improves the efficiency of read operations by reducing the amount of data that query operations need to process. Use indexes, projections, and query limits to enhance query performance and reduce resource consumption.

Query optimization can occur both during development and later as your data usage and demand changes. As collections grow, a periodic review of query performance can help determine when clusters need to scale up or scale out.

## Create Indexes to Support Queries

`Indexes <indexes>` store values from individual fields or sets of fields from a collection in a separate data structure. In read operations, they allow MongoDB to search in the index to identify relevant documents instead of the entire collection. In write operations, MongoDB must both write the change to the collection and update the index.

Create indexes for commonly issued queries. If a query searches multiple fields, create a `compound index <index-type-compound>`.

For example, consider the following query on the `rated` field in the `movies` collection:

```javascript
let ratingValue = <someUserInput>;
db.movies.find( { rated: ratingValue } );
```

To improve performance for this query, add an index to the `movies` collection on the `rated` field. [#ensureIndexOrder]_ In :binary:`~bin.mongosh`, create indexes using the :method:`db.collection.createIndex()` method:

To analyze query performance, see `/tutorial/analyze-query-plan`.

For single-field indexes, the order of the index doesn't matter. For compound indexes, the field order impacts what queries the index supports. For details, see `index-ascending-and-descending`.

## Create Selective Queries

Query selectivity refers to how well the query predicate filters out documents in a collection. Query selectivity determines whether queries can use indexes effectively.

More selective queries match a smaller percentage of documents. For instance, an equality match on the unique `_id` field is highly selective as it can match at most one document.

Less selective queries match a larger percentage of documents and can't use indexes effectively.

.. include:: /includes/extracts/inequality_operators_selectivity.rst

The selectivity of :query:`regular expressions <$regex>` depends on the expressions themselves. For details, see `regular expression and index use <regex-index-use>`.

## Project Only Necessary Data

When you need a subset of fields from documents, you can improve performance by returning only the fields you need. Projections reduce network traffic and processing time.

For example, if your query to the `movies` collection needs only the `year`, `title`, `directors`, and `plot` fields, specify those fields in the projection:

.. include:: /includes/aggregation/fact-project-stage-placement.rst

For more information on using projections, see `read-operations-projection`.

### Example

To achieve a covered query, you must index projected fields. The `ESR (Equality, Sort, Range) rule <esr-indexing-guideline>` applies to the order of fields in the index.

For example, consider the following index on a `movies` collection:

The preceding index, while technically correct, isn't structured to optimize query performance.

The following query uses the ESR (Equality, Sort, Range) rule to structure a more efficient aggregation pipeline and improve query response times.

The index and query follow the ESR rule:

- `rated` is used for an equality match (E), so it is the first
field in the index.

- `title` is used for sorting (S), so it is after `rated` in
the index.

- `released` is used for a range query (R), so it is the last
field in the index.

## Limit Query Results

MongoDB `cursors <cursor>` return results in batches. If you know the number of results you want, specify that value in the :method:`~cursor.limit()` method. Limiting results reduces the demand on network resources.

Sort results before applying a limit to ensure that the query returns the expected documents. For example, if you need only 10 results from your query to the `movies` collection, run the following query:

For more information on limiting results, see :method:`~cursor.limit()`.

## Use Index Hints

The `query optimizer <read-operations-query-optimization>` typically selects the optimal index for a specific operation. However, you can force MongoDB to use a specific index using the :method:`~cursor.hint()` method. Use :method:`~cursor.hint()` to support performance testing or when you are querying a field that appears in several indexes to ensure that MongoDB uses the correct index.

## Use Server-Side Operations

Use the :update:`$inc` operator to increment or decrement values in documents. The operator increments the value of the field on the server side, as an alternative to selecting a document, making changes in the client code, and then writing the entire document to the server. The :update:`$inc` operator can also help avoid race conditions that occur when two application instances query for a document, manually increment a field, and save the entire document back at the same time.

## Run Covered Queries

A covered query is a query that can be satisfied entirely using an index and doesn't have to examine any documents. An index covers a query when all of the following apply:

- All the fields in the query (both as specified by the application and
as needed internally such as for sharding purposes) are part of an index.

- All the fields returned in the results are in the same index.
- No fields in the query are equal to `null`. For example, the
following query predicates can't result in covered queries:

- `{ "field": null }`
- `{ "field": { $eq: null } }`
### Example

A `movies` collection has the following index on the `rated` and `title` fields:

The index covers the following operation which queries on the `rated` and `title` fields and returns only the `title` field:

For the specified index to cover the query, the projection document must explicitly specify `_id: 0 to exclude the id field from the result since the index doesn't include the id` field.

### Embedded Documents

An index can cover a query on fields within embedded documents.

For example, consider the `theaters` collection from the :atlas:`sample_mflix </sample-data/sample-mflix/>` dataset, which has documents with the following structure:

```javascript
{
  theaterId: <num>,
  location: {
    address: {
      street1: "<address>",
      city: "<city>",
      state: "<state>",
      zipcode: "<zip>"
    },
    geo: { ... }
  }
}
```

The collection has the following index:

The `{ "location.address.city": 1 }` index covers the following query:

> **Note:** To index fields in embedded documents, use `dot notation`. See
`index-embedded-fields`.

### Multikey Covering

Multikey indexes can cover queries over the non-array fields if the index tracks which field or fields cause the index to be multikey.

.. include:: /includes/fact-multikey-index-covered-query.rst

For an example of a covered query with a multikey index, see `multikey-covered-queries` on the multikey indexes page.

### Performance

Because the index contains all fields required by the query, MongoDB can both match the `query conditions <read-operations-query-document>` and return the results using only the index.

Querying only the index can be much faster than querying documents outside of the index. Index keys are typically smaller than the documents they catalog, and indexes are typically available in RAM or located sequentially on disk.

### Limitations

Index Types ```````````

Not all `index types <index-types>` can cover queries. For details on covered index support, refer to the documentation page for the corresponding index type.

Sharded Collections ```````````````````

.. include:: /includes/extracts/fact-covered-query-sharded-collection-cover.rst

### Explain Results

To determine whether a query is a covered query, use the :method:`db.collection.explain()` or the :method:`~cursor.explain()` method. See `explain-output-covered-queries`.

## Contents

- Analyze Performance </tutorial/evaluate-operation-performance>
- Write Performance </core/write-performance>
