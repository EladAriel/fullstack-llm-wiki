---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_materialized_view.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.570379Z"
---
DROP MATERIALIZED VIEW
 

 
  
# DROP MATERIALIZED VIEW

  7
  SQL - Language Statements
 

 
  
# DROP MATERIALIZED VIEW

  remove a materialized view
 

 

DROP MATERIALIZED VIEW [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP MATERIALIZED VIEW drops an existing materialized
   view. To execute this command you must be the owner of the materialized
   view.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the materialized view does not exist. A notice
      is issued in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of the materialized view to
      remove.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the materialized view (such as
      other materialized views, or regular views),
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the materialized view if any objects depend on it.  This
      is the default.
     

    
   
  
 

 
  
# Examples

  
   This command will remove the materialized view called
   order_summary:

```

DROP MATERIALIZED VIEW order_summary;

```

 

 
  
# Compatibility

  
   DROP MATERIALIZED VIEW is a
   PostgreSQL extension.
  

 

 
  
# See Also
