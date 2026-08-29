---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_tablespace.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.620445Z"
---
DROP TABLESPACE
 

 
  
# DROP TABLESPACE

  7
  SQL - Language Statements
 

 
  
# DROP TABLESPACE

  remove a tablespace
 

 

DROP TABLESPACE [ IF EXISTS ] name

 

 
  
# Description

  
   DROP TABLESPACE removes a tablespace from the system.
  

  
   A tablespace can only be dropped by its owner or a superuser.
   The tablespace must be empty of all database objects before it can be
   dropped. It is possible that objects in other databases might still reside
   in the tablespace even if no objects in the current database are using
   the tablespace.  Also, if the tablespace is listed in the  setting of any active session, the
   DROP might fail due to temporary files residing in the
   tablespace.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the tablespace does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name of a tablespace.
     

    
   
  
 

 
  
# Notes

   
    DROP TABLESPACE cannot be executed inside a transaction block.
   

 

 
  
# Examples

  
   To remove tablespace mystuff from the system:

```

DROP TABLESPACE mystuff;

```

 

 
  
# Compatibility

  
   DROP TABLESPACE is a PostgreSQL
   extension.
  

 

 
  
# See Also
