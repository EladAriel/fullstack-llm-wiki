---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tls/step-create-csr.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

First, create a minimal OpenSSL configuration file called `csr.conf` that uses the following format:

For more information about the fields in this file, see the OpenSSL [config file documentation](https://docs.openssl.org/3.6/man5/config/)_. Ensure that you fill out both the Common Name (`CN`) and Subject Alternative Name (`alt_names`) fields in the configuration file.

Then, generate a :abbr:`CSR (Certificate Signing Request)`:

```bash
openssl req -new -key mongo0.key -out mongo0.csr -config csr.conf
```

This creates `mongo0.csr`. You will submit this file to the CA.
