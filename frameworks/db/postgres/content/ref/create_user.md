---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/create_user.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.580593Z"
---
CREATE USER
 

 
  
# CREATE USER

  7
  SQL - Language Statements
 

 
  
# CREATE USER

  define a new database role
 

 

CREATE USER name [ [ WITH ] option [ ... ] ]

where option can be:

      SUPERUSER | NOSUPERUSER
    | CREATEDB | NOCREATEDB
    | CREATEROLE | NOCREATEROLE
    | INHERIT | NOINHERIT
    | LOGIN | NOLOGIN
    | REPLICATION | NOREPLICATION
    | BYPASSRLS | NOBYPASSRLS
    | CONNECTION LIMIT connlimit
    | [ ENCRYPTED ] PASSWORD 'password' | PASSWORD NULL
    | VALID UNTIL 'timestamp'
    | IN ROLE role_name [, ...]
    | ROLE role_name [, ...]
    | ADMIN role_name [, ...]
    | SYSID uid

 

 
  
# Description

  
   CREATE USER is now an alias for
   CREATE ROLE.
   The only difference is that when the command is spelled
   CREATE USER, LOGIN is assumed
   by default, whereas NOLOGIN is assumed when
   the command is spelled
   CREATE ROLE.
  

 

 
  
# Compatibility

  
   The CREATE USER statement is a
   PostgreSQL extension.  The SQL standard
   leaves the definition of users to the implementation.
  

 

 
  
# See Also
