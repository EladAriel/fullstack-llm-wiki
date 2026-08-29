---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/UUID.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.960249Z"
---
# UUID() (mongosh method)

**meta:** :description: Generate a BSON UUID object using the `UUID()` method, optionally converting a 36-character string to a UUID.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

Generates a BSON :abbr:`UUID (Universally unique identifier)` object.

:method:`~UUID()` has the following syntax:

**method:** UUID(<string>)

   .. list-table::
      :header-rows: 1
      :widths: 20 20 80

      * - Parameter

        - Type

        - Description

      * - ``hex``

        - string

        - Optional. Specify a 36 character string to convert to a UUID BSON object. If
          not provided, MongoDB generates a random UUID in 
          `RFC 4122 v4 <https://tools.ietf.org/html/rfc4122>`_ format.

   :returns: A BSON UUID object.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst

## Example

### Convert Character String to UUID

Create a 36 character string you wish to convert to a UUID:

.. code-block:: javascript

   var myuuid = '3b241101-e2bb-4255-8caf-4136c566a962'

The following command outputs the ``myuuid`` variable as a BSON UUID object:

.. code-block:: javascript

   UUID(myuuid)

This command generates the following output:

.. code-block:: javascript

   UUID("3b241101-e2bb-4255-8caf-4136c566a962")

### Generate Random UUID

You can run the :method:`~UUID()` method without
specifying an argument to generate a random UUID:

.. code-block:: javascript

   UUID()

This command outputs a random UUID in the following form:

.. code-block:: javascript

   UUID("dee11d4e-63c6-4d90-983c-5c9f1e79e96c")