---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/aggregation-examples/multi-field-join.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================

# Perform Multi-Field Joins

This tutorial illustrates how to construct an aggregation pipeline, perform the aggregation on a collection, and display the results using the language of your choice.

## About This Task

This tutorial demonstrates how to combine data from a collection that describes product information with another collection that describes customer orders. The results show a list of products ordered in 2020 and details about each order.

This aggregation performs a multi-field join by using :pipeline:`$lookup`. A multi-field join occurs when there are multiple corresponding fields in the documents of two collections. The aggregation matches these documents on the corresponding fields and combines information from both into one document.

## Before You Begin

.. include:: /includes/language-or-shell-selector-instructions.rst

## Steps

The following steps demonstrate how to create and run an aggregation pipeline to join collections on multiple fields.
