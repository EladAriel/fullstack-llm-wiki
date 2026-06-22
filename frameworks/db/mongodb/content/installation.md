---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/installation.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Install MongoDB

MongoDB is available in two server editions: Community and Enterprise.

This section contains information on installing MongoDB.

- To upgrade your current deployment to MongoDB {+version+}, see
`{+version+} Upgrade Procedures <{+version+}-upgrade>`.

- To upgrade to the latest patch release for your current version,
see `upgrade-to-latest-revision`.

## MongoDB Installation Tutorials

> **Note:** If you installed MongoDB using a package manager such as APT, DNF,
or Zypper, use your operating system's package management tool to
upgrade within `Patch Releases <versions-patch-release>`.
For `Major <major-releases>` and `Minor <minor-releases>`
releases, follow the installation instructions for your OS.

MongoDB installation tutorials are available for both Community Edition and Enterprise Edition on the following platforms:

### Community Edition

To install MongoDB Community Edition, see `Install MongoDB Community Edition <install-mdb-community-edition>`. Select your platform and follow the instructions for your operating system.

### Enterprise Edition

To install MongoDB Enterprise Edition, select the tutorial for your platform and follow the instructions for your operating system.

.. include:: /includes/unicode-checkmark.rst

## Upgrade Community Edition to Enterprise Edition Tutorials

> **Important:** .. include:: /includes/extracts/enterprise-upgrade-edition-only.rst

- `upgrade_to_enterprise_standalone`
- `upgrade_to_enterprise_rs`
- `upgrade_to_enterprise_sharded_cluster`
## Supported Platforms

> **Important:** MongoDB does not support 32-bit x86 platforms.

.. include:: includes/platform-support.rst

MongoDB only supports Oracle Linux running the  Red Hat Compatible Kernel (RHCK). MongoDB does **not** support the Unbreakable Enterprise Kernel (UEK).

MongoDB on-premises products released for RHEL version 8.0+ are compatible with and supported on Rocky Linux version 8.0+ and AlmaLinux version 8.0+, contingent upon those distributions meeting their obligation to deliver full RHEL compatibility.

MongoDB versions 5.0 and greater are tested against SLES 12 service pack 5. Earlier versions of MongoDB are tested against SLES 12 with no service pack.

MongoDB versions 7.0 and later are tested against SLES 15 service pack 4. Earlier versions of MongoDB are tested against SLES 15 with no service pack.

MongoDB version 7.0 is built and tested against RHEL 7.9. Earlier versions of MongoDB are tested against RHEL 7 and assume forward compatibility.

.. include:: includes/fact-in-place-os-upgrades.rst

## Contents

- Community Edition </administration/install-community>
- Enterprise </administration/install-enterprise>
- Upgrade Community to Enterprise </administration/upgrade-community-to-enterprise>
- Verify Package Integrity </tutorial/verify-mongodb-packages>
- MongoDB Package Components </reference/program>
