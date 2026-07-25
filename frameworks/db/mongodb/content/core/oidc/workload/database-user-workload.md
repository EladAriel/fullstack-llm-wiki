---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/oidc/workload/database-user-workload.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================================

# Authorize Users with Workload Identity Federation

You can add a database user to MongoDB using Workload Identity Federation. This approach enables your organization’s |idp| to manage user access, ensuring secure, centralized authentication for database operations.

## Before you Begin

- You must `workload-external-provider`.
- You must `configure-mongodb-workload`.
.. include:: /includes/note-oidc-add-users-internal-auth.rst

## Steps

.. include:: /includes/oidc-add-user.rst

## Next Steps

You can connect an application to MongoDB using Workload Identity Federation with the following supported drivers:

- :driver:`Java </java/sync/current/fundamentals/enterprise-auth/#std-label-mongodb-oidc>`
- :driver:`Kotlin </kotlin/coroutine/upcoming/fundamentals/enterprise-auth/#std-label-kotlin-oidc>`
- :driver:`Node.js </node/current/fundamentals/authentication/enterprise-mechanisms/#mongodb-oidc>`
- [PyMongo](https://www.mongodb.com/docs/languages/python/pymongo-driver/security/enterprise-authentication/#mongodb-oidc)_
- :driver:`TypeScript </typescript>`
- :driver:`C# </csharp/current/fundamentals/enterprise-authentication/#std-label-csharp-mongodb-oidc>`
- :driver:`Go </go/current/fundamentals/enterprise-auth/#mongodb-oidc>`
- `Rust <rust-authentication-oidc>`
- :website:`Scala </docs/languages/scala/scala-driver/>`
## Learn More

- `workload`
- `workforce`
