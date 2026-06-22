---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/privilege-actions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Privilege Actions

Privilege actions define the operations a user can perform on a `resource <resource-document>`. A MongoDB `privilege <privileges>` comprises a `resource <resource-document>` and the permitted actions. This page lists available actions grouped by common purpose.

MongoDB provides built-in roles with pre-defined pairings of resources and permitted actions. For lists of the actions granted, see:

- `<built-in-roles>`
- :ref:`Built-In Roles on Atlas
<mongodb-users-roles-and-privileges>`

To define custom roles, see:

- :ref:`Create a User-Defined Role in Self-Managed Deployments
<create-user-defined-role>`

- `Create User-Defined Roles in Atlas <add-mongodb-roles>`
## Query and Write Actions

## Database Management Actions

## Deployment Management Actions

## Change Stream Actions

## Replication Actions

## Sharding Actions

## Server Administration Actions

## Session Actions

## {+fts+} Index Actions

The following actions enable users to run `{+fts+} Database Commands <db-commands-atlas-search>`. These actions are only relevant for deployments hosted on :atlas:`MongoDB Atlas </>`.

## Diagnostic Actions

## Internal Actions
