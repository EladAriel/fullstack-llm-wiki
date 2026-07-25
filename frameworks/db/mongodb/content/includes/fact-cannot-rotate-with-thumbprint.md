---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-cannot-rotate-with-thumbprint.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** You cannot use the :dbcommand:`rotateCertificates` command or the
:method:`db.rotateCertificates()` shell method when using
:setting:`net.tls.certificateSelector` or
:option:`--tlsCertificateSelector <mongod --tlsCertificateSelector>`
set to `thumbprint`
