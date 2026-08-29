---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_schema.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.547629Z"
---
ALTER SCHEMA
 

 
  
# ALTER SCHEMA

  7
  SQL - Language Statements
 

 
  
# ALTER SCHEMA

  change the definition of a schema
 

 

ALTER SCHEMA name RENAME TO new_name
ALTER SCHEMA name OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }

 

 
  
# Description

  
   ALTER SCHEMA changes the definition of a schema.
  

  
   You must own the schema to use ALTER SCHEMA.
   To rename a schema you must also have the
   CREATE privilege for the database.
   To alter the owner, you must be able to SET ROLE to the
   new owning role, and that role must have the
   CREATE privilege for the database.
   (Note that superusers have all these privileges automatically.)
  

 

 
  
# Parameters

  
   
    name
    
     
      The name of an existing schema.
     

    
   

   
    new_name
    
     
      The new name of the schema.  The new name cannot
      begin with pg_, as such names
      are reserved for system schemas.
     

    
   

   
    new_owner
    
     
      The new owner of the schema.
     

    
   
  
 

 
  
# Compatibility

  
   There is no ALTER SCHEMA statement in the SQL
   standard.
  

 

 
  
# See Also
