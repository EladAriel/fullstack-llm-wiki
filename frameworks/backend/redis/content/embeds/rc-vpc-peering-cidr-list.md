---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-vpc-peering-cidr-list.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.100800Z"
---
# Rc Vpc Peering Cidr List

If you've enabled the database's [CIDR allow list]({{< relref "/operate/rc/security/cidr-whitelist" >}}), you must also [add the VPC peered IP addresses to the CIDR allow list]({{< relref "/operate/rc/security/cidr-whitelist#define-cidr-allow-list" >}}) to connect to the database via the private endpoint.