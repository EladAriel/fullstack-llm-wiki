---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/reference/compatibility.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.823152Z"
---
**facet:** :name: programming_language
   :values: csharp, go, java, javascript/typescript, php, python, ruby, rust, scala

.. _qe-csfle-compatibility:
.. _qe-compatibility-reference:
.. _qe-driver-compatibility:
.. _csfle-compatibility-reference:
.. _csfle-driver-compatibility:
.. _csfle-reference-compatibility-key-rotation: 

# Compatibility

**meta:** :description: Determine compatibility of MongoDB editions and drivers with Queryable Encryption and Client-Side Field Level Encryption features.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

This page describes the MongoDB Server editions and driver versions
compatible with {+qe+} and {+csfle+} to help you determine whether
your deployment supports each in-use encryption feature.

Select your encryption feature and driver to see compatibility
requirements.

.. composable-tutorial::
   :options: encryption-feature, language-no-dependencies
   :defaults: qe, nodejs

   .. include:: /includes/queryable-encryption/qe-compat.rst

   .. include:: /includes/queryable-encryption/csfle-compat.rst