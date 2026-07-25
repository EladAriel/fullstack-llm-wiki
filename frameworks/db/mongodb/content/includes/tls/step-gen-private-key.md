---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tls/step-gen-private-key.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Generate a private key with OpenSSL:

```bash
 openssl genrsa -out mongo0.key 4096
```

This generates a 4096-bit RSA private key. If you need to use a different key size or algorithm, see the OpenSSL documentation.

Restrict permissions on the generated `mongo0.key` file:

```bash
 chmod 600 mongo0.key
```

Keep this file secret. The server uses this key to prove it owns the certificate.
