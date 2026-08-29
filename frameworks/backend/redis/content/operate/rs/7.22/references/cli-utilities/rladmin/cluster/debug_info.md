---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/rladmin/cluster/debug_info.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.374576Z"
---
# Debug_Info

---
Title: rladmin cluster debug_info
alwaysopen: false
categories:
- docs
- operate
- rs
description: Creates a support package.
headerRange: '[1-2]'
linkTitle: debug_info
tags:
- configured
toc: 'true'
weight: $weight
url: '/operate/rs/7.22/references/cli-utilities/rladmin/cluster/debug_info/'
---

Downloads a support package to the specified path. If you do not specify a path, it downloads the package to the default path specified in the cluster configuration file.

```sh
rladmin cluster debug_info
        [ node <ID> ]
        [ path <path> ]
```

### Parameters

| Parameter | Type/Value | Description |
|-----------|------------|-------------|
| node | integer | Downloads a support package for the specified node |
| path | filepath | Specifies the location where the support package should download |

### Returns

Reports the progress of the support package download.

### Example

```sh
$ rladmin cluster debug_info node 1
Preparing the debug info files package
Downloading...
[==================================================]
Downloading complete. File /tmp/debuginfo.20220511-215637.node-1.tar.gz is saved.
```
