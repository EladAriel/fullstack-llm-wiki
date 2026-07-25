---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/oidc/workforce/database-user-workforce.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================================

# Authorize Users with Workforce Identity Federation

You can add a database user to MongoDB using Workforce authentication. This process allows your organization’s |idp-abbr| to manage user access, ensuring secure and centralized authentication for database operations.

## Before you Begin

- You must `workforce-external-provider`.
- You must `configure-oidc`.
.. include:: /includes/note-oidc-add-users-internal-auth.rst

## Steps

.. include:: /includes/oidc-add-user.rst

## Next Steps

You can connect an application to MongoDB using Workforce Identity Federation in the following ways:

- :compass:`Compass </connect/#connect-with-openid-connect>`
- :mongosh:`MongoDB Shell </connect/#connect-with-openid-connect>`
For more details on MongoDB Shell OIDC options, see :mongosh:`Authentication Options </reference/options/#std-option-mongosh.--oidcFlows>`

## Learn More

- `workforce`
- `workload`
