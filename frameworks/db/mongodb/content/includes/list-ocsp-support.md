---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/list-ocsp-support.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- [OCSP stapling](https://tools.ietf.org/html/rfc6961)_. With OCSP
stapling, :binary:`~bin.mongod` and :binary:`~bin.mongos` instances attach or "staple" the OCSP status response to their certificates when providing these certificates to clients during the TLS/SSL handshake. OCSP stapling removes the need for clients to make a separate request to retrieve the OCSP status of the provided certificate. The OCSP status response is included with the certificates.

- [OCSP must-staple extension](https://tools.ietf.org/html/rfc7633)_.
OCSP must-staple is an extension that can be added to the server certificate that tells the client to expect an OCSP staple when it receives a certificate during the TLS/SSL handshake.
