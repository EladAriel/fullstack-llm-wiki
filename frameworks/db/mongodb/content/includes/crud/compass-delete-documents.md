---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/crud/compass-delete-documents.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This page uses `MongoDB Compass <compass-index>` to delete the documents.

Populate the `inventory` collection with the following documents:

```javascript
[
    { "item": "journal", "qty": 25, "size": { "h": 14, "w": 21, "uom": "cm" }, "status": "A" },
    { "item": "notebook", "qty": 50, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "P" },
    { "item": "paper", "qty": 100, "size": { "h": 8.5, "w": 11, "uom": "in" }, "status": "D" },
    { "item": "planner", "qty": 75, "size": { "h": 22.85, "w": 30, "uom": "cm" }, "status": "D" },
    { "item": "postcard", "qty": 45, "size": { "h": 10, "w": 15.25, "uom": "cm" }, "status": "A" }
]
```

For instructions on inserting documents in MongoDB Compass, see `Insert Documents <write-op-insert>`.

> **Note:** For complete reference on inserting documents in MongoDB Compass,
see the `Compass documentation <compass-insert-documents>`.

## Delete All Documents

To delete all documents from a collection, click the :guilabel:`DELETE` button under the :guilabel:`Documents` tab.

.. include:: /includes/fact-delete-all-inventory.rst

.. figure:: /images/compass-delete-all.png

When you confirm the deletion in the pop-up window that appears after you click :guilabel:`DELETE`, MongoDB Compass deletes all documents and displays a message indicating how many documents were deleted.

## Delete All Documents that Match a Condition

.. include:: /includes/fact-delete-condition-inventory.rst

To specify equality conditions, use `<field>:<value>` expressions in the `query filter document <document-query-filter>`:

```javascript
{ <field1>: <value1>, ... }
```

A `query filter document <document-query-filter>` can use the `query operators <query-selectors>` to specify conditions in the following form:

```javascript
{ <field1>: { <operator1>: <value1> }, ... }
```

To delete all documents that match a deletion criteria, write your query filter in the Compass query bar, then click the :guilabel:`DELETE` button under the :guilabel:`Documents` tab. The following example deletes all documents where `{ status: "A" }`:

.. figure:: /images/compass-delete-filter.png

When you confirm the deletion in the pop-up window that appears after you click :guilabel:`DELETE`, MongoDB Compass deletes all documents and displays a message indicating how many documents were deleted.

## Delete Only One Document that Matches a Condition

To delete a single document that matches a specified filter:

1. Write your query filter in the Compass query bar and click
:guilabel:`Find`. #. Hover your mouse over the document you want to delete. #. Click the :icon-lg:`Trash` button on the right side of your document.

The following example deletes a document with `{ status: "A" }` from the `inventory` collection:

.. figure:: /images/compass-delete-one.png

> **Seealso:** - :compass:`Compass Documents </documents/>`
- `Compass Query Bar <compass-query-bar>`
