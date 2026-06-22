---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/cli-utilities/rladmin/cluster/reset_password.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
url: '/operate/rs/7.4/references/cli-utilities/rladmin/cluster/reset_password/'
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
