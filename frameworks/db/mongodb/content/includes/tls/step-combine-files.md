---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tls/step-combine-files.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You must combine your certificate and its private key to create a `.pem` file. For example, on Linux or MacOS:

```bash
 cat mongo0.crt mongo0.key > mongo0.pem
```

In Windows PowerShell:

```shell
 type mongo0.crt mongo0.key > mongo0.pem
```
