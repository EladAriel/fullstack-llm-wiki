---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/install-mongodb-enterprise-on-red-hat-tarball.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================================

# Install MongoDB Enterprise on Red Hat or CentOS (.tgz)

.. include:: /includes/minor-release.rst

## Overview

Use this tutorial to manually install MongoDB {+version+} |edition| Edition on Red Hat Enterprise Linux, CentOS Linux, or Oracle Linux [#oracle-linux]_ using a downloaded `.tgz` tarball.

:products:`MongoDB Enterprise Edition</mongodb-enterprise-advanced>` is available on select platforms and contains support for several features related to security and monitoring.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

### Installation Method

.. include:: /includes/fact-use-package-manager.rst

|arrow| See `Install MongoDB using the yum Package Manager<install-mdb-enterprise-redhat-centos>` for instructions.

## Considerations

### MongoDB Shell, `mongosh`

.. include:: /includes/fact-have-to-install-mongosh-tgz.rst

### Platform Support

.. include:: /includes/fact-platform-support-enterprise-red-hat.rst

### Production Notes

.. include:: /includes/fact-see-production-notes.rst

## Install MongoDB Enterprise Edition

### Prerequisites

.. include:: /includes/fact-tarball-dependencies.rst

.. include:: /includes/deploy/enterprise-prereq-rhel.rst

### Procedure

Follow these steps to manually install MongoDB |edition| Edition from the `.tgz`.

.. include:: /includes/deploy/install-tar.rst

## Run MongoDB Enterprise Edition

### ulimit

.. include:: /includes/fact-installation-ulimit.rst

### Directory Paths

To Use Default Directories ``````````````````````````

By default, MongoDB runs using the |mongod-user| user account and uses the following default directories:

- |mongod-datadir| (the data directory)
- `/var/log/mongodb` (the log directory)
Create the MongoDB data and log directories:

```bash
sudo mkdir -p /var/lib/mongo
sudo mkdir -p /var/log/mongodb
```

By default, MongoDB runs using the |mongod-user| user account. Create a |mongod-user| and a `mongodb` group. Ensure that the |mongod-user| belongs to the group then set the owner and group of these directories to |mongod-user|:

```bash
sudo chown -R mongod:mongod /var/lib/mongo
sudo chown -R mongod:mongod /var/log/mongodb
```

To Use Non-Default Directories ``````````````````````````````

To use a data directory and/or log directory other than the default directories:

#. Create the new directory or directories.

#. Edit the configuration file `/etc/mongod.conf` and modify the following fields accordingly:

- :setting:`storage.dbPath` to specify a new data directory path (e.g. `/some/data/directory`)
- :setting:`systemLog.path` to specify a new log file path (e.g. `/some/log/directory/mongod.log`)
#. Ensure that the user running MongoDB has access to the directory or directories:

```bash
   sudo chown -R mongod:mongod <directory>

If you change the user that runs the MongoDB process, you **must**
give the new user access to these directories.
```

#. Configure SELinux if enforced.  See `install-rhel-configure-selinux`.

### Configure SELinux

.. include:: /includes/fact-selinux-redhat-options.rst

.. include:: /includes/important-selinux-customizations.rst

### Procedure

Follow these steps to run MongoDB |edition| Edition on your system. These instructions assume that you are using the default settings.

.. include:: /includes/steps/run-mongodb-on-linux-tarball.rst

## Additional Information

### Localhost Binding by Default

.. include:: /includes/fact-installation-bind-ip-default-in-config.rst
