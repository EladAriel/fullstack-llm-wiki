---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_property_graph.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.601778Z"
---
DROP PROPERTY GRAPH
 

 
  
# DROP PROPERTY GRAPH

  7
  SQL - Language Statements
 

 
  
# DROP PROPERTY GRAPH

  remove an SQL-property graph
 

 

DROP PROPERTY GRAPH [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP PROPERTY GRAPH drops an existing property graph.
   To execute this command you must be the owner of the property graph.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the property graph does not exist.  A notice is
      issued in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of the property graph to remove.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the property graph, and in
      turn all objects that depend on those objects (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the property graph if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  

```

DROP PROPERTY GRAPH g1;

```

 

 
  
# Compatibility

  
   DROP PROPERTY GRAPH conforms to ISO/IEC 9075-16
   (SQL/PGQ), except that the standard only allows one property graph to be
   dropped per command, and apart from the IF EXISTS
   option, which is a PostgreSQL extension.
  

 

 
  
# See Also
