---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/install-mongodb-enterprise-on-os-x.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Install MongoDB Enterprise on macOS

.. include:: /includes/minor-release.rst

## Overview

Use this tutorial to manually install MongoDB {+version+} |edition| Edition on macOS using a downloaded `.tgz` tarball.

:products:`MongoDB Enterprise Edition</mongodb-enterprise-advanced>` is available on select platforms and contains support for features related to security and monitoring.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

## Considerations

### MongoDB Shell, `mongosh`

.. include:: /includes/fact-have-to-install-mongosh-tgz.rst

### Platform Support

.. include:: /includes/fact-platform-support-enterprise-macos.rst

### Production Notes

.. include:: /includes/fact-see-production-notes.rst

## Install MongoDB Enterprise Edition

To manually install MongoDB |edition| Edition from the `.tgz`, complete the following steps:

.. include:: /includes/deploy/install-tar.rst

## Run MongoDB Enterprise Edition

ulimit Considerations

.. include:: /includes/fact-installation-ulimit.rst

### Procedure

Follow these steps to run MongoDB |edition| Edition. These instructions assume that you are using the default settings.

.. include:: /includes/steps/run-mongodb-on-osx.rst

## Additional Information

### Localhost Binding by Default

.. include:: /includes/fact-installation-bind-ip-default-in-config.rst
