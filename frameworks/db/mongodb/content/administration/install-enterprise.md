---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/install-enterprise.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# Install MongoDB Enterprise

.. include:: /includes/minor-release.rst

These documents provide instructions to install MongoDB Enterprise.

MongoDB Enterprise is available for MongoDB Enterprise subscribers and includes additional features such as LDAP authentication, Kerberos authentication, and System Event Auditing.

## Before You Begin

Before installing MongoDB Enterprise, confirm the following:

- You have a MongoDB Enterprise subscription. To learn more,
visit [MongoDB Enterprise Advanced](https://www.mongodb.com/products/mongodb-enterprise-advanced)_.

- Your host meets the platform and hardware requirements. For
details, see `production-notes`.

## Select Your Operating System

`Install on Linux <install-enterprise-linux>` Install the official builds of MongoDB Enterprise on Linux-based systems.

`Install on macOS <install-enterprise-macos>` Install the official build of MongoDB Enterprise on macOS

`Install on Windows <install-enterprise-windows>` Install MongoDB Enterprise on Windows using the `.msi` installer.

`Install with Docker <docker-mdb-enterprise-install>` Install a MongoDB Enterprise Docker container.

## Next Steps

After you install MongoDB Enterprise, you can:

- **Get started**: Work through an introductory tutorial. To
learn more, see `getting-started`.

- **Deploy a replica set**: Set up replication for high
availability. To learn how, see `server-replica-set-deploy`.

- **Set up access control**: Secure your deployment with
authentication. To learn how, see `enable-access-control`.

- **Review the security checklist**: Confirm your deployment
follows security best practices. To learn more, see `security-checklist`.

> **Note:** MongoDB Search and MongoDB Vector Search are available as Public Preview
features for your Enterprise clusters through MongoDB Controllers for
Kubernetes. To learn more, see `Deploy Search and Vector Search with
MongoDB
<https://www.mongodb.com/docs/kubernetes/current/fts-vs-deployment/>`__.

## Contents

- Install on Linux </administration/install-enterprise-linux>
- Install on macOS </tutorial/install-mongodb-enterprise-on-os-x>
- Install on Windows </tutorial/install-mongodb-enterprise-on-windows>
- Install with Docker </tutorial/install-mongodb-enterprise-with-docker>
