---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.listConnections.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.925623Z"
---
# sp.listConnections() (mongosh method)

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

## Definition

**method:** sp.listConnections()

   Returns documents for each connection in the connection registry of
   the current :atlas:`stream processing workspace
   </atlas-sp/manage-processing-instance>`. Each document provides
   descriptive information including the name and type of each
   connection.

   .. include:: /includes/stream-processing-command-reqs.rst

## Syntax
   
The :method:`sp.listConnections()` method has the following syntax:

.. code-block:: json

   sp.listConnections()


## Command Fields

``sp.listConnections()`` takes no fields.

## Behavior

``sp.listConnections()`` returns documents describing all of the
connections in the connection registry of the current stream
processing workspace to the shell.

## Access Control

The user running ``sp.listConnections()`` must have the
:atlasrole:`atlasAdmin` role.

## Example

The following example shows an expected response from
``sp.listConnections()``:

.. io-code-block::
   :copyable: true

   .. input:: 
      :language: sh

      sp.listStreamProcessors()

   .. output:: 
      :language: json
      :linenos:

      {
	ok: 1,
	connections: [
	  { name: 'vt', type: 'atlas', cluster: 'versiontest' },
	  { name: 'testkafka', type: 'kafka' },
	  { name: 'sample_stream_solar', type: 'inmemory' },
	  { name: 'jsncluster0', type: 'atlas', cluster: 'jsncluster0' }
	]
      } 

## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-processing-instance>`