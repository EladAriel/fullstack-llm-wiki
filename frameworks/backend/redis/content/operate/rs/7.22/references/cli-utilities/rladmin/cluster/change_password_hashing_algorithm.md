---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/cli-utilities/rladmin/cluster/change_password_hashing_algorithm.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: rladmin cluster change_password_hashing_algorithm
alwaysopen: false
categories:
- docs
- operate
- rs
description: Changes the password hashing algorithm.
headerRange: '[1-2]'
linkTitle: change_password_hashing_algorithm
tags:
- configured
toc: 'true'
weight: $weight
url: '/operate/rs/7.22/references/cli-utilities/rladmin/cluster/change_password_hashing_algorithm/'
---

Changes the password hashing algorithm for the entire cluster. When you change the hashing algorithm, it rehashes the administrator password and passwords for all users, including default users.

```sh
rladmin cluster change_password_hashing_algorithm <algorithm>
```

### Parameters

| Parameter | Type/Value | Description |
|-----------|------------|-------------|
| algorithm | SHA-256<br />PBKDF2 | Change to the specified hashing algorithm. The default hashing algorithm is `SHA-256`. |

### Returns

Reports whether the algorithm change succeeded or an error occurred.

### Example

```sh
$ rladmin cluster change_password_hashing_algorithm PBKDF2
Please confirm changing the password hashing algorithm
Please confirm [Y/N]: y
Algorithm changed
```
