---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-platform-support-ubuntu.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB {+version+} Community Edition supports the following :red:`64-bit` Ubuntu LTS (long-term support) releases on `x86_64 <prod-notes-supported-platforms-x86_64>` architecture:

- 24.04 :abbr:`LTS (Long Term Support)` ("Noble")
- 22.04 :abbr:`LTS (Long Term Support)` ("Jammy")
- 20.04 :abbr:`LTS (Long Term Support)` ("Focal")
MongoDB only supports the 64-bit versions of these platforms. To determine which Ubuntu release your host is running, run the following command on the host's terminal:

```bash
cat /etc/lsb-release
```

MongoDB {+version+} Community Edition on Ubuntu also supports the `ARM64 <prod-notes-supported-platforms-ARM64>` architecture on select platforms.

See `prod-notes-supported-platforms` for more information.
