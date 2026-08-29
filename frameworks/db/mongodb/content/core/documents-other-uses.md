---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/documents-other-uses.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.509510Z"
---
.. _documents-other-uses:

# Document Structure Use Cases

.. default-domain:: mongodb

**meta:** :keywords: documents, specification documents
   :description: Other uses of the MongoDB document structure.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

In addition to defining data records, MongoDB uses the document
structure throughout, including but not limited to: :ref:`query filters
<document-query-filter>`, :ref:`update specifications documents
<document-update-specification>`, and :ref:`index specification
documents <document-index-specification>`

.. _document-query-filter:

### Query Filter Documents

Query filter documents specify the conditions that determine which
records to select for read, update, and delete operations.

You can use ``<field>:<value>`` expressions to specify the equality
condition and :ref:`query operator <query-projection-operators-top>`
expressions.

.. code-block:: javascript

   {
     <field1>: <value1>,
     <field2>: { <operator>: <value> },
     ...
   }

For examples, see:

- :doc:`/tutorial/query-documents`

- :doc:`/tutorial/query-embedded-documents`

- :doc:`/tutorial/query-arrays`

- :doc:`/tutorial/query-array-of-documents/`

.. _document-update-specification:

### Update Specification Documents

Update specification documents use :ref:`update operators
<update-operators>` to specify the data modifications to perform on
specific fields during an update operation.

.. code-block:: javascript

   {
     <operator1>: { <field1>: <value1>, ... },
     <operator2>: { <field2>: <value2>, ... },
     ...
   }


For examples, see :ref:`Update specifications
<update-documents-modifiers>`.

.. _document-index-specification:

### Index Specification Documents

Index specification documents define the field to index and the index
type:

.. code-block:: javascript

   { <field1>: <type1>, <field2>: <type2>, ...  }