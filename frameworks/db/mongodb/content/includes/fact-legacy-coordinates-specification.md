---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-legacy-coordinates-specification.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To specify data as legacy coordinate pairs, you can use either an array (preferred) or an embedded document.

Array:

```javascript
  <field>: [ <x>, <y> ]

When you use longitude and latitude, list longitude first, then latitude:

.. code-block:: javascript

  <field>: [ <longitude>, <latitude> ]

.. include:: /includes/extracts/geospatial-valid-long-lat-values.rst
```

Embedded document:

```javascript
  <field>: { <field1>: <x>, <field2>: <y> }

If you use longitude and latitude, the first field must be longitude and
the second must be latitude:

.. code-block:: javascript

  <field>: { <field1>: <longitude>, <field2>: <latitude> }

.. include:: /includes/extracts/geospatial-valid-long-lat-values.rst
```

Use arrays for legacy coordinate pairs because some languages do not preserve object field ordering.
