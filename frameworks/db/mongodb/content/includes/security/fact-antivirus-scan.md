---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/security/fact-antivirus-scan.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If you use an antivirus (AV) scanner or an endpoint detection and response (EDR) scanner, configure your scanner to exclude the :setting:`database storage path <storage.dbPath>` and the :setting:`database log path <systemLog.path>` from the scan.

The data files in the `database storage path` are compressed. Additionally, if you use the `encrypted storage engine <security-encryption-at-rest>`, the data files are also encrypted. The I/O and CPU costs to scan these files may significantly decrease performance without providing any security benefits.

If you don't exclude the directories in your `database storage path` and `database log path`, the scanner could quarantine or delete important files. Missing or quarantined files can corrupt your database and crash your MongoDB instance.
