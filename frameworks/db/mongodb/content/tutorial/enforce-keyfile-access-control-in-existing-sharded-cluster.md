---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/enforce-keyfile-access-control-in-existing-sharded-cluster.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================================

# Update Self-Managed Sharded Cluster to Keyfile Authentication

## Overview

Enforcing access control on a `sharded cluster` requires configuring:

- Security between components of the cluster using
`Internal Authentication<replica-set-security>`.

- Security between connecting clients and the cluster using
`/core/authorization`.

For this tutorial, each member of the sharded cluster must use the same internal authentication mechanism and settings. This means enforcing internal authentication on each :binary:`~bin.mongos` and :binary:`~bin.mongod` in the cluster.

The following tutorial uses a `keyfile <internal-auth-keyfile>` to enable internal authentication.

Enforcing internal authentication also enforces user access control. To connect to the replica set, clients like :binary:`~bin.mongosh` need to use a `user account<authorization>`. See `security-shardClust-enforce-access-control`.

### CloudManager and OpsManager

If Cloud Manager or Ops Manager is managing your deployment, internal authentication is automatically enforced.

To configure Access Control on a managed deployment, see: `Configure Access Control for MongoDB Deployments` in the :mms-docs:`Cloud Manager manual </tutorial/edit-host-authentication-credentials>` or in the :opsmgr:`Ops Manager manual </tutorial/edit-host-authentication-credentials>`.

## Considerations

.. include:: /includes/important-hostnames.rst

### IP Binding

.. include:: /includes/fact-default-bind-ip-change.rst

### Operating System

This tutorial primarily refers to the :binary:`~bin.mongod` process. Windows users should use the :binary:`mongod.exe` program instead.

### Keyfile Security

Keyfiles are bare-minimum forms of security and are best suited for testing or development environments. For production environments we recommend using `X.509 certificates<security-auth-x509>`.

### Access Control

.. include:: /includes/internal-authentication-tutorials-access-control-consideration.rst

### Users

.. include:: /includes/sharded-clusters-users.rst

See the `/core/security-users` security documentation for more information.

### Downtime

Upgrading a sharded cluster to enforce access control requires downtime.

## Before You Begin

.. include:: /includes/dSO-role-intro.rst

.. include:: /includes/dSO-warning.rst

## Procedures

### Enforce Keyfile Internal Authentication on Existing Sharded Cluster Deployment

.. include:: /includes/steps/enable-authentication-in-sharded-cluster.rst

## X.509 Internal Authentication

For details on using X.509 for internal authentication, see `/tutorial/configure-x509-member-authentication`.

To upgrade from keyfile internal authentication to X.509 internal authentication, see `/tutorial/upgrade-keyfile-to-x509`.

> **Seealso:** - `/core/sharded-cluster-components`
- `/core/sharded-cluster-requirements`
