---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/aggregation-examples/unpack-arrays.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================

# Unwind Arrays and Group Data

This tutorial illustrates how to construct an aggregation pipeline, perform the aggregation on a collection, and display the results using the language of your choice.

## About This Task

This tutorial demonstrates how to create insights from customer order data. The results show the list of products ordered that cost more than $15. Each document contains the number of units sold and the total sale value for each product.

The aggregation pipeline performs the following operations:

- Unwinds an array field into separate documents
- Matches a subset of documents by a field value
- Groups documents by common field values
- Adds computed fields to each result document
## Before You Begin

.. include:: /includes/language-or-shell-selector-instructions.rst

## Steps

The following steps demonstrate how to create and run an aggregation pipeline to unpack array fields into separate documents and compute new values based on groups of common values.
