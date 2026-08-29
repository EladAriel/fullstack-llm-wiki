---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_publication.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.541675Z"
---
DROP PUBLICATION
 

 
  
# DROP PUBLICATION

  7
  SQL - Language Statements
 

 
  
# DROP PUBLICATION

  remove a publication
 

 

DROP PUBLICATION [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP PUBLICATION removes an existing publication from
   the database.
  

  
   A publication can only be dropped by its owner or a superuser.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the publication does not exist. A notice is
      issued in this case.
     

    
   

   
    name
    
     
      The name of an existing publication.
     

    
   

   
    CASCADE
    RESTRICT

    
     
      These key words do not have any effect, since there are no dependencies
      on publications.
     

    
   
  
 

 
  
# Examples

  
   Drop a publication:

```

DROP PUBLICATION mypublication;

```

 

 
  
# Compatibility

  
   DROP PUBLICATION is a PostgreSQL
   extension.
  

 

 
  
# See Also
