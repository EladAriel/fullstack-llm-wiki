---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_extension.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.576286Z"
---
DROP EXTENSION
 

 
  
# DROP EXTENSION

  7
  SQL - Language Statements
 

 
  
# DROP EXTENSION

  remove an extension
 

 

DROP EXTENSION [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP EXTENSION removes extensions from the database.
   Dropping an extension causes its member objects, and other explicitly
   dependent routines (see ,
   the DEPENDS ON EXTENSION extension_name
    action), to be dropped as well.
  

  
   You must own the extension to use DROP EXTENSION.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the extension does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name of an installed extension.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the extension,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      This option prevents the specified extensions from being dropped if
      other objects, besides these extensions, their members, and their
      explicitly dependent routines, depend on them. This is the default.
     

    
   
  
 

 
  
# Examples

  
   To remove the extension hstore from the current
   database:

```

DROP EXTENSION hstore;

```

   This command will fail if any of hstore's objects
   are in use in the database, for example if any tables have columns
   of the hstore type.  Add the CASCADE option to
   forcibly remove those dependent objects as well.
  

 

 
  
# Compatibility

  
   DROP EXTENSION is a PostgreSQL
   extension.
  

 

 
  
# See Also
