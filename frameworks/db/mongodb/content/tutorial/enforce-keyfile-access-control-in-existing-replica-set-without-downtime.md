---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/enforce-keyfile-access-control-in-existing-replica-set-without-downtime.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# Update Self-Managed Replica Set (No Downtime)

## Overview

To secure against unauthorized access, enforce `authentication <authentication>` for your deployments. Authentication for replica sets consists of `internal authentication <inter-process-auth>` among the replica set members, and `user access control <authorization>` for clients connecting to the replica set.

If your deployment does not currently enforce authentication, you can use the :option:`--transitionToAuth <mongod --transitionToAuth>` option to enforce authentication without downtime.

This tutorial uses the `keyfile <internal-auth-keyfile>` internal authentication mechanism for internal security, and `authentication-scram`-based `role-based access controls <authorization>` for client connections.

### Cloud Manager and Ops Manager

If you are using Cloud Manager or Ops Manager to manage your deployment, see the respective :mms-docs:`Cloud Manager manual </tutorial/edit-host-authentication-credentials>` or the :opsmgr:`Ops Manager manual </tutorial/edit-host-authentication-credentials>` to enforce authentication.

### Architecture

This tutorial assumes that your replica set can elect a new `primary` after stepping down the existing primary replica set member. This requires:

- A majority of voting replica set members available after stepping down the
`primary`.

- At least one `secondary` member that is not :ref:`delayed
<replica-set-delayed-members>`, `hidden <replica-set-hidden-members>`, or `Priority 0 <replica-set-secondary-only-members>`.

### Transition State

A :binary:`~bin.mongod` running with :option:`--transitionToAuth <mongod --transitionToAuth>` accepts both authenticated and non-authenticated connections. Clients connected to the :binary:`~bin.mongod` during this transition state can perform read, write, and administrative operations on any database.

### Client Access

At the end of the following procedure, the replica set rejects any client attempting to make a non-authenticated connection. The procedure creates `users <users>` for client applications to use when connecting to the replica set.

See `security-checklist-role-based-access-control` for user creation and management best practices.

### IP Binding

.. include:: /includes/fact-default-bind-ip-change.rst

### Passwords

> **Important:** Passwords should be random, long, and complex to ensure system
security and to prevent or delay malicious access.

## Enforce Keyfile Access Control on Existing Replica Set

.. include:: /includes/important-hostnames.rst

.. include:: /includes/steps/enable-authentication-in-replica-set-no-downtime.rst

## X.509 Internal Authentication

For details on using X.509 for internal authentication, see `/tutorial/configure-x509-member-authentication`.

To upgrade from keyfile internal authentication to X.509 internal authentication, see `/tutorial/upgrade-keyfile-to-x509`.
