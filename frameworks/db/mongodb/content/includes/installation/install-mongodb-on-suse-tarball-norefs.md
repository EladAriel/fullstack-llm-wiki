---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/installation/install-mongodb-on-suse-tarball-norefs.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================================

# Install MongoDB Community on SUSE using .tgz Tarball

## Overview

Use this tutorial to manually install MongoDB {+version+} |edition| Edition on SUSE Linux Enterprise Server (SLES) using a downloaded `.tgz` tarball.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

### Installation Method

.. include:: /includes/fact-use-package-manager.rst

|arrow| See `Install MongoDB using the zypper Package Manager <install-mdb-community-suse>` for instructions.

## Considerations

### MongoDB Shell, `mongosh`

.. include:: /includes/fact-have-to-install-mongosh-tgz.rst

### Platform Support

.. include:: /includes/fact-platform-support-suse.rst

### Production Notes

.. include:: /includes/fact-see-production-notes.rst

## Install MongoDB Community Edition

### Prerequisites

.. include:: /includes/fact-tarball-dependencies.rst

.. include:: /includes/extracts/install-mongodb-community-manually-suse-15.rst

### Procedure

Follow these steps to manually install MongoDB |edition| Edition from the `.tgz`.

.. include:: /includes/steps/install-mongodb-on-linux.rst

## Run MongoDB Community Edition

Follow these steps to run MongoDB |edition| Edition. These instructions assume that you are using the default settings.

.. include:: /includes/steps/run-mongodb-on-linux-tarball.rst

## Additional Information

### Localhost Binding by Default

.. include:: /includes/fact-installation-bind-ip-default-in-config.rst
