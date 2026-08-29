---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_trigger.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.531861Z"
---
DROP TRIGGER
 

 
  
# DROP TRIGGER

  7
  SQL - Language Statements
 

 
  
# DROP TRIGGER

  remove a trigger
 

 

DROP TRIGGER [ IF EXISTS ] name ON table_name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP TRIGGER removes an existing
   trigger definition. To execute this command, the current
   user must be the owner of the table for which the trigger is defined.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the trigger does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name of the trigger to remove.
     

    
   

   
    table_name
    
     
      The name (optionally schema-qualified) of the table for which
      the trigger is defined.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the trigger,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the trigger if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  
   Destroy the trigger if_dist_exists on the table
   films:

```

DROP TRIGGER if_dist_exists ON films;

```

 

 
  
# Compatibility

  
   The DROP TRIGGER statement in
   PostgreSQL is incompatible with the SQL
   standard.  In the SQL standard, trigger names are not local to
   tables, so the command is simply DROP TRIGGER
   name.
  

 

 
  
# See Also
