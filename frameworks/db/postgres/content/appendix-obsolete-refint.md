---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/appendix-obsolete-refint.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.361774Z"
---
# refint Extension Removed

   
    refint
   

   
    PostgreSQL 19 and below shipped an extension
    named refint (part of the spi contrib
    module) that provided the trigger functions
    check_primary_key and
    check_foreign_key as an early way to enforce
    referential integrity.  This functionality was long superseded by the
    built-in foreign key mechanism (see ),
    and the extension was removed in PostgreSQL 20.
