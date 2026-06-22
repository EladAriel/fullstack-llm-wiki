---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/oidc/workload/workload-external-provider.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# Configure Workload Identity Federation

To configure Workload Identity Federation using OAuth 2.0, register your OAuth 2.0 application with an external |idp| like Microsoft Azure or Google Cloud Platform (GCP). This enables secure authentication and streamlines user management.

## About this Task

Workload Identity Federation uses OAuth2.0 access tokens. These tokens can be issued by any external |idp|.

The following procedures configure Microsoft Azure Entra ID and Google Cloud Platform as external |idps| for MongoDB.

## Before you Begin

- To use Microsoft Azure as an |idp|, you must have a `Microsoft
Azure account <https://azure.microsoft.com/en-us/get-started/azure-portal>`__.

- To use Google Cloud as an |idp|, you must have a `Google
Cloud account <https://cloud.google.com>`__.

.. NOTE TO WRITERS: Material on this page is based on https://github.com/10gen/cloud-docs/blob/master/source/workload-oidc.txt or https://www.mongodb.com/docs/atlas/workload-oidc/ on the Atlas Docs site.

There are some small changes between docs to make them Atlas/self-managed specific.

If you update the procedures on this page, make sure the changes are also made to the source docs.

## Steps
