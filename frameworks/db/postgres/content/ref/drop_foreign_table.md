---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_foreign_table.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.573997Z"
---
DROP FOREIGN TABLE
 

 
  
# DROP FOREIGN TABLE

  7
  SQL - Language Statements
 

 
  
# DROP FOREIGN TABLE

  remove a foreign table
 

 

DROP FOREIGN TABLE [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP FOREIGN TABLE removes a foreign table.
   Only the owner of a foreign table can remove it.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the foreign table does not exist.
      A notice is issued in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of the foreign table to drop.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the foreign table (such as
      views), and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the foreign table if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  
   To destroy two foreign tables, films and
   distributors:

```

DROP FOREIGN TABLE films, distributors;

```

 

 
  
# Compatibility

  
   This command conforms to ISO/IEC 9075-9 (SQL/MED), except that the
   standard only allows one foreign table to be dropped per command, and apart
   from the IF EXISTS option, which is a PostgreSQL
   extension.
  

 

 
  
# See Also
