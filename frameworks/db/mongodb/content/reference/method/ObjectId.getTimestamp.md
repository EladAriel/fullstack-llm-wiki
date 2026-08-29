---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ObjectId.getTimestamp.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.981682Z"
---
# ObjectId.getTimestamp() (mongosh method)

**meta:** :description: Retrieve the timestamp from an `ObjectId` using the `getTimestamp()` method, returning it as a Date object.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** ObjectId.getTimestamp()

   Returns the timestamp portion of the :method:`ObjectId()` as a Date.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst

## Example

The following example calls the :method:`getTimestamp()
<ObjectId.getTimestamp()>` method on an :method:`ObjectId()`:

.. code-block:: javascript

   ObjectId("507c7f79bcf86cd7994f6c0e").getTimestamp()

This will return the following output:

.. code-block:: javascript

   ISODate("2012-10-15T21:26:17Z")

**seealso:** :ref:`ObjectId BSON Type <objectid>`