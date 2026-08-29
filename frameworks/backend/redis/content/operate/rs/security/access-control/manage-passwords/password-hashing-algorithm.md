---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/security/access-control/manage-passwords/password-hashing-algorithm.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.561826Z"
---
# Password Hashing Algorithm

---
Title: Change the password hashing algorithm
alwaysopen: false
categories:
- docs
- operate
- rs
description: Change the password hashing algorithm for user passwords in a Redis Software cluster.
linkTitle: Password hashing algorithm
toc: 'true'
weight: 95
---

Redis Software securely stores all user passwords using a cryptographic hash function. The default password hashing algorithm is `SHA-256`, but `PBKDF2` is also supported as of Redis Software version 7.8.6-13.

You can change the password hashing algorithm using [`rladmin`]({{<relref "/operate/rs/references/cli-utilities/rladmin">}}) or the [REST API]({{<relref "/operate/rs/references/rest-api">}}). When you change the password hashing algorithm, the cluster rehashes the administrator password and passwords for all users, including default users.

## Command-line method

To change the password hashing algorithm from the command line, run [`rladmin cluster change_password_hashing_algorithm`]({{<relref "/operate/rs/references/cli-utilities/rladmin/cluster/change_password_hashing_algorithm">}}):

```sh
rladmin cluster change_password_hashing_algorithm PBKDF2
```

## REST API method

You can [change the password hashing algorithm]({{<relref "/operate/rs/references/rest-api/requests/cluster/change_password_hashing_algorithm#patch-change-password-hashing-algorithm">}}) using a REST API request:

```sh
PATCH /v1/cluster/change_password_hashing_algorithm
{ "algorithm": "PBKDF2" }
```
