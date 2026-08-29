---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_view.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.591258Z"
---
DROP VIEW
 

 
  
# DROP VIEW

  7
  SQL - Language Statements
 

 
  
# DROP VIEW

  remove a view
 

 

DROP VIEW [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP VIEW drops an existing view.  To execute
   this command you must be the owner of the view.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the view does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of the view to remove.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the view (such as
      other views),
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the view if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  
   This command will remove the view called kinds:

```

DROP VIEW kinds;

```

 

 
  
# Compatibility

  
   This command conforms to the SQL standard, except that the standard only
   allows one view to be dropped per command, and apart from the
   IF EXISTS option, which is a PostgreSQL
   extension.
  

 

 
  
# See Also
