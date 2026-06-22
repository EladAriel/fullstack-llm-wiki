---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/deploy-replica-set-with-keyfile-access-control.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================================

# Deploy Self-Managed Replica Set With Keyfile Authentication

## Overview

Enforcing access control on a `replica set` requires configuring:

- Security between members of the replica set using
`Internal Authentication<replica-set-security>`, and

- Security between connecting clients and the replica set using
`/core/authorization`.

For this tutorial, each member of the replica set uses the same internal authentication mechanism and settings.

Enforcing internal authentication also enforces user access control. To connect to the replica set, clients like :binary:`~bin.mongosh` need to use a `user account<authorization>`. See `security-repSetDeploy-access-control`.

### Cloud Manager and Ops Manager

If you are currently using or are planning to use Cloud Manager or Ops Manager, see the :mms-docs:`Cloud Manager manual </tutorial/edit-host-authentication-credentials>` or the :opsmgr:`Ops Manager manual </tutorial/edit-host-authentication-credentials>` for enforcing access control.

## Considerations

.. include:: /includes/important-hostnames.rst

### IP Binding

.. include:: /includes/extracts/default-bind-ip-security.rst

### Operating System

This tutorial primarily refers to the :binary:`~bin.mongod` process. Windows users should use the :binary:`mongod.exe` program instead.

### Keyfile Security

We recommend keyfiles only for testing and development environments, due to their limitations in manageability and cryptographic strength. For production environments, we strongly advise using `X.509 certificates<security-auth-x509>`. While keyfiles can be secure in specific, controlled scenarios, they present scalability and management challenges in complex deployments. X.509 certificates offer more robust security features, enable better key management, support individual authentication, and adhere to industry standards for sensitive data protection.

### Users and Authentication Mechanisms

.. include:: /includes/internal-authentication-tutorials-access-control-consideration.rst

## Deploy New Replica Set with Keyfile Access Control

.. include:: /includes/important-hostnames.rst

.. include:: /includes/steps/deploy-replica-set-with-auth.rst

## X.509 Internal Authentication

For details on using X.509 for internal authentication, see `/tutorial/configure-x509-member-authentication`.

To upgrade from keyfile internal authentication to X.509 internal authentication, see `/tutorial/upgrade-keyfile-to-x509`.
