---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tls/step-copy-files.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Copy your `.pem` files to the directory where you plan to store TLS assets for MongoDB. You will reference these paths in your MongoDB configuration file in the next tutorial.

You might need to copy the `.pem` files onto the remote server on which you host your node. Additionally, ensure you secure your files with appropriate permissions, such as read-only access for the owner.

In Linux/MacOS:

```bash
sudo mkdir -p /etc/ssl/mongodb
sudo cp mongo0.pem ca.pem /etc/ssl/mongodb
```

In Windows PowerShell:

```shell
New-Item -ItemType Directory -Path C:\tls\mongodb -Force
Copy-Item mongo0.pem,ca.pem `
  -Destination C:\tls\mongodb
```
