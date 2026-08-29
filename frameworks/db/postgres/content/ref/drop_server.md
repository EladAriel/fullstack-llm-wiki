---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_server.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.589334Z"
---
DROP SERVER
 

 
  
# DROP SERVER

  7
  SQL - Language Statements
 

 
  
# DROP SERVER

  remove a foreign server descriptor
 

 

DROP SERVER [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP SERVER removes an existing foreign server
   descriptor.  To execute this command, the current user must be the
   owner of the server.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the server does not exist.  A notice is
      issued in this case.
     

    
   

   
    name
    
     
      The name of an existing server.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the server (such as
      user mappings),
      and in turn all objects that depend on those objects
      (see ).
      However, a subscription that uses the server is never dropped
      automatically; it must be dropped with
      DROP SUBSCRIPTION
      before the server can be dropped.
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the server if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  
   Drop a server foo if it exists:

```

DROP SERVER IF EXISTS foo;

```

 

 
  
# Compatibility

  
   DROP SERVER conforms to ISO/IEC 9075-9
   (SQL/MED).  The IF EXISTS clause is
   a PostgreSQL extension.
  

 

 
  
# See Also
