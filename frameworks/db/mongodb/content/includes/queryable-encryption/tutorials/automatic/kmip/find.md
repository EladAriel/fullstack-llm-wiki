---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/automatic/kmip/find.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Retrieve the {+in-use-doc+} you inserted in the `Insert a Document with Encrypted Fields <qe-kmip-insert>` step of this guide.

To show the functionality of {+qe-abbr+}, the following code snippet queries for your document with a client configured for automatic {+qe-abbr+} as well as a client that is not configured for automatic {+qe-abbr+}.

The output of the preceding code snippet should look like this:
