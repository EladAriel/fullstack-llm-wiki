---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/appendix-obsolete-default-roles.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.361318Z"
---
# Default Roles Renamed to Predefined Roles

   
     default-roles
   

   
    PostgreSQL 13 and below used the term Default Roles.  However, as these
    roles are not able to actually be changed and are installed as part of the
    system at initialization time, the more appropriate term to use is Predefined Roles.
    See  for current documentation regarding
    Predefined Roles, and the release notes for
    PostgreSQL 14 for details on this change.
