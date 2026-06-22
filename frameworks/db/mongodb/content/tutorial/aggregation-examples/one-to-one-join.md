---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/aggregation-examples/one-to-one-join.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Perform One-to-One Joins

This tutorial illustrates how to construct an aggregation pipeline, perform the aggregation on a collection, and display the results using the language of your choice.

## About This Task

This tutorial demonstrates how to combine data from a collection that describes product information with another collection that describes customer orders. The results show a list of all orders placed in 2020 and includes the product details associated with each order.

This aggregation performs a one-to-one join. A one-to-one join occurs when a document in one collection has a field value that matches a single document in another collection that has the same field value. The aggregation matches these documents on the field value and combines information from both sources into one result.

> **Note:** A one-to-one join does not require the documents to have a one-to-one
relationship. To learn more about this data relationship,
see the Wikipedia entry about :wikipedia:`One-to-one (data model)
<w/index.php?title=One-to-one_(data_model)&oldid=1096960092>`.

## Before You Begin

.. include:: /includes/language-or-shell-selector-instructions.rst

## Steps

The following steps demonstrate how to create and run an aggregation pipeline to join collections on a single common field.
