---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/group-data/outlier-pattern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Group Data with the Outlier Pattern

If your collection stores documents of generally the same size and shape, a drastically different document (an outlier) can cause performance issues for common queries.

Consider a collection that stores an array field. If a document contains many more array elements than other documents in the collection, you may need to handle that document differently in your schema.

Use the outlier pattern to isolate documents that don't match the expected shape from the rest of your collection. Your schema still maintains all of the same data, but common queries are not affected by a single large document.

## Before You Begin

Before you modify your schema to handle outliers, consider the pros and cons of the outlier pattern:

### Pros

The outlier pattern improves performance for commonly-run queries. Queries that return typical documents do not need to also return large outlier documents.

The outlier pattern also handles edge cases in the application. For example, if your application typically displays 50 results from an array, there won't be a document that contains 2,000 results that disrupts the user experience.

### Cons

The outlier pattern requires more complex logic to handle updates. If you frequently need to update your data, you may want to consider other schema design patterns. For more information, see `outlier-pattern-updates`.

## About this Task

Consider a schema that tracks book sales. Typical documents in the collection look like this:

```javascript
db.sales.insertOne(
   {
      "_id": 1,
      "title": "Invisible Cities",
      "year": 1972,
      "author": "Italo Calvino",
      "customers_purchased": [ "user00", "user01", "user02" ]
   }
)
```

The `customers_purchased` array is **unbounded**, meaning that as more customers purchase a book, the array grows larger. For most documents, this is not a problem because the store does not expect more than a few sales for a particular book.

Suppose that a new, popular book results in a large number of purchases. The current schema design results in a bloated document, which negatively impacts performance. To address this issue, implement the outlier pattern for documents that don't have a typical amount of sales.

## Steps

## Results

The outlier pattern prevents atypical documents from impacting query performance. The resulting schema avoids large documents in the collection while maintaining a full list of sales.

Consider an application page that shows information about a book and all users who bought that book. After implementing the outlier pattern, the page displays information for most books (typical documents) quickly.

For popular books (outliers), the application performs an extra query in the `extra_sales` collection on `book_id`. To improve performance for this query, you can create an index on the `book_id` field.

### Updates for Outliers

You need to handle updates for outlier documents differently than typical documents. The logic you use to perform updates depends on your schema design.

To perform updates for outliers for the preceding schema, implement the following application logic:

- Check if the document being updated has `has_extras` set to
`true`.

- If `has_extras` is missing or `false`, add the new purchases
to the `sales` collection.

- If the resulting `customers_purchased` array contains more than
50 elements, set `has_extras` to `true`.

- If `has_extras` is `true`, add the new purchases to the
`sales_extras` collection for the corresponding `book_id`.

## Learn More

- `group-data-bucket-pattern`
- :atlas:`Avoid Unbounded Arrays </schema-suggestions/avoid-unbounded-arrays>`
- `data-modeling-decisions`
- `model-computed-data`
