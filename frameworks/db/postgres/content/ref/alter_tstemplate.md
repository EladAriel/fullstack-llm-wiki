---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_tstemplate.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.577614Z"
---
ALTER TEXT SEARCH TEMPLATE
 

 
  
# ALTER TEXT SEARCH TEMPLATE

  7
  SQL - Language Statements
 

 
  
# ALTER TEXT SEARCH TEMPLATE

  change the definition of a text search template
 

 

ALTER TEXT SEARCH TEMPLATE name RENAME TO new_name
ALTER TEXT SEARCH TEMPLATE name SET SCHEMA new_schema

 

 
  
# Description

  
   ALTER TEXT SEARCH TEMPLATE changes the definition of
   a text search template.  Currently, the only supported functionality
   is to change the template's name.
  

  
   You must be a superuser to use ALTER TEXT SEARCH TEMPLATE.
  

 

 
  
# Parameters

  
   
    name
    
     
      The name (optionally schema-qualified) of an existing text search template.
     

    
   

   
    new_name
    
     
      The new name of the text search template.
     

    
   

   
    new_schema
    
     
      The new schema for the text search template.
     

    
   
 
 

 
  
# Compatibility

  
   There is no ALTER TEXT SEARCH TEMPLATE statement in
   the SQL standard.
  

 

 
  
# See Also
