---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/oidc/workload.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# Workload Identity Federation with OAuth 2.0

Workload Identity Federation uses OAuth 2.0 to enable your applications to access MongoDB using external programmatic identities such as Azure Service Principals, Azure Managed Identities, and Google Service Accounts.

> **Important:** .. include:: includes/fact-OIDC-linux-only.rst

## Use Cases

With Workload Identity Federation, you can:

- Manage your application's access to MongoDB deployments through your
existing cloud provider or |idp-abbr|.

- Enforce security policies such as role-based access control, credential
rotation, and workload-specific permissions.

- Grant access to specific applications, containers, or virtual machines
without managing individual service accounts.

## Behavior

- To use Workload Identity Federation, you must use MongoDB
Enterprise and have MongoDB 7.0.11 or later.

.. include:: /includes/fact-confirm-enterprise-binaries.rst

- Workload Identity Federation allows your applications to access MongoDB
clusters with OAuth 2.0 access tokens. The access tokens can be issued by any external |idp|, including Azure Entra ID and Google Cloud Platform.

- MongoDB stores user identifiers and privileges, but not secrets.
## Get Started

To configure and use Workload Identity Federation, perform the following tasks:

1. `workload-external-provider`
Register your OAuth 2.0 application with an |idp| that supports the OAuth 2.0 standard, such as Azure Service Principals, Azure Managed Identities and Google Service Accounts.

#. `configure-mongodb-workload`

Configure your MongoDB server to use Workload Identity Federation with OAuth 2.0.

#. `database-user-workload`

Specify privileges for workload identity principals by adding roles to MongoDB (for OAuth, external authorization, or both) or adding database users to MongoDB (for database-managed authorization).

## Details

MongoDB Drivers support two types of authentication flow for Workload Identity Federation: Built-in Authentication and Callback Authentication.

### Built-in Authentication

You can use built-in authentication if you deploy your application on a supported infrastructure with a supported principal type. Your application can access MongoDB clusters without supplying a password or manually requesting a JSON Web Tokens (JWT) from your cloud provider's metadata service. Instead, your chosen MongoDB driver uses your existing principal identifier to request a JWT access token under the hood, which is then passed to the Atlas cluster automatically when your application connects.

For more implementation details, see your chosen :driver:`Driver's documentation </>`.

Built-in Authentication Supported Infrastructure and Principal Types ````````````````````````````````````````````````````````````````````

### Callback Authentication

You can use callback authentication with any service supporting OAuth 2.0 access tokens. Workload Identity Federation calls a callback method, in which you can request the required JWT from your authorization server or cloud provider that you must pass when your application connects to MongoDB with Workload Identity Federation.

Review your chosen :driver:`driver's documentation </>` for more  implementation details.

## Contents

- /core/oidc/workload/workload-external-provider
- /core/oidc/workload/configure-mongodb-workload
- /core/oidc/workload/database-user-workload
