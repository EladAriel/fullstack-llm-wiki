---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-bind-to-all-ips.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To bind to all IPv4 addresses, you can specify the bind ip address of `0.0.0.0`. To bind to all IPv4 and IPv6 addresses, you can specify the bind ip address of `::,0.0.0.0` or alternatively, use the new :setting:`net.bindIpAll` setting or the new command-line option `--bind_ip_all`.
