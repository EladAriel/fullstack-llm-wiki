---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/security/access-control/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Access control
alwaysopen: false
categories:
- docs
- operate
- rs
description: An overview of access control in Redis Enterprise Software.
hideListLinks: false
linkTitle: Access control
weight: 10
url: '/operate/rs/7.8/security/access-control/'
---

Redis Enterprise Software lets you use role-based access control (RBAC) to manage users' access privileges. RBAC requires you to do the following:

1. Create roles and define each role's access privileges.

1. Create users and assign roles to them. The assigned role determines the user's access privileges.

## Cluster access versus database access

Redis Enterprise allows two separate paths of access:

- **Cluster access** allows performing management-related actions, such as creating databases and viewing statistics.

- **Database access** allows performing data-related actions, like reading and writing data in a database.

You can grant cluster access, database access, or both to each role. These roles let you differentiate between users who can access databases and users who can access cluster management, according to your organization's security needs.

The following diagram shows three different options for roles and users:

{{<image filename="images/rs/rbac-diagram.png" alt="Role-based access control diagram.">}}

- Role A was created with permission to access the cluster and perform management-related actions. Because user A was assigned role A, they can access the cluster but cannot access databases.

- Role B was created with permission to access one or more databases and perform data-related actions. Because user B was assigned role B, they cannot access the cluster but can access databases.

- Role C was created with cluster access and database access permissions. Because user C was assigned role C, they can access the cluster and databases.

## Default database access

When you create a database, [default user access]({{< relref "/operate/rs/7.8/security/access-control/manage-users/default-user" >}}) is enabled automatically.

If you set up role-based access controls for your database and don't require compatibility with versions earlier than Redis 6, you can [deactivate the default user]({{< relref "/operate/rs/7.8/security/access-control/manage-users/default-user" >}}).

{{<warning>}}
Before you [deactivate default user access]({{< relref "/operate/rs/7.8/security/access-control/manage-users/default-user#deactivate-default-user" >}}), make sure the role associated with the database is [assigned to a user]({{< relref "/operate/rs/7.8/security/access-control/create-users#assign-roles-to-users" >}}). Otherwise, the database will be inaccessible.
{{</warning>}}

## More info
