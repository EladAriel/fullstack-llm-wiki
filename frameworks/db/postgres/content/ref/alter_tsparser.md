---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_tsparser.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.575326Z"
---
ALTER TEXT SEARCH PARSER
 

 
  
# ALTER TEXT SEARCH PARSER

  7
  SQL - Language Statements
 

 
  
# ALTER TEXT SEARCH PARSER

  change the definition of a text search parser
 

 

ALTER TEXT SEARCH PARSER name RENAME TO new_name
ALTER TEXT SEARCH PARSER name SET SCHEMA new_schema

 

 
  
# Description

  
   ALTER TEXT SEARCH PARSER changes the definition of
   a text search parser.  Currently, the only supported functionality
   is to change the parser's name.
  

  
   You must be a superuser to use ALTER TEXT SEARCH PARSER.
  

 

 
  
# Parameters

  
   
    name
    
     
      The name (optionally schema-qualified) of an existing text search parser.
     

    
   

   
    new_name
    
     
      The new name of the text search parser.
     

    
   

   
    new_schema
    
     
      The new schema for the text search parser.
     

    
   
 
 

 
  
# Compatibility

  
   There is no ALTER TEXT SEARCH PARSER statement in
   the SQL standard.
  

 

 
  
# See Also
