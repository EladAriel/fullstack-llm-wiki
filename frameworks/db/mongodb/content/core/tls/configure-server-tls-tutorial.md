---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/tls/configure-server-tls-tutorial.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================================

# Configure TLS on Self-Managed Deployments

This tutorial shows you how to configure |tls| on a self-managed replica set. Select an approach based on whether you want to use intra-cluster :abbr:`mTLS (Mutual TLS)`, which is required to enable X.509 authentication between nodes.

.. include:: /includes/tls/note-self-managed-only.rst

## Before You Begin

Before you start, verify that you have the following:

- A self-managed replica set in which each node has a hostname, such as
`localhost` or `mongo0.example.com`. TLS is not currently configured on any node in the replica set.

- TLS server certificates for each node that you obtained by following the
`Obtain Server Certificates <tls-certificate-tutorial>` tutorial, such as `mongo0.pem`.

- A CA certificate to sign the server certificates, such as `ca.pem`.
- Access to the |mongod| configuration file on each node.
- Access to {+mongosh+}.
## Steps

## Next Steps

To learn how to connect to your deployment with a client application, continue to `configure-client-tls-tutorial`.
