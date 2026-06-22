---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/enforce-keyfile-access-control-in-existing-replica-set.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================================

# Update Self-Managed Replica Set to Keyfile Authentication

## Overview

Enforcing access control on an existing `replica set` requires configuring:

- Security between members of the replica set using
`Internal Authentication<replica-set-security>`, and

- Security between connecting clients and the replica set using
`User Access Controls<authorization>`.

For this tutorial, each member of the replica set uses the same internal authentication mechanism and settings.

Enforcing internal authentication also enforces user access control. To connect to the replica set, clients like :binary:`~bin.mongosh` need to use a `user account<authorization>`. See `security-replSet-auth-access-control`.

### Cloud Manager and Ops Manager

If Cloud Manager or Ops Manager is managing your deployment, see the :mms-docs:`Cloud Manager manual </tutorial/edit-host-authentication-credentials>` or the :opsmgr:`Ops Manager manual </tutorial/edit-host-authentication-credentials>` for enforcing access control.

## Considerations

.. include:: /includes/important-hostnames.rst

### IP Binding

.. include:: /includes/fact-default-bind-ip-change.rst

### Operating System

This tutorial uses the :binary:`~bin.mongod` programs. Windows users should use the :binary:`mongod.exe` program instead.

### Keyfile Security

Keyfiles are bare-minimum forms of security and are best suited for testing or development environments. For production environments we recommend using `X.509 certificates<security-auth-x509>`.

### Users

.. include:: /includes/internal-authentication-tutorials-access-control-consideration.rst

### Downtime

The following procedure for enforcing access control requires downtime. For a procedure that does not require downtime, see `/tutorial/enforce-keyfile-access-control-in-existing-replica-set-without-downtime` instead.

## Enforce Keyfile Access Control on Existing Replica Set

.. include:: /includes/steps/enable-authentication-in-replica-set.rst

## X.509 Internal Authentication

For details on using X.509 for internal authentication, see `/tutorial/configure-x509-member-authentication`.

To upgrade from keyfile internal authentication to X.509 internal authentication, see `/tutorial/upgrade-keyfile-to-x509`.
