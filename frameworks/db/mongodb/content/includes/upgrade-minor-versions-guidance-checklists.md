---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/upgrade-minor-versions-guidance-checklists.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

If you need guidance on upgrading to |newversion|, [MongoDB professional services](https://www.mongodb.com/products/consulting) offer upgrade support to help ensure a smooth transition without interruption to your MongoDB application.

## Upgrade Recommendations and Checklists

When upgrading, consider the following:

### Upgrade Version Path

To upgrade an existing MongoDB deployment to |newversion|, you must be running a |newseries|-series release.

When upgrading from a minor version, you must successively upgrade minor releases until you have upgraded to |newversion|.

To learn more, see `Upgrade 8.2 to 8.3 <8.3-upgrade-from-8.2>`.

### Check Driver Compatibility

Before you upgrade MongoDB, check that you're using a MongoDB |newversion|-compatible driver. Consult the :driver:`driver documentation </>` for your specific driver to verify compatibility with MongoDB |newversion|.

Upgraded deployments that run on incompatible drivers might encounter unexpected or undefined behavior.

### Preparedness

Before beginning your upgrade, see the |compatibility| document to ensure that your applications and deployments are compatible with MongoDB |newversion|. Resolve the incompatibilities in your deployment before starting the upgrade.

Before upgrading MongoDB, always test your application in a staging environment before deploying the upgrade to your production environment.

### Downgrade Consideration

.. include:: /includes/downgrade/previous-version.rst

.. include:: includes/downgrade/single-version-support.rst
