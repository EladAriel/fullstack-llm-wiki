---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_collation.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.541941Z"
---
DROP COLLATION
 

 
  
# DROP COLLATION

  7
  SQL - Language Statements
 

 
  
# DROP COLLATION

  remove a collation
 

 

DROP COLLATION [ IF EXISTS ] name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP COLLATION removes a previously defined collation.
   To be able to drop a collation, you must own the collation.
  

 

 
  
# Parameters

   
    
     IF EXISTS
     
      
       Do not throw an error if the collation does not exist.
       A notice is issued in this case.
      

     
    

    
     name

     
      
       The name of the collation. The collation name can be
       schema-qualified.
      

     
    

    
     CASCADE
     
      
       Automatically drop objects that depend on the collation,
       and in turn all objects that depend on those objects
       (see ).
      

     
    

    
     RESTRICT
     
      
       Refuse to drop the collation if any objects depend on it.  This
       is the default.
      

     
    
   
 

 
  
# Examples

  
   To drop the collation named german:

```

DROP COLLATION german;

```

 

 
  
# Compatibility

  
   The DROP COLLATION command conforms to the
   SQL standard, apart from the IF
   EXISTS option, which is a PostgreSQL extension.
  

 

 
  
# See Also
