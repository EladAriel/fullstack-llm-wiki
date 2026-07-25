---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/oidc/workforce/workforce-external-provider.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================

# Configure OIDC for Workforce Authentication

To configure Workforce Identity Federation with :abbr:`OIDC (OpenID Connect)`, register your OIDC application with an external |idp-abbr|, such as Okta or Microsoft Entra ID. This ensures secure authentication and facilitates user management.

## About this Task

Workforce Identity Federation uses OIDC. You can use any external |idp| that supports the OIDC standard.

You can configure your OIDC application for the following grant types:

- Authorization Code Flow with :abbr:`PKCE (Proof Key of Code Exchange)`
- Device Authorization Flow
MongoDB recommends that you use Authorization Code Flow with PKCE for increased security. Use Device Authorization Flow only if your users need to access the database from machines with no browser.

> **Note:** Workforce Identity Federation supports only :abbr:`JWT (JSON Web Token)` for
authentication. It doesn't support opaque access tokens.

The following procedures provide detailed configuration instructions for Microsoft Entra ID and Okta, and generic configuration instructions for other external |idps|.

## Before you Begin

- To use Okta as an |idp|, you must have an `Okta account
<https://www.okta.com/>`__.

- To use Microsoft Entra ID as an |idp|, you must have a `Microsoft
Azure account <https://azure.microsoft.com/en-us/get-started/azure-portal>`__.

## Steps

## Next Steps

- `configure-oidc`
- `database-user-workforce`
## Learn More

- [Okta account](https://www.okta.com/)_
- [Microsoft Azure](https://azure.microsoft.com/en-us/get-started/azure-portal)_
