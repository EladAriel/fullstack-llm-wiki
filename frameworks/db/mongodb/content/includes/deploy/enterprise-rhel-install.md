---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/enterprise-rhel-install.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To install the latest stable version of MongoDB Enterprise {+latest-lts-version+}, issue the following command:

```sh
sudo yum install -y {+package-name-enterprise+}
```

.. include:: /includes/release/pin-version-intro.rst

.. include:: /includes/release/pin-repo-to-version-yum-enterprise.rst

> **Note:** Although you can specify any available version of MongoDB
Enterprise, `yum` upgrades the packages when a newer
version becomes available. To prevent unintended upgrades,
pin the package by adding the following `exclude` directive
to your `/etc/yum.conf` file:
.. code-block:: ini
   exclude=mongodb-enterprise,mongodb-enterprise-database,mongodb-enterprise-server,mongodb-enterprise-shell,mongodb-enterprise-mongos,mongodb-enterprise-tools
