---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-rdi-secrets-encryption-permissions.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

* **Encryption key**: Select the [encryption key](#create-encryption-key) you created earlier.

* **Resource permissions**: Add the following permissions to your secret to allow the Redis data pipeline to access your secret. Replace `<AWS ACCOUNT ID>` with the AWS account ID for the Redis Cloud cluster that you saved earlier.

{{< embed-md "rc-rdi-secrets-permissions.md" >}}