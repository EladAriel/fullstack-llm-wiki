---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_statistics.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.620686Z"
---
DROP STATISTICS
 

 
  
# DROP STATISTICS

  7
  SQL - Language Statements
 

 
  
# DROP STATISTICS

  remove extended statistics
 

 

DROP STATISTICS [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP STATISTICS removes statistics object(s) from the
   database.  Only the statistics object's owner, the schema owner, or a
   superuser can drop a statistics object.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the statistics object does not exist. A notice
      is issued in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of the statistics object to drop.
     

    
   

   
    CASCADE
    RESTRICT

    
     
      These key words do not have any effect, since there are no dependencies
      on statistics.
     

    
   

  
 

 
  
# Examples

  
   To destroy two statistics objects in different schemas, without failing
   if they don't exist:

```

DROP STATISTICS IF EXISTS
    accounting.users_uid_creation,
    public.grants_user_role;

```

 

 
  
# Compatibility

  
   There is no DROP STATISTICS command in the SQL standard.
  

 

 
  
# See Also
