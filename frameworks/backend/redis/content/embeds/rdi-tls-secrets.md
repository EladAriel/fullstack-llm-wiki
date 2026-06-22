---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rdi-tls-secrets.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

When creating secrets for TLS or mTLS, ensure that all certificates and keys are in `PEM` format. The only exception to this is that for PostgreSQL, the private key `SOURCE_DB_KEY` secret must be in `DER` format. If you have a key in `PEM` format, you must convert it to `DER` before creating the `SOURCE_DB_KEY` secret using the command:

```bash
openssl pkcs8 -topk8 -inform PEM -outform DER \
    -in /path/to/myclient.pem \
    -out /path/to/myclient.pk8 -nocrypt
```

This command assumes that the private key is not encrypted. See the [`openssl` documentation](https://docs.openssl.org/master/) to learn how to convert an encrypted private key.