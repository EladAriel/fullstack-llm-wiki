---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_group.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.532146Z"
---
ALTER GROUP
 

 
  
# ALTER GROUP

  7
  SQL - Language Statements
 

 
  
# ALTER GROUP

  change role name or membership
 

 

ALTER GROUP role_specification ADD USER user_name [, ... ]
ALTER GROUP role_specification DROP USER user_name [, ... ]

where role_specification can be:

    role_name
  | CURRENT_ROLE
  | CURRENT_USER
  | SESSION_USER

ALTER GROUP group_name RENAME TO new_name

 

 
  
# Description

  
   ALTER GROUP changes the attributes of a user group.
   This is an obsolete command, though still accepted for backwards
   compatibility, because groups (and users too) have been superseded by the
   more general concept of roles.
  

  
   The first two variants add users to a group or remove them from a group.
   (Any role can play the part of either a user or a
   group for this purpose.)  These variants are effectively
   equivalent to granting or revoking membership in the role named as the
   group; so the preferred way to do this is to use
   GRANT or
   REVOKE. Note that
   GRANT and REVOKE have additional
   options which are not available with this command, such as the ability
   to grant and revoke ADMIN OPTION, and the ability to
   specify the grantor.
  

  
   The third variant changes the name of the group.  This is exactly
   equivalent to renaming the role with
   ALTER ROLE.
  

 

 
  
# Parameters

  
   
    group_name
    
     
      The name of the group (role) to modify.
     

    
   

   
    user_name
    
     
      Users (roles) that are to be added to or removed from the group.
      The users must already exist; ALTER GROUP does not
      create or drop users.
     

    
   

   
    new_name
    
     
      The new name of the group.
     

    
   
  
 

 
  
# Examples

  
   Add users to a group:

```

ALTER GROUP staff ADD USER karl, john;

```

   Remove a user from a group:

```

ALTER GROUP workers DROP USER beth;

```

 

 
  
# Compatibility

  
   There is no ALTER GROUP statement in the SQL
   standard.
  

 

 
  
# See Also
