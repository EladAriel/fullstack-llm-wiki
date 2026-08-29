---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_tsdictionary.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.554053Z"
---
DROP TEXT SEARCH DICTIONARY
 

 
  
# DROP TEXT SEARCH DICTIONARY

  7
  SQL - Language Statements
 

 
  
# DROP TEXT SEARCH DICTIONARY

  remove a text search dictionary
 

 

DROP TEXT SEARCH DICTIONARY [ IF EXISTS ] name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP TEXT SEARCH DICTIONARY drops an existing text
   search dictionary.  To execute this command you must be the owner of the
   dictionary.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the text search dictionary does not exist.
      A notice is issued in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of an existing text search
      dictionary.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the text search dictionary,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the text search dictionary if any objects depend on it.
      This is the default.
     

    
   
  
 

 
  
# Examples

  
   Remove the text search dictionary english:

```

DROP TEXT SEARCH DICTIONARY english;

```

   This command will not succeed if there are any existing text search
   configurations that use the dictionary.  Add CASCADE to
   drop such configurations along with the dictionary.
  

 

 
  
# Compatibility

  
   There is no DROP TEXT SEARCH DICTIONARY statement in the
   SQL standard.
  

 

 
  
# See Also
