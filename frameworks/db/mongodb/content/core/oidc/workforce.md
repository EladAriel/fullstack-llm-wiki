---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/oidc/workforce.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================================

# Workforce Identity Federation with OpenID Connect

Workforce Identity Federation uses OpenID Connect (OIDC) to enable human users to authenticate and get authorized using an external |idp-abbr|. You can use Workforce Identity Federation to enhance security and simplify user management.

## Use Cases

With Workforce Identity Federation, you can:

- Manage your workforce access to MongoDB deployments through your existing
|idp|.

- Enforce security policies such as password complexity, credential rotation,
and multi-factor authentication within your |idp|.

- Grant access for a group of users or a single user.
## Behavior

You must use MongoDB Enterprise and have MongoDB 7.0.11 or later.

.. include:: /includes/fact-confirm-enterprise-binaries.rst

## Get Started

To configure and use Workforce Identity Federation, you must perform the following tasks:

1. `workforce-external-provider`
Register your OIDC application with an |idp| that supports the OIDC standard, such as Microsoft Entra ID, Okta, or Ping Identity.

#. `configure-oidc`

Configure your MongoDB server to use Workforce Identity Federation with OIDC.

#. `database-user-workforce`

Specify privileges for workforce identity principals by adding roles to MongoDB (for OIDC, external authorization, or both) or adding database users to MongoDB (for database-managed authorization).

## Contents

- /core/oidc/workforce/workforce-external-provider
- /core/oidc/workforce/configure-oidc
- /core/oidc/workforce/database-user-workforce
