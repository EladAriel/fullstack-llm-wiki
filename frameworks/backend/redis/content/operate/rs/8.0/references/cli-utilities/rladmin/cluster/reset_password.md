---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/cli-utilities/rladmin/cluster/reset_password.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: rladmin cluster reset_password
alwaysopen: false
categories:
- docs
- operate
- rs
description: Changes the password for a given email.
headerRange: '[1-2]'
linkTitle: reset_password
tags:
- configured
toc: 'true'
weight: $weight
url: '/operate/rs/8.0/references/cli-utilities/rladmin/cluster/reset_password/'
---

Changes the password for the user associated with the specified email address.

Enter a new password when prompted. Then enter the same password when prompted a second time to confirm the password change.

```sh
rladmin cluster reset_password <user email>
```

### Parameters

| Parameter | Type/Value | Description |
|-----------|------------|-------------|
| user email | email address | The email address of the user that needs a password reset |

### Returns

Reports whether the password change succeeded or an error occurred. 

### Example

```sh
$ rladmin cluster reset_password user@example.com
New password: 
New password (again): 
Password changed.
```