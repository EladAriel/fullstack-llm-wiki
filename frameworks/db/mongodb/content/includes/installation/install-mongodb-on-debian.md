---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/installation/install-mongodb-on-debian.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# Install MongoDB Community Edition on Debian

.. include:: /includes/fact-atlas-banner.rst

## Overview

Use this tutorial to install MongoDB {+version+} |edition| Edition using the |package-manager| package manager.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

## Considerations

### Platform Support

.. include:: /includes/fact-platform-support-debian.rst

### Production Notes

.. include:: /includes/fact-see-production-notes.rst

### Official MongoDB Packages

.. include:: /includes/important-dont-use-distro-packages.rst

See `debian-package-content` for the complete list of official packages.

## Install MongoDB Community Edition

Follow these steps to install MongoDB |edition| Edition using the |package-manager| package manager.

.. include:: /includes/deploy/community-debian

## Run MongoDB Community Edition

### ulimit Considerations

.. include:: /includes/fact-installation-ulimit.rst

### Directories

.. include:: /includes/fact-installation-directories.rst

### Procedure

Follow these steps to run MongoDB |edition| Edition on your system. These instructions assume that you are using the official |package-name| package -- not the unofficial `mongodb` package provided by |distro-name| --  and are using the default settings.

**Init System**

.. include:: /includes/fact-systemd-vs-initd.rst

## Uninstall MongoDB Community Edition

.. include:: /includes/fact-uninstall.rst

.. include:: /includes/steps/uninstall-mongodb-on-debian.rst

## Additional Information

### Localhost Binding by Default

.. include:: /includes/fact-installation-bind-ip-default-in-config.rst

### MongoDB Community Edition Packages

.. include:: /includes/list-mongodb-org-packages.rst
