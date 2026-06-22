---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/install-mongodb-enterprise-on-ubuntu.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# Install MongoDB Enterprise Edition on Ubuntu

.. include:: /includes/minor-release.rst

## Overview

Use this tutorial to install MongoDB {+version+} |edition| Edition on LTS (long-term support) releases of Ubuntu Linux using the |package-manager| package manager.

:products:`MongoDB Enterprise Edition</mongodb-enterprise-advanced>` is available on select platforms and contains support for features related to security and monitoring.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

## Considerations

### Platform Support

.. include:: /includes/fact-platform-support-enterprise-ubuntu.rst

### Production Notes

.. include:: /includes/fact-see-production-notes.rst

### Official MongoDB Packages

.. include:: /includes/important-dont-use-distro-packages.rst

See `ubuntu-enterprise-package-content` for the complete list of official packages.

## Install MongoDB Enterprise Edition

Follow these steps to install MongoDB |edition| Edition using the |package-manager| package manager.

.. include:: /includes/deploy/enterprise-ubuntu

> **Note:** .. include:: /includes/install-mongodb-apt-commands.rst

For help with troubleshooting errors encountered while installing MongoDB on Ubuntu, see our `troubleshooting <install-ubuntu-troubleshooting>` guide.

## Run MongoDB Enterprise Edition

.. include:: /includes/fact-installation-directories.rst

.. include:: /includes/fact-installation-ulimit.rst

### Procedure

Follow these steps to run MongoDB |edition| Edition on your system. These instructions assume that you are using the official |package-name| package, not the unofficial `mongodb` package provided by |distro-name|, and are using the default settings.

**Init System**

.. include:: /includes/fact-systemd-vs-initd.rst

## Uninstall MongoDB

.. include:: /includes/fact-uninstall.rst

.. include:: /includes/steps/uninstall-mongodb-enterprise-on-debian.rst

## Additional Information

### Upgrading MongoDB Enterprise Edition

When upgrading MongoDB |edition| Edition, ensure that you are using the `official packages <enterprise-official-packages>`. Specify the same version for each component as in this example:

```sh
VERSION=${VERSION} sudo apt install -y \
  mongodb-enterprise=${VERSION} \
  mongodb-enterprise-server=${VERSION} \
  mongodb-enterprise-mongos=${VERSION} \
  mongodb-enterprise-tools=${VERSION} \
  --allow-downgrades --allow-change-held-packages
```

### Localhost Binding by Default

.. include:: /includes/fact-installation-bind-ip-default-in-config.rst

### MongoDB Enterprise Edition Packages

.. include:: /includes/list-mongodb-enterprise-packages.rst

## Contents

- Install using .tgz Tarball </tutorial/install-mongodb-enterprise-on-ubuntu-tarball>
