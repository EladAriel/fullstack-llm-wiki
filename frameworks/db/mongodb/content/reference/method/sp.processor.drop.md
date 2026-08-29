---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sp.processor.drop.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.965129Z"
---
# sp.processor.drop() (mongosh method)

**meta:** :description: Delete a named Stream Processor from the current Stream Processing Workspace using `sp.processor.drop()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

## Definition

**method:** sp.processor.drop()

**versionadded:** 7.0

   Deletes a named
   :atlas:`Stream Processor
   </atlas-sp/overview/#mongodb-expression-exp.Stream-Processor>` from
   the current :atlas:`Stream Processing Workspace
   </atlas-sp/overview/#mongodb-expression-exp.Stream-Processing-Instance>`.

## Compatibility

**include:** /includes/fact-environments-atlas-support-stream-processing-only.rst

## Syntax
   
The :method:`sp.processor.drop()` method has the following
syntax:

.. code-block:: json

   sp.processor.drop(
     {
       <options>
     }
   )


## Command Fields

``sp.processor.drop()`` takes a generic, optional ``<options>`` document 
whose fields are passed to the underlying drop command.

## Behavior

``sp.processor.drop()`` deletes the given named stream processor
from the current stream processing workspace. If you invoke this
command on a currently running stream processor, it stops that
processor before deleting it.

## Access Control

The user running ``sp.processor.drop()`` must have the
:atlasrole:`atlasAdmin` role.

## Example

The following example stops a stream processor named ``solarDemo``

.. code-block::
   :copyable: true

   sp.solarDemo.drop()


## Learn More

- :atlas:`Manage Stream Processors </atlas-sp/manage-stream-processor>`