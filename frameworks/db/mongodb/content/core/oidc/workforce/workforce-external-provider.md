---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/oidc/workforce/workforce-external-provider.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.827025Z"
---
.. _workforce-external-provider:

# Configure OIDC for Workforce Authentication

.. default-domain:: mongodb

**facet:** :name: genre
   :values: tutorial

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

To configure Workforce Identity Federation with 
:abbr:`OIDC (OpenID Connect)`, register your OIDC application with an 
external |idp-abbr|, such as Okta or Microsoft Entra ID. This 
ensures secure authentication and facilitates user management.

## About this Task

Workforce Identity Federation uses OIDC. You can use any external |idp|
that supports the OIDC standard.

You can configure your OIDC application for the following grant types:

- Authorization Code Flow with :abbr:`PKCE (Proof Key of Code Exchange)`
- Device Authorization Flow

MongoDB recommends that you use Authorization Code Flow with PKCE for increased
security. Use Device Authorization Flow only if your users need
to access the database from machines with no browser.

**note:** Workforce Identity Federation supports only :abbr:`JWT (JSON Web Token)` for 
   authentication. It doesn't support opaque access tokens.

The following procedures provide detailed configuration instructions for Microsoft 
Entra ID and Okta, and generic configuration instructions for other external |idps|.

## Before you Begin

- To use Okta as an |idp|, you must have an `Okta account 
  <https://www.okta.com/>`__.

- To use Microsoft Entra ID as an |idp|, you must have a `Microsoft 
  Azure account <https://azure.microsoft.com/en-us/get-started/azure-portal>`__.

## Steps

**tabs:** .. tab:: Microsoft Entra ID
      :tabid: azure

      .. include:: includes/oidc-azure-instructions.rst
   
   .. tab:: Okta
      :tabid: okta

      .. include:: includes/oidc-okta-instructions.rst

   .. tab:: Generic
      :tabid: generic

      .. include:: includes/oidc-generic-instructions.rst

## Next Steps

- :ref:`configure-oidc`
- :ref:`database-user-workforce`

## Learn More

- `Okta account <https://www.okta.com/>`__
- `Microsoft Azure <https://azure.microsoft.com/en-us/get-started/azure-portal>`__