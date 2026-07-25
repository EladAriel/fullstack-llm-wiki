---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/community-rhel-install.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To install the latest stable version of MongoDB, issue the following command:

```sh
sudo yum install -y {+package-name-org+}
```

Alternatively, to install a specific release of MongoDB, specify each component package individually and append the version number to the package name, as in the following example:

.. include:: /includes/release/pin-repo-to-version-yum.rst

> **Note:** `yum` automatically upgrades packages when newer versions
become available. If you want to prevent MongoDB upgrades, pin
the package by adding the following `exclude` directive to
your `/etc/yum.conf` file:
.. code-block:: ini
   exclude=mongodb-org,mongodb-org-database,mongodb-org-server,mongodb-mongosh,mongodb-org-mongos,mongodb-org-tools
