---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tls/step-verify-ca-bundle.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If your CA provided a separate chain file, you can also inspect it:

```bash
openssl x509 -in mongo0.crt -text -noout
openssl x509 -in ca.pem -text -noout
```

Confirm that the certificate's `Issuer` and `Subject` fields, as well as validity dates, look correct.
