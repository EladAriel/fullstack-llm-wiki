---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-scram-client-authentication.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================================================

# Use SCRAM to Authenticate Clients on Self-Managed Deployments

The following procedure sets up SCRAM for client authentication on a standalone :binary:`~bin.mongod` instance.

To use SCRAM authentication for replica sets or sharded clusters, see `/tutorial/deploy-replica-set-with-keyfile-access-control`.

> **Important:** .. include:: /includes/security/fact-no-dual-auth-with-scram.rst

## Procedure

.. include:: /includes/steps/create-admin-then-enable-authentication.rst

## Next Steps

To use SCRAM authentication for replica sets or sharded clusters, see `/tutorial/deploy-replica-set-with-keyfile-access-control`.
