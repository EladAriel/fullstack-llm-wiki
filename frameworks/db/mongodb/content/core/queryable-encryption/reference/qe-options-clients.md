---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/reference/qe-options-clients.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.823420Z"
---
**facet:** :name: programming_language
   :values: csharp, go, java, javascript/typescript, python, shell

**meta:** :keywords: code example, node.js, compass
   :description: Explore configuration options for `MongoClient` instances to enable Queryable Encryption, including automatic encryption settings and key management.

.. _qe-reference-mongo-client:

# MongoClient Options for {+qe+}

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

## Overview

On this page, you can learn about the {+qe+}-specific configuration options for
``MongoClient`` instances.

## Automatic Encryption Options

.. tabs-selector:: drivers

**include:** /includes/queryable-encryption/automatic-enc-options/tabs.rst
