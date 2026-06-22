---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-x509-member-authentication.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================================

# Verify Cluster Membership with X.509 on Self-Managed MongoDB

MongoDB supports X.509 certificate authentication for use with a secure `TLS/SSL connection <configure-mongod-mongos-for-tls-ssl>`. Sharded cluster members and replica set members can use X.509 certificates to verify their membership to the cluster or the replica set instead of using `keyfiles <internal-auth-keyfile>`. The membership authentication is an internal process.

> **Note:** .. include:: /includes/fact-tls-1.0.rst

Enabling internal authentication also enables `/core/authorization`. Clients must authenticate as a user in order to connect and perform operations in the deployment.

- See the `/tutorial/manage-users-and-roles` tutorial for
instructions on adding users to the deployment.

- See the `/tutorial/configure-x509-client-authentication` tutorial
for instructions on using X.509 certificates for user authentication.

> **Important:** .. include:: /includes/extracts/security-prereq-configure-x509-member-authentication.rst

## Member X.509 Certificate

> **Note:** You must have valid X.509 certificates.
.. include:: /includes/extracts/ssl-facts-x509-invalid-certificate.rst

### Certificate Requirements

.. include:: /includes/extracts/x509-certificate-member.rst

## Configure Replica Set/Sharded Cluster

Outside of rolling upgrade procedures, every component of a `replica set` or `sharded cluster` should use the same `--clusterAuthMode` setting to ensure it can securely connect to all other components in the deployment.

For `replica set` deployments, this includes all :binary:`~bin.mongod` members of the replica set.

For `sharded cluster` deployments, this includes all :binary:`~bin.mongod` or :binary:`~bin.mongos` instances.

> **Note:** .. include:: /includes/extracts/default-bind-ip-security.rst

### Use Command-line Options (`tls`)

> **Note:** The procedures in this section use the `tls` settings/option. For
procedures using the deprecated `ssl` aliases, see
`configure-member-ssl`.
The `tls` settings/options provide **identical** functionality
as the `ssl` options since MongoDB has always supported TLS 1.0
and later.

For more information, see `/tutorial/configure-ssl`.

### Use Command-line Options (`ssl`)

> **Note:** The procedures in this section use the deprecated `ssl` settings/option.
For procedures that use `tls` aliases, see `configure-member-tls`.
The `tls` settings/options provide **identical** functionality
as the `ssl` options since MongoDB has always supported TLS 1.0
and later.

For more information, see `/tutorial/configure-ssl`.

## Additional Information

To upgrade from keyfile internal authentication to X.509 internal authentication, see `/tutorial/upgrade-keyfile-to-x509`.

To perform a rolling update of the certificates to new certificates with different `DN`, see `/tutorial/rotate-x509-membership-certificates`.
