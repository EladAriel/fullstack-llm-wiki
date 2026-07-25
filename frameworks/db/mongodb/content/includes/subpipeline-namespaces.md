---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/subpipeline-namespaces.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.0, namespaces in subpipelines within `$lookup` and `$unionWith` are validated to ensure the correct use of `from` and `coll` fields:

- For `$lookup`, omit the `from` field if you use a subpipeline with
a stage which doesn't require a specified collection. For example, a :pipeline:`$documents` stage.

- Similarly, for `$unionWith`, omit the `coll` field.
Unchanged behavior:

- For a `$lookup` that starts with a stage for a collection, for
example a :pipeline:`$match` or :pipeline:`$collStats` subpipeline, you must include the `from` field and specify the collection.

- Similarly, for `$unionWith`, include the `coll` field and specify
the collection.

The following scenario shows an example.

.. include:: /includes/let-example-create-flavors.rst
