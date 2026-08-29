---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_language.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.536265Z"
---
DROP LANGUAGE
 

 
  
# DROP LANGUAGE

  7
  SQL - Language Statements
 

 
  
# DROP LANGUAGE

  remove a procedural language
 

 

DROP [ PROCEDURAL ] LANGUAGE [ IF EXISTS ] name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP LANGUAGE removes the definition of a
   previously registered procedural language.  You must be a superuser
   or the owner of the language to use DROP LANGUAGE.
  

  
   
    As of PostgreSQL 9.1, most procedural
    languages have been made into extensions, and should
    therefore be removed with DROP EXTENSION
    not DROP LANGUAGE.
   

  
 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the language does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name of an existing procedural language.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the language (such as
      functions in the language),
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the language if any objects depend on it.  This
      is the default.
     

    
   
  
 

 
  
# Examples

  
   This command removes the procedural language
   plsample:

```

DROP LANGUAGE plsample;

```

 

 
  
# Compatibility

  
   There is no DROP LANGUAGE statement in the SQL
   standard.
  

 

 
  
# See Also
