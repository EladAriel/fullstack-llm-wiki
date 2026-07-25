---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-x.509.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====

# x.509

MongoDB supports X.509 certificate authentication for client authentication and internal authentication of the members of replica sets and sharded clusters.

X.509 certificate authentication requires a secure `TLS/SSL connection </tutorial/configure-ssl>`.

## Certificate Authority

.. include:: /includes/fact-ssl-certificate-authorities.rst

## Client X.509 Certificates

To authenticate to servers, clients can use X.509 certificates instead of usernames and passwords.

### Client Certificate Requirements

.. include:: /includes/extracts/x509-certificate-client.rst

### MongoDB User and `$external` Database

To authenticate with a client certificate, you must first add the client certificate's `subject` as a MongoDB user in the `$external` database. The `$external` database is the `authentication-database` for the user.

Each unique X.509 client certificate is for one MongoDB user. You cannot use a single client certificate to authenticate more than one MongoDB user.

.. include:: /includes/extracts/sessions-external-username-limit.rst

### TLS Connection X509 Certificate Startup Warning

.. include:: /includes/fact-5.0-x509-certificate-client-warning.rst

## Member X.509 Certificates

For internal authentication between members of sharded clusters and replica sets, you can use X.509 certificates instead of `keyfiles </tutorial/deploy-sharded-cluster-with-keyfile-access-control>`.

### Member Certificate Requirements

.. include:: /includes/extracts/x509-certificate-member.rst

### MongoDB Configuration for Membership Authentication

.. include:: /includes/extracts/x509-member-auth-configuration.rst

## Contents

- Authenticate Clients </tutorial/configure-x509-client-authentication>
