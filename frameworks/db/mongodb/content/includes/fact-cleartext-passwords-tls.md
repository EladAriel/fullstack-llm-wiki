---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-cleartext-passwords-tls.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
