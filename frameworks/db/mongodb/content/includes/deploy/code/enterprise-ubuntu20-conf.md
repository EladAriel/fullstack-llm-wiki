---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/code/enterprise-ubuntu20-conf.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Create the list file for Ubuntu 20.04 (Focal).

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-{+pgp-version+}.gpg ] http://repo.mongodb.com/apt/ubuntu focal/mongodb-enterprise/{+version+} multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-enterprise-{+version+}.list
```
