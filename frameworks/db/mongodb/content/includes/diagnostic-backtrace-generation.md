---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/diagnostic-backtrace-generation.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For MongoDB instances running on Linux:

- When the :binary:`~bin.mongod` and :binary:`~bin.mongos` processes
receive a `SIGUSR2` signal, backtrace details are added to the logs for each process thread.

- Backtrace details show the function calls for the process, which can
be used for diagnostics and provided to MongoDB Support if required.

The backtrace functionality is available for these architectures:

- `x86_64`
- `arm64` (starting in MongoDB 5.0.10, and 6.0)
