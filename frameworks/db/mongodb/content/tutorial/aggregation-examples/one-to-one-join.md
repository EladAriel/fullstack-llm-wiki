---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/aggregation-examples/one-to-one-join.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.852546Z"
---
.. _agg-example-join-one-to-one:

# Perform One-to-One Joins

**facet:** :name: genre
   :values: tutorial

**meta:** :keywords: code example

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

This tutorial illustrates how to construct an aggregation pipeline,
perform the aggregation on a collection, and display the results using
the language of your choice.

.. composable-tutorial::
   :options: language-no-dependencies
   :defaults: shell

## About This Task

   This tutorial demonstrates how to combine data from a collection that
   describes product information with another collection that describes
   customer orders. The results show a list of all orders placed in 2020
   and includes the product details associated with each order.

   This aggregation performs a one-to-one join. A one-to-one join occurs
   when a document in one collection has a field value that matches a
   single document in another collection that has the same field value. The
   aggregation matches these documents on the field value and combines
   information from both sources into one result.

   .. note::

      A one-to-one join does not require the documents to have a one-to-one
      relationship. To learn more about this data relationship,
      see the Wikipedia entry about :wikipedia:`One-to-one (data model)
      <w/index.php?title=One-to-one_(data_model)&oldid=1096960092>`.

## Before You Begin

   .. selected-content::
      :selections: shell

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/mongosh-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: python

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/python-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: java-sync

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/java-sync-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: kotlin-coroutine

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/kotlin-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: scala

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/scala-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: csharp

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/csharp-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: c

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/c-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: cpp

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/cpp-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: nodejs

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/nodejs-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: php

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/php-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: ruby

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/ruby-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: go

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/golang-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps

   .. selected-content::
      :selections: rust

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/rust-one-to-one-join.rst
         :start-after: start-prep-steps
         :end-before: end-prep-steps


## Steps

   The following steps demonstrate how to create and run an aggregation
   pipeline to join collections on a single common field.

   .. selected-content::
      :selections: shell

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/mongosh-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: python

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/python-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: java-sync

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/java-sync-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: kotlin-coroutine

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/kotlin-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: scala

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/scala-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: csharp

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/csharp-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: c

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/c-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: cpp

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/cpp-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: nodejs

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/nodejs-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: php

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/php-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: ruby

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/ruby-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: go

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/golang-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial

   .. selected-content::
      :selections: rust

      .. include:: /includes/aggregation/aggregation-examples/one-to-one-join/rust-one-to-one-join.rst
         :start-after: start-tutorial
         :end-before: end-tutorial
