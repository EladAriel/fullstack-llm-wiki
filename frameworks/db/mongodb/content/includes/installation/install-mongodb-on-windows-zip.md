---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/installation/install-mongodb-on-windows-zip.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================================================

# Install MongoDB Community on Windows using the Zip File

## Overview

Use this tutorial to install MongoDB Community on Windows by downloading and extracting the zip file.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

### Installation Method

This tutorial installs MongoDB on Windows by extracting from a zip file. You can also install MongoDB on Windows by these other methods:

- `Install MongoDB using msiexec.exe <install-mdb-community-windows-msiexec>`
- `Install MongoDB using the MSI Installer <install-mdb-community-windows>`
## Considerations

### MongoDB Shell, `mongosh`

.. include:: /includes/fact-have-to-install-mongosh-win.rst

### Platform Support

.. include:: /includes/fact-platform-support-windows.rst

### Virtualization

.. include:: /includes/fact-virtualbox-not-supported.rst

### Production Notes

.. include:: /includes/fact-see-production-notes.rst

### Full Time Diagnostic Data Capture

MongoDB logs diagnostic data to assist with troubleshooting. For detailed information, see `Full Time Diagnostic Data Capture <ftdc-stub>`.

.. include:: /includes/fact-ftdc-windows-user-permissions.rst

## Install MongoDB Community Edition

### Procedure

Follow these steps to install MongoDB |edition| Edition from the zip file.

.. include:: /includes/steps/install-mongodb-on-windows-zip.rst

## Start MongoDB Community Edition from the Command Interpreter

.. include:: /includes/start-community-from-cmd.rst

## Run MongoDB Community Edition as a Windows Service

.. include:: /includes/community-as-service-on-windows.rst

## Additional Considerations

.. include:: /includes/community-on-windows-considerations.rst
