---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_tstemplate.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.545982Z"
---
DROP TEXT SEARCH TEMPLATE
 

 
  
# DROP TEXT SEARCH TEMPLATE

  7
  SQL - Language Statements
 

 
  
# DROP TEXT SEARCH TEMPLATE

  remove a text search template
 

 

DROP TEXT SEARCH TEMPLATE [ IF EXISTS ] name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP TEXT SEARCH TEMPLATE drops an existing text search
   template.  You must be a superuser to use this command.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the text search template does not exist.
      A notice is issued in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of an existing text search
      template.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the text search template,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the text search template if any objects depend on it.
      This is the default.
     

    
   
  
 

 
  
# Examples

  
   Remove the text search template thesaurus:

```

DROP TEXT SEARCH TEMPLATE thesaurus;

```

   This command will not succeed if there are any existing text search
   dictionaries that use the template.  Add CASCADE to
   drop such dictionaries along with the template.
  

 

 
  
# Compatibility

  
   There is no DROP TEXT SEARCH TEMPLATE statement in the
   SQL standard.
  

 

 
  
# See Also
