---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/12-2025/12-06-2025-ldap-authentication-support.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.908847Z"
---
# 12 06 2025 Ldap Authentication Support

---
title: "12.06.2025: LDAP Authentication Support"
description: Available in Phoenix 12.20+
---


## LDAP Authentication

Phoenix now supports authentication against LDAP directories, enabling integration with enterprise identity infrastructure including:

- **Microsoft Active Directory**
- **OpenLDAP**
- **389 Directory Server**
- Any LDAP v3 compliant directory

**Key Features:**

* Authenticate users with their corporate directory credentials
* Automatic user provisioning on first login
* Group-based role mapping (ADMIN, MEMBER, VIEWER)
* Support for nested groups in Active Directory
* Multi-server failover for high availability
* TLS encryption with StartTLS and LDAPS support
* Mutual TLS (client certificate) authentication
* Custom CA certificate support for internal PKI

**Configuration Highlights:**

* Simple setup with just `PHOENIX_LDAP_HOST` and `PHOENIX_LDAP_USER_SEARCH_BASE`
* Flexible group-to-role mappings via JSON configuration
* Support for both AD-style `memberOf` and POSIX group lookups
* Optional immutable unique identifiers for user tracking

#### More Information in our documentation:

<Card title="LDAP Authentication | Phoenix" icon="book" href="/docs/phoenix/self-hosting/features/authentication#configuring-ldap-authentication" horizontal description="LDAP authentication setup"/>


