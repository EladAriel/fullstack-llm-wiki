---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/quick-start/production-warning.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Important:** Because the instructions in this tutorial include storing an encryption key in an insecure
environment, you should not use an unmodified version of this
application in production. Using this application in production risks
unauthorized access to the encryption key or loss of the key needed to
decrypt your data. The purpose of this tutorial is to demonstrate how to use
{+qe+} without needing to set up a {+kms-long+}.
You can use a {+kms-long+} to securely store your encryption key in a production
environment. A {+kms-abbr+} is a remote service that securely stores and manages your
encryption keys. To learn how to set up a {+qe+} enabled application that
uses a {+kms-abbr+}, see the `{+qe+} Tutorials <qe-tutorial-automatic-encryption>`.
