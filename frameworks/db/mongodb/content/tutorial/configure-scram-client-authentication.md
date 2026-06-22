---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-scram-client-authentication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
