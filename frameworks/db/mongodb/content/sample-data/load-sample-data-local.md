---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/sample-data/load-sample-data-local.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================================

# Load Sample Data Into A Local Deployment

## About this Task

Estimated completion time: 5 minutes

Use this tutorial to load sample data into your self-managed MongoDB deployment.

## Before You Begin

To utilize the sample data that MongoDB provides, you must first create a deployment to load data into. To create a self-managed local deployment, see `configuration-file`.

To load sample data, you must also have a minimum of :authrole:`readWrite` access to the deployment. For more information on user administration, see `manage-users-and-roles`.

## Steps

To load sample data into your local deployment:

.. include:: /includes/steps-load-sample-data-local.rst

## Learn More

You can also generate synthetic data that aligns to your real data's schema. To learn more, see `synthetic-data`.

To import your own data, see `import-strategies`.
