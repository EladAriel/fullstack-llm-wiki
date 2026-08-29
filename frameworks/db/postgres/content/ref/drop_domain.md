---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_domain.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.541462Z"
---
DROP DOMAIN
 

 
  
# DROP DOMAIN

  7
  SQL - Language Statements
 

 
  
# DROP DOMAIN

  remove a domain
 

 

DROP DOMAIN [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP DOMAIN removes a domain.  Only the owner of
   a domain can remove it.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the domain does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of an existing domain.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the domain (such as
      table columns),
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the domain if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  
   To remove the domain box:

```

DROP DOMAIN box;

```

 

 
  
# Compatibility

  
   This command conforms to the SQL standard, except for the
   IF EXISTS option, which is a PostgreSQL
   extension.
  

 

 
  
# See Also
