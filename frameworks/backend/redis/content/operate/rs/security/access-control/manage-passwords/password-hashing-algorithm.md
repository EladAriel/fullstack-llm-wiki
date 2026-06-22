---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/security/access-control/manage-passwords/password-hashing-algorithm.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
