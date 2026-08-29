---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-scram-client-authentication.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.633042Z"
---
.. _scram-client-authentication:

# Use SCRAM to Authenticate Clients on Self-Managed Deployments

**meta:** :description: Set up SCRAM authentication for client access on a standalone `mongod` instance, including user creation and enabling access control.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The following procedure sets up SCRAM for client authentication on a
standalone :binary:`~bin.mongod` instance.

To use SCRAM authentication for replica sets or sharded clusters, see
:doc:`/tutorial/deploy-replica-set-with-keyfile-access-control`.

**important:** .. include:: /includes/security/fact-no-dual-auth-with-scram.rst

.. _enable-auth-procedure:

## Procedure

**include:** /includes/steps/create-admin-then-enable-authentication.rst

## Next Steps

To use SCRAM authentication for replica sets or sharded clusters, see
:doc:`/tutorial/deploy-replica-set-with-keyfile-access-control`.