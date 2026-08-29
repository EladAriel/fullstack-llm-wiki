---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-rdi-secrets-encryption-permissions.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.106362Z"
---
# Rc Rdi Secrets Encryption Permissions

* **Encryption key**: Select the [encryption key](#create-encryption-key) you created earlier.

* **Resource permissions**: Add the following permissions to your secret to allow the Redis data pipeline to access your secret. Replace `<AWS ACCOUNT ID>` with the AWS account ID for the Redis Cloud cluster that you saved earlier.

{{< embed-md "rc-rdi-secrets-permissions.md" >}}