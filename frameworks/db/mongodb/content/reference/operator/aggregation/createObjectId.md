---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/createObjectId.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================================

# $createObjectId (aggregation) (expression operator)

## Definition

.. versionadded:: 8.3

Generate a new random :method:`ObjectId` value.

Use :expression:`$createObjectId` to generate unique ObjectId values in an aggregation pipeline or expression-based update.

For example, you can generate new identifier fields or replace existing `id values so other stages can distinguish between documents. This includes operators that rely on a stable id` value, like :pipeline:`$graphLookup`.

## Syntax

:expression:`$createObjectId` has the following syntax:

```javascript
{
   $createObjectId: { }
}
```

> **Note:** You must use an empty object (`{}`) as the argument.

## Behavior

:expression:`$createObjectId` behaves as follows:

> **Tip:** To convert an existing value to an ObjectId, use :expression:`$toObjectId`.

## Example

.. include:: /includes/sample-data-usage.rst

### Generate identifiers in a view

This example adds ObjectId values to a `view <views-landing-page> so other aggregation stages can rely on a stable id` value.

In the `sample_mflix` database, create a view over the `movies collection that hides the original id` field:

```javascript
db.createView(
   "moviesView",
   "movies",
   [
      { $project: { _id: 0, title: 1, cast: 1 } }
   ]
)
```

Stages that rely on `_id do not behave as expected with this view because the documents no longer have an id` field. For example, a graph traversal stage like :pipeline:`$graphLookup uses id` internally to track visited documents and de-duplicate results.

To use this view with stages that expect a stable identifier, create a second view that adds a unique `_id` field with :expression:`$createObjectId`:

```javascript
db.createView(
   "moviesViewWithId",
   "moviesView",
   [
      {
         $project: {
            _id: { $createObjectId: {} },  // unique id
            title: 1,
            cast: 1
         }
      }
   ]
)
```

You can now run an aggregation that treats each document in `moviesViewWithId` as a distinct node. For example, the following :pipeline:`$graphLookup` stage finds other movies that share cast members with each movie:

```javascript
db.movies.aggregate( [
   {
      $graphLookup: {
         from: "moviesViewWithId",
         startWith: "$cast",
         connectFromField: "cast",
         connectToField: "cast",
         as: "relatedMovies"
      }
   }
] )
```

In this pipeline, :expression:`$createObjectId ensures that each document in the view has a unique ObjectId value in id`. Stages that depend on a stable identifier can then distinguish between documents correctly.
