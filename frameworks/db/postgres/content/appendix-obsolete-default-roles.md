---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/appendix-obsolete-default-roles.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## Default Roles Renamed to Predefined Roles

default-roles

PostgreSQL 13 and below used the term Default Roles. However, as these roles are not able to actually be changed and are installed as part of the system at initialization time, the more appropriate term to use is Predefined Roles. See `predefined-roles` for current documentation regarding Predefined Roles, and the release notes for PostgreSQL 14 for details on this change.
