---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/install-mongodb-enterprise-on-windows-zip.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================================

# Install MongoDB Enterprise on Windows From a Zip File

.. include:: /includes/minor-release.rst

## Overview

Use this tutorial to install MongoDB {+version+} |edition| Edition on Windows by downloading and extracting the zip file.

:products:`MongoDB Enterprise Edition</mongodb-enterprise-advanced>` is available on select platforms and contains support for features related to security and monitoring.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

### Installation Method

This tutorial installs MongoDB on Windows by extracting from a zip file. You can also install MongoDB on Windows using these methods:

- `Install MongoDB using msiexec.exe <install-enterprise-windows-msiexec>`
- `Install MongoDB using the MSI Installer <install-enterprise-windows>`
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

Follow these steps to install MongoDB |edition| Edition from the zip file.

.. include:: /includes/deploy/windows-zip.rst

## Configure MongoDB Enterprise Edition as a Windows Service

You can install and configure MongoDB as a :guilabel:`Windows Service`. Follow these steps:

1. Add `<install directory>\bin` to your `PATH` environment
variable.

#. Open a Windows Command prompt as an :guilabel:`Administrator`, change to your MongoDB install directory, and run `mongod` with the `--dbpath`, `--logpath` and `--install` parameters. For example, the following command installs MongoDB as a service that uses `C:\data\db` for its data location and `C:\data\log.txt` for the log file:

```bat
   mongod --dbpath=C:\data\db --logpath=C:\data\log.txt --install
```

## Start MongoDB Enterprise Edition as a Windows Service

.. include:: /includes/steps-start-windows-service.rst

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

## Start MongoDB Enterprise Edition from the Command Interpreter

Open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows- commands/cmd)_ (`cmd.exe`) as an :guilabel:`Administrator`.

> **Important:** You must open the command interpreter as an
:guilabel:`Administrator`.

.. include:: /includes/steps/run-mongodb-on-windows.rst

## Additional Considerations

### Localhost Binding by Default

.. include:: /includes/fact-installation-bind-ip-default-in-config.rst

### Point Releases and `.msi`

If you installed MongoDB with the Windows installer (`.msi`), the `.msi` automatically upgrades within the `same release series <release-version-numbers>`, such as 7.2.1 to 7.2.2.

Upgrading a full release series, such as 6.0 to 7.0, requires a new installation.

### Add MongoDB binaries to the System PATH

All command-line examples in this tutorial use absolute paths to the MongoDB binaries. You can add `C:\Program Files\MongoDB\Server\{+version+}\bin` to your System `PATH` to omit the full path to the MongoDB binaries.
