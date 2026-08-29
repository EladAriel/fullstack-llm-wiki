---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/views/specify-collation.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.800482Z"
---
.. _manual-views-collation:
.. _create-view-w-collation:

# Create a View with Default Collation

**meta:** :description: Specify default collation for views to apply language-specific string comparison rules, affecting operations like counting documents.

:ref:`Collation <manual-collation>` allows you to specify
language-specific rules for string comparison, such as rules for
letter-case and accent marks.

This page explains how to specify a default collation for a view.

## Example

Create a ``places`` collection with the following documents:

.. code-block:: javascript

   db.places.insertMany([
      { _id: 1, category: "café" },
      { _id: 2, category: "cafe" },
      { _id: 3, category: "cafE" }
   ])

The following operation creates a view, specifying collation at the view
level:

.. code-block:: javascript

   db.createView(
      "placesView", 
      "places",
      [ { $project: { category: 1 } } ],
      { collation: { locale: "fr", strength: 1 } } 
   )

The following operation uses the view's collation:

.. code-block:: javascript

   db.placesView.countDocuments( { category: "cafe" } )

The operation returns ``3``.

**note:** Collation Behavior

   .. include:: /includes/extracts/views-collation-behavior.rst