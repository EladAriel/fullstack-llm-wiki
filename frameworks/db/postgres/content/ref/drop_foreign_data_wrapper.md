---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_foreign_data_wrapper.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.564636Z"
---
DROP FOREIGN DATA WRAPPER
 

 
  
# DROP FOREIGN DATA WRAPPER

  7
  SQL - Language Statements
 

 
  
# DROP FOREIGN DATA WRAPPER

  remove a foreign-data wrapper
 

 

DROP FOREIGN DATA WRAPPER [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP FOREIGN DATA WRAPPER removes an existing
   foreign-data wrapper.  To execute this command, the current user
   must be the owner of the foreign-data wrapper.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the foreign-data wrapper does not
      exist.  A notice is issued in this case.
     

    
   

   
    name
    
     
      The name of an existing foreign-data wrapper.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the foreign-data
      wrapper (such as foreign tables and servers),
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the foreign-data wrapper if any objects depend
      on it.  This is the default.
     

    
   
  
 

 
  
# Examples

  
   Drop the foreign-data wrapper dbi:

```

DROP FOREIGN DATA WRAPPER dbi;

```

 

 
  
# Compatibility

  
   DROP FOREIGN DATA WRAPPER conforms to ISO/IEC
   9075-9 (SQL/MED).  The IF EXISTS clause is
   a PostgreSQL extension.
  

 

 
  
# See Also
