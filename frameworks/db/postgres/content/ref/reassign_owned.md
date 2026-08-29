---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/reassign_owned.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.613482Z"
---
REASSIGN OWNED
 

 
  
# REASSIGN OWNED

  7
  SQL - Language Statements
 

 
  
# REASSIGN OWNED

  change the ownership of database objects owned by a database role
 

 

REASSIGN OWNED BY { old_role | CURRENT_ROLE | CURRENT_USER | SESSION_USER } [, ...]
               TO { new_role | CURRENT_ROLE | CURRENT_USER | SESSION_USER }

 

 
  
# Description

  
   REASSIGN OWNED instructs the system to change
   the ownership of database objects owned by any of the
   old_roles to
   new_role.
  

 

 
  
# Parameters

  
   
    old_role
    
     
      The name of a role. The ownership of all the objects within the
      current database, and of all shared objects (databases, tablespaces),
      owned by this role will be reassigned to
      new_role. Subscriptions,
      although stored in a shared catalog, belong to a specific database
      and are reassigned only when REASSIGN OWNED is executed
      in that database.
     

    
   

   
    new_role
    
     
      The name of the role that will be made the new owner of the
      affected objects.
     

    
   
  
 

 
  
# Notes

  
   REASSIGN OWNED is often used to prepare for the
   removal of one or more roles. Because REASSIGN
   OWNED does not affect objects within other databases,
   it is usually necessary to execute this command in each database
   that contains objects owned by a role that is to be removed.
  

  
   REASSIGN OWNED requires membership on both the
   source role(s) and the target role.
  

  
   The DROP OWNED command is an alternative that
   simply drops all the database objects owned by one or more roles.
  

  
   The REASSIGN OWNED command does not affect any
   privileges granted to
   the old_roles on objects
   that are not owned by them.  Likewise, it does not affect default
   privileges created with ALTER DEFAULT PRIVILEGES.
   Use DROP OWNED to revoke such privileges.
  

  
   See  for more discussion.
  

 

 
  
# Compatibility

  
   The REASSIGN OWNED command is a
   PostgreSQL extension.
  

 

 
  
# See Also
