---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-iso-date-objects.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The argument can be:

- An `expression <aggregation-expressions>` that resolves to a
`Date <document-bson-type-date>`, a `Timestamp <document-bson-type-timestamp>`, or an `ObjectID <document-bson-type-object-id>`.

- A document with this format:
```javascript
  { date: <dateExpression>, timezone: <tzExpression> }

.. list-table::
  :header-rows: 1
  :widths: 25 75

  * - Field

    - Description

  * - ``date``

    - The date to which the operator is applied.
      ``<dateExpression>`` must be a valid :ref:`expression
      <aggregation-expressions>` that resolves to a
      :ref:`Date <document-bson-type-date>`, a
      :ref:`Timestamp <document-bson-type-timestamp>`,
      or an :ref:`ObjectID <document-bson-type-object-id>`.

  * - ``timezone``

    - .. include:: /includes/fact-timezone-description.rst
```
