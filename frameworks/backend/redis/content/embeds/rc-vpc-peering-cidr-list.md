---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-vpc-peering-cidr-list.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

If you've enabled the database's [CIDR allow list]({{< relref "/operate/rc/security/cidr-whitelist" >}}), you must also [add the VPC peered IP addresses to the CIDR allow list]({{< relref "/operate/rc/security/cidr-whitelist#define-cidr-allow-list" >}}) to connect to the database via the private endpoint.