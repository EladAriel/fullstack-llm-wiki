---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/community-apt-key.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

From a terminal, install `gnupg` and `curl` if they are not already available:

```bash
  sudo apt install gnupg curl
```

To import the MongoDB public GPG key, run the following command:

```bash
curl -fsSL https://www.mongodb.org/static/pgp/server-{+version+}.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-{+version+}.gpg \
   --dearmor
```
