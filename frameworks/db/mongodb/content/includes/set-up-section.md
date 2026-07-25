---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/set-up-section.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Before you begin this tutorial, complete the following prerequisite steps:

1. Download the {+shared-library+} from the :website:`MongoDB Download Center </try/download/enterprise>`.
Navigate to the :guilabel:`MongoDB Enterprise Server Download` section and select the follow options:

- In the :guilabel:`Version` dropdown, select the version marked as `"current"`.
- In the :guilabel:`Platform` dropdown, select your platform.
- In the :guilabel:`Package` dropdown, select `crypt_shared`.
Extract the archive and save the path to the shared library file for future use.

> **Note:**    The {+shared-library+} is a preferred alternative to `mongocryptd` and
   does not require spawning a new process to perform automatic encryption.
   This tutorial uses the {+shared-library+}, but `mongocryptd` is still
   supported.

2. Configure a MongoDB Atlas cluster or a local replica set deployment, and save your
connection string for future use. To learn more, see the `unified-get-started` tutorial.
