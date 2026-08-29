---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/text-search-languages.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.715369Z"
---
.. _text-search-languages:

# $text Query Languages on Self-Managed Deployments

.. default-domain:: mongodb

**meta:** :keywords: on-prem
   :description: Explore $text query capabilities for self-managed MongoDB deployments using various languages with ISO 639-1 codes.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**include:** /includes/fact-fts-language-analyzers.rst

The :ref:`text index <index-type-text>` and the :query:`$text`
operator may be used with the following languages, and accepts either the
two-letter ISO 639-1 language code or the long form of the
language name:

.. list-table::
   :header-rows: 1

   * - Language Name
     - ISO 639-1 (Two letter codes)

   * - ``danish``
     - ``da``

   * -  ``dutch``
     - ``nl``

   * - ``english``
     - ``en``

   * - ``finnish``
     - ``fi``

   * - ``french``
     - ``fr``

   * - ``german``
     - ``de``

   * - ``hungarian``
     - ``hu``

   * - ``italian``
     - ``it``

   * - ``norwegian``
     - ``nb``

   * - ``portuguese``
     - ``pt``

   * - ``romanian``
     - ``ro``

   * - ``russian``
     - ``ru``

   * - ``spanish``
     - ``es``

   * - ``swedish``
     - ``sv``

   * - ``turkish``
     - ``tr``

.. |text-obj| replace:: text search

**include:** /includes/fact-text-search-language-none.rst

**seealso:** :doc:`/core/indexes/index-types/index-text/specify-text-index-language`
