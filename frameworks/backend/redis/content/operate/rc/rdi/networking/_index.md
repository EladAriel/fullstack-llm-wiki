---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/rdi/networking/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.302441Z"
---
# _Index

---
Title: Networking
alwaysopen: false
categories:
- docs
- operate
- rc
description: Network reference for connecting a Data Integration pipeline to your source database.
hideListLinks: true
linkTitle: Networking
weight: 4
---

Your Data Integration pipeline runs on Redis Cloud and connects to your source database over [AWS PrivateLink]({{<relref "/operate/rc/rdi/setup#set-up-connectivity">}}). The following guides explain how the network path works and how to keep it available:

- [AWS PrivateLink reference]({{<relref "/operate/rc/rdi/networking/aws-privatelink">}}): How traffic flows between the pipeline and your database, which address each component sees, and how to keep the connection available when your database fails over.
