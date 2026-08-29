---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.startAutoMerger.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.918582Z"
---
# sh.startAutoMerger() (mongosh method)

**meta:** :description: Enable the AutoMerger in MongoDB deployments to automate chunk merging with configurable time intervals.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.startAutoMerger()

**versionadded:** 7.0

**include:** /includes/startAutoMerger.rst

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

.. code-block:: javascript

   sh.startAutoMerger()

## Behavior

**include:** /includes/auto-merger-time-parameters.rst

## Example

The following example enables the {+auto-merge-upper+}. Run the example 
from :binary:`~bin.mongos`:

.. code-block:: javascript

   sh.startAutoMerger()

## Learn More

- :ref:`automerger-concept`
- :method:`sh.stopAutoMerger()` method
- :method:`sh.enableAutoMerger()` method
- :method:`sh.disableAutoMerger()` method

**include:** /includes/auto-merger-learn-more.rst