---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/code/community-ubuntu22-conf.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Create the list file for Ubuntu 22.04 (Jammy):

```bash
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-{+pgp-version+}.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/{+version+} multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-{+version+}.list
```
