---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-aws-key-pct-encode-uri.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:** If the AWS access key ID, the secret access key, or the session token
include the following characters:
.. code-block:: none
   :copyable: false
   $ : / ? # [ ] @
those characters must be converted using `percent encoding
<https://tools.ietf.org/html/rfc3986#section-2.1>`__.
