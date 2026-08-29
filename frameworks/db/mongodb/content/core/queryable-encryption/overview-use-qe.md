---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/overview-use-qe.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.781081Z"
---
**facet:** :name: genre
   :values: reference

**meta:** :keywords: queryable encryption, in-use encryption

.. _qe-overview-use-qe:

# Overview: Use Queryable Encryption

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

This page summarizes the tasks required to create a {+qe+}-enabled
collection, insert a document with encrypted fields, and query encrypted
data.

## Enable {+qe+}

Before encrypting and querying data, you must install a {+qe+}-enabled driver
and libraries, create a {+cmk-long+}, and create your application. See
:ref:`Overview: Enable {+qe+} <qe-overview-enable-qe>` for instructions.

## Use {+qe+}

**procedure:** :style: normal
      
   .. step:: Create an encrypted collection and insert a document with encrypted fields

      :ref:`Create an encrypted collection and insert documents <qe-create-encrypted-collection>`

   .. step:: Query a document with encrypted fields

      :ref:`Query a document with encrypted fields <qe-query-encrypted-document>`

**toctree:** :titlesonly:

   Create a Collection </core/queryable-encryption/qe-create-encrypted-collection>
   Query </core/queryable-encryption/qe-retrieve-encrypted-document>