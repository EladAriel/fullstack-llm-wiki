---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/security/access-control/manage-passwords/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Set password policies
alwaysopen: false
categories:
- docs
- operate
- rs
description: Set password policies.
hideListLinks: true
linkTitle: Set password policies
toc: 'true'
weight: 30
url: '/operate/rs/8.0/security/access-control/manage-passwords/'
---

Redis Software provides several ways to manage the passwords of local accounts, including:

- [Password complexity rules]({{< relref "/operate/rs/8.0/security/access-control/manage-passwords/password-complexity-rules" >}})

- [Password expiration]({{< relref "/operate/rs/8.0/security/access-control/manage-passwords/password-expiration" >}})

- [Password rotation]({{< relref "/operate/rs/8.0/security/access-control/manage-passwords/rotate-passwords" >}})

You can also manage a user's ability to [sign in]({{< relref "/operate/rs/8.0/security/access-control/manage-users/login-lockout#user-login-lockout" >}}) and control [session timeout]({{< relref "/operate/rs/8.0/security/access-control/manage-users/login-lockout#session-timeout" >}}).

To enforce more advanced password policies, we recommend using [LDAP integration]({{< relref "/operate/rs/8.0/security/access-control/ldap" >}}) with an external identity provider, such as Active Directory.

{{<note>}}
Redis Software securely stores all user passwords using a cryptographic hash function. The default password hashing algorithm is `SHA-256`, but you can [change the password hashing algorithm]({{<relref "/operate/rs/8.0/security/access-control/manage-passwords/password-hashing-algorithm">}}) to `PBKDF2` as of Redis Software version 7.8.6-13.
{{</note>}}
