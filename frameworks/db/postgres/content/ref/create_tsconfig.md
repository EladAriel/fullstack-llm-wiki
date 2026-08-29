---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/create_tsconfig.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.542543Z"
---
CREATE TEXT SEARCH CONFIGURATION
 

 
  
# CREATE TEXT SEARCH CONFIGURATION

  7
  SQL - Language Statements
 

 
  
# CREATE TEXT SEARCH CONFIGURATION

  define a new text search configuration
 

 

CREATE TEXT SEARCH CONFIGURATION name (
    PARSER = parser_name |
    COPY = source_config
)

 

 
  
# Description

  
   CREATE TEXT SEARCH CONFIGURATION creates a new text
   search configuration.  A text search configuration specifies a text
   search parser that can divide a string into tokens, plus dictionaries
   that can be used to determine which tokens are of interest for searching.
  

  
   If only the parser is specified, then the new text search configuration
   initially has no mappings from token types to dictionaries, and therefore
   will ignore all words.  Subsequent ALTER TEXT SEARCH
   CONFIGURATION commands must be used to create mappings to
   make the configuration useful.  Alternatively, an existing text search
   configuration can be copied.
  

  
   If a schema name is given then the text search configuration is created in
   the specified schema.  Otherwise it is created in the current schema.
  

  
   The user who defines a text search configuration becomes its owner.
  

  
   Refer to  for further information.
  

 

 
  
# Parameters

  
   
    name
    
     
      The name of the text search configuration to be created.  The name can be
      schema-qualified.
     

    
   

   
    parser_name
    
     
      The name of the text search parser to use for this configuration.
     

    
   

   
    source_config
    
     
      The name of an existing text search configuration to copy.
     

    
   
  
 

 
  
# Notes

  
   The PARSER and COPY options are mutually
   exclusive, because when an existing configuration is copied, its
   parser selection is copied too.
  

 

 
  
# Compatibility

  
   There is no CREATE TEXT SEARCH CONFIGURATION statement
   in the SQL standard.
  

 

 
  
# See Also
