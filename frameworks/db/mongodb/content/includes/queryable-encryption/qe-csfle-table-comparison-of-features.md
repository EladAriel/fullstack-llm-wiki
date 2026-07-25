---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/qe-csfle-table-comparison-of-features.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The following table describes potential security threats and how MongoDB encryption features address them. Use these mechanisms together: Role-Based Access Control, Encryption at Rest, Transport Encryption, and In-Use Encryption. Note that you can't use both {+csfle+} and {+qe+} in the same collection.

> **Important:** This is a high-level summary meant for general comparison. For detailed
information, see the
`Overview of {+qe+}
<https://cdn.bfldr.com/2URK6TO/as/64kp46t53v34xw37gkngbrg/An_Overview_of_Queryable_Encryption>`__
and
`Design and Analysis of a Stateless
Document Database Encryption Scheme
<https://cdn.bfldr.com/2URK6TO/as/jkwp857q2zr8fj5vqs24f5/Design__Analysis_Stateless_Document_Database_Encryption_Scheme>`__
whitepapers.

This assumes exfiltration occurs between completed operations. See [whitepaper](https://cdn.bfldr.com/2URK6TO/as/64kp46t53v34xw37gkngbrg/An_Overview_of_Queryable_Encryption)_ for details.
