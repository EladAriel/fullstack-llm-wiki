---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_tsparser.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.554268Z"
---
DROP TEXT SEARCH PARSER
 

 
  
# DROP TEXT SEARCH PARSER

  7
  SQL - Language Statements
 

 
  
# DROP TEXT SEARCH PARSER

  remove a text search parser
 

 

DROP TEXT SEARCH PARSER [ IF EXISTS ] name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP TEXT SEARCH PARSER drops an existing text search
   parser.  You must be a superuser to use this command.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the text search parser does not exist.
      A notice is issued in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of an existing text search parser.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the text search parser,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the text search parser if any objects depend on it.
      This is the default.
     

    
   
  
 

 
  
# Examples

  
   Remove the text search parser my_parser:

```

DROP TEXT SEARCH PARSER my_parser;

```

   This command will not succeed if there are any existing text search
   configurations that use the parser.  Add CASCADE to
   drop such configurations along with the parser.
  

 

 
  
# Compatibility

  
   There is no DROP TEXT SEARCH PARSER statement in the
   SQL standard.
  

 

 
  
# See Also
