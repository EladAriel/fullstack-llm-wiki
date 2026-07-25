---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/admonition-multiple-arbiters.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** Avoid deploying more than one `arbiter` in a :term:`replica
set`. See `rollbacks-multi-arbiters`.

To add an arbiter to an existing replica set:

- Typically, if there are two or fewer data-bearing members in the
replica set, you might need to first set the `cluster wide write concern <set_global_default_write_concern>` for the replica set.

- See :ref:`cluster wide write concern
<set_global_default_write_concern>` for more information on why you might need to set the cluster wide write concern.

You do not need to change the cluster wide write concern before starting a new replica set with an arbiter.

> **Seealso:** `Default write concern formula <default-wc-formula>`
