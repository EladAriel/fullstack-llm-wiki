---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/linux-syslog-limitations.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In a Linux system, messages are subject to the rules defined in the Linux configuration file :file:`/etc/systemd/journald.conf`. By default, log message bursts are limited to 1000 messages within a 30 second period. To see more messages, increase the `RateLimitBurst` parameter in :file:`/etc/systemd/journald.conf`.
