---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_language.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.600221Z"
---
ALTER LANGUAGE
 

 
  
# ALTER LANGUAGE

  7
  SQL - Language Statements
 

 
  
# ALTER LANGUAGE

  change the definition of a procedural language
 

 

ALTER [ PROCEDURAL ] LANGUAGE name RENAME TO new_name
ALTER [ PROCEDURAL ] LANGUAGE name OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }

 

 
  
# Description

  
   ALTER LANGUAGE changes the definition of a
   procedural language.  The only functionality is to rename the language or
   assign a new owner.  You must be superuser or owner of the language to
   use ALTER LANGUAGE.
  

 

 
  
# Parameters

  
   
    name
    
     
      Name of a language
     

    
   

   
    new_name
    
     
      The new name of the language
     

    
   

   
    new_owner
    
     
      The new owner of the language
     

    
   
  
 

 
  
# Compatibility

  
   There is no ALTER LANGUAGE statement in the SQL
   standard.
  

 

 
  
# See Also
