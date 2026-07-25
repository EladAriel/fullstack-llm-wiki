---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/system-collections.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================

# System Collections

## Synopsis

MongoDB stores system information in collections that use the `<database>.system.*` `namespace`, which MongoDB reserves for internal use. Do not create collections that begin with `system`.

MongoDB also stores some additional instance-local metadata in the `local database <replica-set-local-database>` `local.replset.*` namespace, specifically for replication purposes and in the `config database <config-database>` for `sessions information <sessions>`.

|service-fullname| and other MongoDB cloud services store essential operational data in dedicated databases that use the prefix `__mdb_internal_*`. **Do not access or modify databases with this prefix.** We recommend that you ignore these namespaces in administrative tools. For more information on these cloud-specific databases, see :atlas:`Internal Databases </reference/internal-database>`.

## Collections

System collections include these collections stored in the `admin` database:

System collections include these collections stored in the `config` database:

### Database-Specific Collections

System collections also include these collections stored directly in each database:
