---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/appendix-obsolete-default-roles.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

## Default Roles Renamed to Predefined Roles

default-roles

PostgreSQL 13 and below used the term Default Roles. However, as these roles are not able to actually be changed and are installed as part of the system at initialization time, the more appropriate term to use is Predefined Roles. See `predefined-roles` for current documentation regarding Predefined Roles, and the release notes for PostgreSQL 14 for details on this change.
