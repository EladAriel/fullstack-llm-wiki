---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_type.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.546860Z"
---
DROP TYPE
 

 
  
# DROP TYPE

  7
  SQL - Language Statements
 

 
  
# DROP TYPE

  remove a data type
 

 

DROP TYPE [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP TYPE removes a user-defined data type.
   Only the owner of a type can remove it.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the type does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of the data type to remove.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the type (such as
      table columns, functions, and operators),
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the type if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  
   To remove the data type box:

```

DROP TYPE box;

```

 

 
  
# Compatibility

  
   This command is similar to the corresponding command in the SQL
   standard, apart from the IF EXISTS
   option, which is a PostgreSQL extension.
   But note that much of the CREATE TYPE command
   and the data type extension mechanisms in
   PostgreSQL differ from the SQL standard.
  

 

 
  
# See Also
