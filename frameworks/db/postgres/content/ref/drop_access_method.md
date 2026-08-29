---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_access_method.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.555079Z"
---
DROP ACCESS METHOD
 

 
  
# DROP ACCESS METHOD

  7
  SQL - Language Statements
 

 
  
# DROP ACCESS METHOD

  remove an access method
 

 

DROP ACCESS METHOD [ IF EXISTS ] name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP ACCESS METHOD removes an existing access method.
   Only superusers can drop access methods.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the access method does not exist.
      A notice is issued in this case.
     

    
   

   
    name
    
     
      The name of an existing access method.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the access method
      (such as operator classes, operator families, and indexes),
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the access method if any objects depend on it.
      This is the default.
     

    
   
  
 

 
  
# Examples

  
   Drop the access method heptree:

```

DROP ACCESS METHOD heptree;

```

 

 
  
# Compatibility

  
   DROP ACCESS METHOD is a
   PostgreSQL extension.
  

 

 
  
# See Also
