---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-bind-to-all-ips.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To bind to all IPv4 addresses, you can specify the bind ip address of `0.0.0.0`. To bind to all IPv4 and IPv6 addresses, you can specify the bind ip address of `::,0.0.0.0` or alternatively, use the new :setting:`net.bindIpAll` setting or the new command-line option `--bind_ip_all`.
