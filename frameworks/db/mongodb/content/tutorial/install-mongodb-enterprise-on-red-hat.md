---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/install-mongodb-enterprise-on-red-hat.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================================

# Install MongoDB Enterprise Edition on Red Hat or CentOS

.. include:: /includes/minor-release.rst

## Overview

Use this tutorial to install MongoDB {+version+} |edition| Edition on Red Hat Enterprise Linux, CentOS Linux, or Oracle Linux [#oracle-linux]_ using the |package-manager| package manager.

:products:`MongoDB Enterprise Edition</mongodb-enterprise-advanced>` is available on select platforms and contains support for features related to security and monitoring.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

## Considerations

### Platform Support

.. include:: /includes/fact-platform-support-enterprise-red-hat.rst

### Production Notes

.. include:: /includes/fact-see-production-notes.rst

## Install MongoDB Enterprise Edition

Follow these steps to install MongoDB |edition| Edition using the |package-manager| package manager.

.. include:: /includes/deploy/enterprise-rhel

> **Note:** .. include:: /includes/install-mongodb-yum-commands.rst

## Run MongoDB Enterprise Edition

### ulimit

.. include:: /includes/fact-installation-ulimit.rst

### Directory Paths

To Use Default Directories ``````````````````````````

By default, MongoDB runs using the |mongod-user| user account and uses the following default directories:

- |mongod-datadir| (the data directory)
- `/var/log/mongodb` (the log directory)
The package manager creates the default directories during installation. The owner and group name are |mongod-user|.

To Use Non-Default Directories ``````````````````````````````

To use a data directory and/or log directory other than the default directories:

#. Create the new directory or directories.

#. Edit the configuration file `/etc/mongod.conf` and modify the following fields accordingly:

- :setting:`storage.dbPath` to specify a new data directory path, such as `/some/data/directory`
- :setting:`systemLog.path` to specify a new log file path, such as `/some/log/directory/mongod.log`
#. Ensure that the user running MongoDB has access to the directory or directories:

```bash
   sudo chown -R mongod:mongod <directory>

If you change the user that runs the MongoDB process, you **must**
give the new user access to these directories.
```

#. Configure SELinux if enforced. See `install-enterprise-rhel-configure-selinux`.

### Configure SELinux

.. include:: /includes/fact-selinux-redhat-with-policy.rst

### Procedure

Follow these steps to run MongoDB |edition| Edition on your system. These instructions assume that you are using the default settings.

**Init System**

.. include:: /includes/fact-systemd-vs-initd.rst

## Uninstall MongoDB

.. include:: /includes/fact-uninstall.rst

.. include:: /includes/steps/uninstall-mongodb-enterprise-on-redhat.rst

## Additional Information

### Localhost Binding by Default

.. include:: /includes/fact-installation-bind-ip-default-in-config.rst

### MongoDB Enterprise Edition Packages

.. include:: /includes/list-mongodb-enterprise-packages.rst

## Contents

- Install using .tgz Tarball </tutorial/install-mongodb-enterprise-on-red-hat-tarball>
