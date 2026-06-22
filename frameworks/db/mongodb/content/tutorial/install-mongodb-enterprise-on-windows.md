---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/install-mongodb-enterprise-on-windows.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# Install MongoDB Enterprise Edition on Windows

.. include:: /includes/minor-release.rst

## Overview

Use this tutorial to install MongoDB {+version+} |edition| Edition on Windows using the default installation wizard.

:products:`MongoDB Enterprise Edition</mongodb-enterprise-advanced>` is available on select platforms and contains support for features related to security and monitoring.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

### Installation Method

This tutorial installs MongoDB on Windows using the default MSI installation wizard. To install MongoDB using the `msiexec.exe` command-line tool instead, see `Install MongoDB using msiexec.exe <install-enterprise-windows-msiexec>`. The `msiexec.exe` tool is useful for system administrators who deploy MongoDB using automation.

## Considerations

### MongoDB Shell, `mongosh`

.. include:: /includes/fact-have-to-install-mongosh-win.rst

### Platform Support

.. include:: /includes/fact-platform-support-enterprise-windows.rst

### Virtualization

.. include:: /includes/fact-virtualbox-not-supported.rst

### Production Notes

.. include:: /includes/fact-see-production-notes.rst

### Full Time Diagnostic Data Capture

MongoDB logs diagnostic data to assist with troubleshooting. For details, see `Full Time Diagnostic Data Capture <ftdc-stub>`.

.. include:: /includes/fact-ftdc-windows-user-permissions.rst

## Install MongoDB Enterprise Edition

### Procedure

Follow these steps to install MongoDB |edition| Edition using the Windows Installation wizard. The installation process installs the MongoDB binaries and the default `configuration <configuration-options>` file. The configuration file is located in the installation directory at :file:`bin\\mongod.cfg`.

.. include:: /includes/deploy/windows-interactive.rst

### If You Installed MongoDB as a Windows Service

The MongoDB service starts upon successful installation. Configure the MongoDB instance with the configuration file :file:`<install directory>\\bin\\mongod.cfg`.

If you have not already done so, follow the :mongosh:`mongosh installation instructions </install>` to download and install the MongoDB Shell (:mongosh:`mongosh </>`).

Be sure to add the path to your `mongosh.exe` binary to your `PATH` environment variable during installation.

Open a new :guilabel:`Command Interpreter` and enter `mongosh.exe` to connect to MongoDB.

For more information on connecting to `mongod` using :mongosh:`mongosh.exe </>`, such as connecting to a MongoDB instance running on a different host and/or port, see :mongosh:`Connect to a Deployment </connect>`.

For information on CRUD (Create, Read, Update, Delete) operations, see:

- `write-op-insert`
- `read-operations-queries`
- `write-op-update`
- `write-op-delete`
### If You Did Not Install MongoDB as a Windows Service

If you only installed the executables and did not install MongoDB as a Windows service, you must manually start the MongoDB instance.

See `run-mongodb-enterprise-from-cmd` for instructions.

## Start MongoDB Enterprise Edition from the Command Interpreter

.. include:: /includes/steps/run-mongodb-on-windows.rst

## Start MongoDB Enterprise Edition as a Windows Service

You can install and configure MongoDB as a :guilabel:`Windows Service` during installation. The MongoDB service starts upon successful installation.

To start or restart the MongoDB service, use the Services console:

#. From the Services console, locate the MongoDB service.

#. Right-click on the MongoDB service and click :guilabel:`Start`.

You can also manage the service from the command line. To start the MongoDB service from the command line, open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows- commands/cmd)_ (`cmd.exe`) as an :guilabel:`Administrator`, and run the following command:

.. include:: /includes/steps/create-manually-windows-service-for-mongodb.rst

## Stop MongoDB Enterprise Edition as a Windows Service

To stop or pause the MongoDB service, use the Services console:

#. From the Services console, locate the MongoDB service.

#. Right-click on the MongoDB service and click :guilabel:`Stop` or :guilabel:`Pause`.

You can also manage the service from the command line. To stop the MongoDB service from the command line, open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows- commands/cmd)_ (`cmd.exe`) as an :guilabel:`Administrator`, and run the following command:

```bat
net stop MongoDB
```

## Remove MongoDB Enterprise Edition as a Windows Service

To remove the MongoDB service, first use the Services console to stop the service. Then open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd)_ (`cmd.exe`) as an :guilabel:`Administrator`, and run the following command:

```bat
sc.exe delete MongoDB
```

## Additional Considerations

### Localhost Binding by Default

.. include:: /includes/fact-installation-bind-ip-default-in-config.rst

### Point Releases and `.msi`

If you installed MongoDB with the Windows installer (`.msi`), the `.msi` automatically upgrades within its `release series <release-version-numbers>`, such as 4.2.1 to 4.2.2.

Upgrading a full release series, such as 4.0 to 4.2, requires a new installation.

### Add MongoDB binaries to the System PATH

All command-line examples in this tutorial use absolute paths to the MongoDB binaries. You can add `C:\Program Files\MongoDB\Server\{+version+}\bin` to your System `PATH` to omit the full path to the MongoDB binaries.

## Contents

- Install using msiexec.exe </tutorial/install-mongodb-enterprise-on-windows-unattended>
- Install From Zip File </tutorial/install-mongodb-enterprise-on-windows-zip>
