---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/sample-data/load-sample-data-local.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.727771Z"
---
.. _load-sample-data-local:

# Load Sample Data Into A Local Deployment

**facet:** :name: genre
   :values: tutorial

**meta:** :description: Load sample datasets into your self-managed, local MongoDB deployment so you can experiment with real-world data and explore MongoDB features and tools.
   :keywords: atlas cli, sample dataset, atlas ui

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## About this Task

*Estimated completion time: 5 minutes*

Use this tutorial to load sample data into your self-managed
MongoDB deployment.

## Before You Begin

To utilize the sample data that MongoDB provides, you must first create a
deployment to load data into. To create a self-managed local deployment, see
:ref:`configuration-file`.

To load sample data, you must also have a minimum of 
:authrole:`readWrite` access to the deployment. For more information on user
administration, see :ref:`manage-users-and-roles`. 

.. _sample-dataset-local:

## Steps

To load sample data into your local deployment: 

**include:** /includes/steps-load-sample-data-local.rst

## Learn More
      
You can also generate synthetic data that aligns to your real data's
schema. To learn more, see :ref:`synthetic-data`.

To import your own data, see :ref:`import-strategies`.
      