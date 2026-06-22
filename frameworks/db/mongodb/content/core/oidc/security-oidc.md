---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/oidc/security-oidc.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================================

# Authentication and Authorization with OIDC/OAuth 2.0

MongoDB Enterprise supports OpenID Connect (OIDC) and OAuth 2.0 authentication and authorization for both human users and applications. These protocols enable Workforce and Workload Identity Federation, which streamline authentication and authorization by integrating with external |idps|. This lets you simplify your security management and enhance your system's scalability and flexibility.

> **Important:** .. include:: includes/fact-OIDC-linux-only.rst

## Use Cases

Workload and Workforce Identity Federation use OIDC and OAuth 2.0 as follows:

- Workforce Identity Federation uses OIDC to enable human users to
authenticate and get authorized using an external |idp|.

- Workload Identity Federation uses OAuth 2.0 to enable your applications to
access MongoDB using external programmatic identities such as Azure Service Principals, Azure Managed Identities, and Google Service Accounts.

## Behavior

To use Workforce and Workload Identity Federation, you must use MongoDB Enterprise and have MongoDB 7.0.11 or later.

.. include:: /includes/fact-confirm-enterprise-binaries.rst

## Get Started

Select an authentication method to get started:

## Contents

- Workforce (Humans) </core/oidc/workforce>
- Workload (Applications) </core/oidc/workload>
