---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.disableBlockWarnings.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.887166Z"
---
# cursor.disableBlockWarnings() (mongosh method)

**meta:** :description: Use ``disableBlockWarnings()`` to silence warnings printed when using blocking calls on cursors, such as ``.next()`` or ``.hasNext()`` on change streams.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** cursor.disableBlockWarnings()


   .. include:: /includes/fact-mongosh-shell-method.rst

   Use the ``disableBlockWarnings()`` cursor option to silence warnings
   that ``mongosh`` prints when you run blocking calls on cursors, such
   as ``.next()`` or ``.hasNext()`` on change streams and tailable
   cursors.

## Syntax

.. code-block:: javascript
   
   db.<collection>.find(<match document>).disableBlockWarnings()

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst

## Example

The following example silences warnings on a tailable cursor that is
stored in a variable called ``myTailableCursor``:

.. code-block:: javascript

   myTailableCursor.disableBlockWarnings()