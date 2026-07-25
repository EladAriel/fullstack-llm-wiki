---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/tls/configure-client-tls-tutorial.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

====================================

# Connect to a TLS-Enabled Replica Set

This tutorial shows you how to connect {+mongosh+} to a |tls|-enabled self-managed replica set.

## Before You Begin

Before you start, verify that you have the following:

- A replica set that you configured to use TLS using the steps
in `configure-server-tls-tutorial`.

- MongoDB access control enabled on your deployment and at least
one admin user created. To set up access control, see `enable-access-control`. This user must have `clusterMonitor` privileges.

- If you want to connect to your deployment using X.509 authentication,
ensure that you have OpenSSL installed to generate a client certificate.

- Access to {+mongosh+}.
## Steps

## Final Result

After completing this tutorial, `mongosh` is connected to your replica set over an encrypted TLS connection, authenticated with either SCRAM or X.509.

----------

certain protocols or certificate rotation and revocation, continue to the next page.
