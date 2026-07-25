---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/linux-syslog-limitations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In a Linux system, messages are subject to the rules defined in the Linux configuration file :file:`/etc/systemd/journald.conf`. By default, log message bursts are limited to 1000 messages within a 30 second period. To see more messages, increase the `RateLimitBurst` parameter in :file:`/etc/systemd/journald.conf`.
