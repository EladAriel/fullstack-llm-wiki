---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_schema.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.545758Z"
---
DROP SCHEMA
 

 
  
# DROP SCHEMA

  7
  SQL - Language Statements
 

 
  
# DROP SCHEMA

  remove a schema
 

 

DROP SCHEMA [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP SCHEMA removes schemas from the database.
  

  
   A schema can only be dropped by its owner or a superuser.  Note that
   the owner can drop the schema (and thereby all contained objects)
   even if they do not own some of the objects within the schema.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the schema does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name of a schema.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects (tables, functions, etc.) that are
      contained in the schema,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the schema if it contains any objects.  This is
      the default.
     

    
   
  
 

 
  
# Notes

  
   Using the CASCADE option might make the command
   remove objects in other schemas besides the one(s) named.
  

 

 
  
# Examples

  
   To remove schema mystuff from the database,
   along with everything it contains:

```

DROP SCHEMA mystuff CASCADE;

```

 

 
  
# Compatibility

  
   DROP SCHEMA is fully conforming with the SQL
   standard, except that the standard only allows one schema to be
   dropped per command, and apart from the
   IF EXISTS option, which is a PostgreSQL
   extension.
  

 

 
  
# See Also
