---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/security/access-control/data-access-control/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
LinkTitle: Data access control
Title: Data access control
alwaysopen: false
categories:
- docs
- operate
- rc
description: Control who can access your databases using the default user database
  password and role-based access control.
headerRange: '[1-3]'
hideListLinks: true
toc: 'true'
weight: 25
---

## Default user

When you create a Redis Cloud database, your database is given a randomly generated password called the [**Default user password**]({{< relref "/operate/rc/security/access-control/data-access-control/default-user" >}}). Learn how to [change the default user password]({{< relref "/operate/rc/security/access-control/data-access-control/default-user#change-password" >}}) or [turn off default user access]({{< relref "/operate/rc/security/access-control/data-access-control/default-user#turn-off-default-user" >}}).

## Role-based access control

With [role-based access control (RBAC)]({{< relref "/operate/rc/security/access-control/data-access-control/role-based-access-control.md" >}}), you create roles and assign users to those roles to grant different levels of access to the database.

- [Enable RBAC]({{< relref "/operate/rc/security/access-control/data-access-control/role-based-access-control" >}})
- [Configure ACLs]({{< relref "/operate/rc/security/access-control/data-access-control/configure-acls" >}})
- [Create roles]({{< relref "/operate/rc/security/access-control/data-access-control/create-roles" >}})
- [Create and edit database users]({{< relref "/operate/rc/security/access-control/data-access-control/create-assign-users" >}})
- [Active-Active roles]({{< relref "/operate/rc/security/access-control/data-access-control/active-active-roles" >}})