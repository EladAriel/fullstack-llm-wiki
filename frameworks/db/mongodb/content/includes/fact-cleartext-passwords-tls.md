---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-cleartext-passwords-tls.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** By default, |command| sends all specified data to the MongoDB
instance in cleartext, even if using :method:`passwordPrompt()`. Use
TLS transport encryption to protect communications between clients
and the server, including the password sent by |command|. For
instructions on enabling TLS transport encryption, see
`/tutorial/configure-ssl`.
MongoDB does not store the password in cleartext. The password
is only vulnerable in transit between the client and the
server, and only if TLS transport encryption is not enabled.
