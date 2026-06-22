---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/admonition-important-userToDNMapping-escape.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** If you use :setting:`~security.ldap.userToDNMapping`\'s
`substitution` parameter to transform the group name, the result
of the substitution **must** be an `RFC4514
<https://www.ietf.org/rfc/rfc4514.txt>`_ escaped string.
