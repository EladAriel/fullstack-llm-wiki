---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/applications/data-models-applications.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.726656Z"
---
.. _data-models-application-context:
.. _data-modeling-examples:

# Model Specific Application Contexts

**meta:** :description: Explore methods for modeling application-specific data contexts, including atomic updates, keyword searches, monetary data, and IoT data in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

:doc:`/tutorial/model-data-for-atomic-operations`
   Illustrates how embedding fields related to an atomic update
   within the same document ensures that the fields are in sync.

:doc:`/tutorial/model-data-for-keyword-search`
   Describes one method for supporting keyword search by storing
   keywords in an array in the same document as the text field.
   Combined with a multi-key index, this pattern can support
   application's keyword search operations.

:doc:`/tutorial/model-monetary-data`
   Describes two methods to model monetary data in MongoDB.

:doc:`/tutorial/model-iot-data`
   Describes how to deal with IoT data in MongoDB.

**toctree:** :titlesonly: 
   :hidden: 

   Atomic Operations </tutorial/model-data-for-atomic-operations>
   IOT Data </tutorial/model-iot-data>
   Keyword Search </tutorial/model-data-for-keyword-search>
   Monetary Data </tutorial/model-monetary-data>