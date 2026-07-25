---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/views/join-collections-with-view.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# Use a View to Join Two Collections

Use :pipeline:`$lookup` to create a view over two collections. Applications can query the view without constructing or maintaining complex pipelines.

## Example

.. include:: /includes/sample-data-usage.rst

### Create a Joined View

In the example:

- The :pipeline:`$match` stage filters the `movies` collection to
documents released in 2014 onward.

- The :pipeline:`$lookup stage uses the id` field in the
`movies` collection to join documents in the `comments` collection that have a matching `movie_id` field.

- The matching documents are added as an array in the
`movieComments` field.

- The :pipeline:`$project` stage selects a subset of the available
fields, including `numComments`, which is the count of comments for each movie.

### Query the View

Query the view for the five movies with the most comments:

```javascript
[
  { _id: '<title>', totalComments: <num> },
  { _id: '<title>', totalComments: <num> },
  { _id: '<title>', totalComments: <num> },
  { _id: '<title>', totalComments: <num> },
  { _id: '<title>', totalComments: <num> }
]
```
