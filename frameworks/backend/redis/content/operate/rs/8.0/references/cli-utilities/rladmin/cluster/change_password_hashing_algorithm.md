---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/cli-utilities/rladmin/cluster/change_password_hashing_algorithm.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.662513Z"
---
# Change_Password_Hashing_Algorithm

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
url: '/operate/rs/8.0/references/cli-utilities/rladmin/cluster/change_password_hashing_algorithm/'
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
