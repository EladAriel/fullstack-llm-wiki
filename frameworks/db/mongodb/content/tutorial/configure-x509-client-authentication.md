---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-x509-client-authentication.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.643517Z"
---
.. _x509-client-authentication:

# Use X.509 to Authenticate Clients on Self-Managed MongoDB

**meta:** :description: Configure X.509 certificate authentication for client connections on a standalone `mongod` instance using command-line or configuration file options.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


The following procedure sets up X.509 certificate authentication for
client authentication on a standalone :binary:`~bin.mongod` instance.
This is also known as Mutual TLS or mTLS.

To use X.509 authentication for replica sets or sharded clusters, see
:doc:`/tutorial/configure-x509-member-authentication`.

## Prerequisites

**include:** /includes/extracts/security-prereq-configure-x509-client-authentication.rst


### Certificate Authority

**include:** /includes/fact-ssl-certificate-authorities.rst

**include:** /includes/extracts/ssl-facts-x509-ca-file.rst


### Client X.509 Certificate

You must have valid X.509 certificates. The client X.509 certificates
must meet the :ref:`client certificate requirements
<client-x509-certificates-requirements>`.

**include:** /includes/extracts/ssl-facts-x509-invalid-certificate.rst

## Procedure

**include:** /includes/steps/use-x509-authentication.rst

## Next Steps

To use X.509 authentication for replica sets or sharded clusters, see
:doc:`/tutorial/configure-x509-member-authentication`.