---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tls/step-verify-certificate.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

After you receive or create your certificate, verify that it matches the private key:

```bash
# Compare the modulus of the key and certificate
openssl rsa -noout -modulus -in  mongo0.key | openssl sha256
openssl x509 -noout -modulus -in mongo0.crt | openssl sha256
```

The output digests must match. If they do not, the certificate and key do not belong together, and MongoDB will not be able to use them.
