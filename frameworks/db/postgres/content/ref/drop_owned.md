---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_owned.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.592050Z"
---
DROP OWNED
 

 
  
# DROP OWNED

  7
  SQL - Language Statements
 

 
  
# DROP OWNED

  remove database objects owned by a database role
 

 

DROP OWNED BY { name | CURRENT_ROLE | CURRENT_USER | SESSION_USER } [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP OWNED drops all the objects within the current
   database that are owned by one of the specified roles. Any
   privileges granted to the given roles on objects in the current
   database or on shared objects (databases, tablespaces, configuration
   parameters) will also be revoked.
  

 

 
  
# Parameters

  
   
    name
    
     
      The name of a role whose objects will be dropped, and whose
      privileges will be revoked.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the affected objects,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the objects owned by a role if any other database
      objects depend on one of the affected objects. This is the default.
     

    
   
  
 

 
  
# Notes

  
   DROP OWNED is often used to prepare for the
   removal of one or more roles. Because DROP OWNED
   only affects the objects in the current database, it is usually
   necessary to execute this command in each database that contains
   objects owned by a role that is to be removed.
  

  
   Using the CASCADE option might make the command
   recurse to objects owned by other users.
  

  
   The REASSIGN OWNED command is an alternative that
   reassigns the ownership of all the database objects owned by one or
   more roles.  However, REASSIGN OWNED does not deal with
   privileges for other objects.
  

  
   Databases and tablespaces owned by the role(s) will not be removed.
  

  
   See  for more discussion.
  

 

 
  
# Compatibility

  
   The DROP OWNED command is a
   PostgreSQL extension.
  

 

 
  
# See Also
