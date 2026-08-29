---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_transform.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.615306Z"
---
DROP TRANSFORM
 

 
  
# DROP TRANSFORM

  7
  SQL - Language Statements
 

 
  
# DROP TRANSFORM

  remove a transform
 

 

DROP TRANSFORM [ IF EXISTS ] FOR type_name LANGUAGE lang_name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP TRANSFORM removes a previously defined transform.
  

  
   To be able to drop a transform, you must own the type and the language.
   These are the same privileges that are required to create a transform.
  

 

 
  
# Parameters

   

   
    IF EXISTS
    
     
      Do not throw an error if the transform does not exist. A notice is issued
      in this case.
     

    
   

    
     type_name

     
      
       The name of the data type of the transform.
      

     
    

    
     lang_name

     
      
       The name of the language of the transform.
      

     
    

    
     CASCADE
     
      
       Automatically drop objects that depend on the transform,
       and in turn all objects that depend on those objects
       (see ).
      

     
    

    
     RESTRICT
     
      
       Refuse to drop the transform if any objects depend on it.  This is the
       default.
      

     
    
   
 

 
  
# Examples

  
   To drop the transform for type hstore and language
   plpython3u:

```

DROP TRANSFORM FOR hstore LANGUAGE plpython3u;

```

 

 
  
# Compatibility

  
   This form of DROP TRANSFORM is a
   PostgreSQL extension.  See  for details.
  

 

 
  
# See Also
