---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-x509-client-authentication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================================

# Use X.509 to Authenticate Clients on Self-Managed MongoDB

The following procedure sets up X.509 certificate authentication for client authentication on a standalone :binary:`~bin.mongod` instance. This is also known as Mutual TLS or mTLS.

To use X.509 authentication for replica sets or sharded clusters, see `/tutorial/configure-x509-member-authentication`.

## Prerequisites

.. include:: /includes/extracts/security-prereq-configure-x509-client-authentication.rst

### Certificate Authority

.. include:: /includes/fact-ssl-certificate-authorities.rst

.. include:: /includes/extracts/ssl-facts-x509-ca-file.rst

### Client X.509 Certificate

You must have valid X.509 certificates. The client X.509 certificates must meet the `client certificate requirements <client-x509-certificates-requirements>`.

.. include:: /includes/extracts/ssl-facts-x509-invalid-certificate.rst

## Procedure

.. include:: /includes/steps/use-x509-authentication.rst

## Next Steps

To use X.509 authentication for replica sets or sharded clusters, see `/tutorial/configure-x509-member-authentication`.
