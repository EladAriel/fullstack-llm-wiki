---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/stable-api-reference.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.714358Z"
---
# Migrate to a Later API Version

**meta:** :description: Upgrade your API version to access improved functionality and prepare for future MongoDB server versions.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


## Compatibility with Future Versions

The only API version that currently exists is ``"1"``, but there will 
be new API versions released in the future. Upgrading your API version
provides improved functionality and semantics for your application.

Some API V1 commands and behaviors will be deprecated in future 
versions of the MongoDB server. Deprecated commands and behaviors are 
typically not included in the next API version.

### Find Deprecated Commands and Behaviors

To migrate an existing application from API V1 to API V2, you must find 
and update all of the deprecated commands and behaviors features it 
uses.

.. code-block:: none

   client = MongoClient(
     <connection string>,
     api={"version": "1", "strict": True, "deprecationErrors": True}
   )

The returns a :ref:`APIDeprecationError <api-deprecation-resp>` if 
your application code tries to use commands and behaviors deprecated in 
API V1. Once your application tests pass and all deprecation errors 
have been fixed, you will be ready to test your application with API 
V2.