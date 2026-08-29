---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_cast.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.595509Z"
---
DROP CAST
 

 
  
# DROP CAST

  7
  SQL - Language Statements
 

 
  
# DROP CAST

  remove a cast
 

 

DROP CAST [ IF EXISTS ] (source_type AS target_type) [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP CAST removes a previously defined cast.
  

  
   To be able to drop a cast, you must own the source or the target
   data type.  These are the same privileges that are required to
   create a cast.
  

 

 
  
# Parameters

   

   
    IF EXISTS
    
     
      Do not throw an error if the cast does not exist. A notice is issued
      in this case.
     

    
   

    
     source_type

     
      
       The name of the source data type of the cast.
      

     
    

    
     target_type

     
      
       The name of the target data type of the cast.
      

     
    

    
     CASCADE
     RESTRICT

     
      
       These key words do not have any effect, since there are no
       dependencies on casts.
      

     
    
   
 

 
  
# Examples

  
   To drop the cast from type text to type int:

```

DROP CAST (text AS int);

```

 

 
  
# Compatibility

  
   The DROP CAST command conforms to the SQL standard.
  

 

 
  
# See Also
