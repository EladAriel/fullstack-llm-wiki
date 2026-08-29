---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/overview-enable-qe.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.780815Z"
---
**facet:** :name: genre
   :values: reference

**meta:** :keywords: queryable encryption, in-use encryption

.. _qe-overview-enable-qe:

# Overview: Enable Queryable Encryption

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

This page summarizes the tasks required to set up your MongoDB
deployment and your development environment for {+qe+}.

## Enable {+qe+}

**procedure:** :style: normal

   .. step:: Install a compatible MongoDB driver and dependencies

      :ref:`Install a {+qe+} compatible driver and dependencies <qe-install>`
      
   .. step:: Install and configure a {+qe+} library

      :ref:`Install and configure a query analysis component <qe-csfle-install-library>`

   .. step:: Create a {+cmk-long+}

      :ref:`Create a {+cmk-long+} <qe-create-cmk>`

   .. step:: Create your {+qe+} enabled application

      :ref:`Create a {+qe+} enabled application <qe-create-application>`

## Use {+qe+}

After you install a {+qe+} driver and libraries, create a {+cmk-long+}, and
create your application, you can start encrypting and querying data. See
:ref:`Overview: Use {+qe+} <qe-overview-use-qe>` for instructions.

**toctree:** :titlesonly:

   Install a Driver </core/queryable-encryption/install>
   Install and Configure a Query Analysis Component </core/queryable-encryption/install-library>
   Create a Customer Master Key </core/queryable-encryption/qe-create-cmk>
   Create an Application  </core/queryable-encryption/qe-create-application>