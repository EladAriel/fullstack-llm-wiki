---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/materialized-views.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# On-Demand Materialized Views

> **Note:** This page discusses on-demand materialized views. For discussion of
standard views, see `views-landing-page`.
To understand the differences between the view types, see
`materialized-view-compare`.

An on-demand materialized view is a pre-computed aggregation pipeline result that is stored on and read from disk. On-demand materialized views are typically the results of a :pipeline:`$merge` or :pipeline:`$out` stage.

## Comparison with Standard Views

.. include:: /includes/views/fact-compare-view-and-materialized-view.rst

## Create a Materialized View in the {+atlas+} UI

The example in this section uses the :atlas:`sample training dataset </sample-data/sample-training/>`. To learn how to load the sample dataset into your {+atlas+} deployment, see :atlas:`Load Sample Data </sample-data/#std-label-load-sample-data>`.

To create a materialized view in the {+atlas+} UI, follow these steps:

## Example

The example uses the `movies` collection from the :atlas:`sample_mflix </sample-data/sample-mflix/>` dataset. To learn how to load sample data, see :atlas:`Load Sample Data </sample-data/#std-label-load-sample-data>`.

### 1. Define the On-Demand Materialized View

The following `updateMovieStats` function defines a `movieYearStats` materialized view that contains the count and average IMDb rating of movies by year. The function accepts a `startYear` parameter to update statistics for movies released from that year forward.

- The :pipeline:`$match` stage filters movies to process only
those with a `year` value greater than or equal to `startYear`.

- The :pipeline:`$group` stage groups movies by `year`. The
documents output by this stage have the form:

```javascript
  { "_id" : <year>, "movieCount" : <num>, "avgRating" : <num> }
```

- The :pipeline:`$merge` stage writes the output to the
`movieYearStats` collection.

The stage matches `on <merge-on> the id` field and checks if each aggregation result `matches <merge-whenMatched>` an existing document:

- `When there is a match <merge-whenMatched>` (that is, a
document with the same year already exists in the collection), the stage `replaces the existing document <merge-whenMatched-replace>` with the document from the aggregation results.

- `When there isn't a match <merge-whenNotMatched>`, the
stage inserts the document from the aggregation results into the collection (the default behavior when not matched).

### 2. Perform Initial Run

For the initial run, pass in a starting year to populate `movieYearStats` with data from that year forward:

After the initial run, `db.movieYearStats.find().sort( { _id: 1 } )` returns documents like the following:

```javascript
{ "_id" : 2015, "movieCount" : <num>, "avgRating" : <num> }
{ "_id" : 2016, "movieCount" : <num>, "avgRating" : <num> }
{ "_id" : 2017, "movieCount" : <num>, "avgRating" : <num> }
```

### 3. Refresh Materialized View

Assume a new movie is added to the `movies` collection for 2016:

To refresh `movieYearStats` for 2016 onward, run the function with a `startYear` of `2016`:

The updated `movieYearStats` reflects the new movie in the `movies` collection. `db.movieYearStats.find().sort( { _id: 1 } )` returns:

```javascript
{ "_id" : 2015, "movieCount" : <num>, "avgRating" : <num> }
{ "_id" : 2016, "movieCount" : <num>, "avgRating" : <num> }
{ "_id" : 2017, "movieCount" : <num>, "avgRating" : <num> }
```

## Additional Information

The :pipeline:`$merge` stage:

- Can output to a collection in the same or different database.
- Creates a new collection if the output collection does not already
exist.

- Can incorporate results (insert new documents, merge documents,
replace documents, keep existing documents, fail the operation, process documents with a custom update pipeline) into an existing collection.

- Can output to a sharded collection. Input collection can
also be sharded.

See :pipeline:`$merge` for:

- More information on :pipeline:`$merge` and available options
- Example: `merge-mat-view-init-creation`
- Example: `merge-mat-view-refresh`
- Example: `merge-mat-view-insert-only`
