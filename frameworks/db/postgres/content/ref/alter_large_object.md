---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_large_object.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.554837Z"
---
ALTER LARGE OBJECT
 

 
  
# ALTER LARGE OBJECT

  7
  SQL - Language Statements
 

 
  
# ALTER LARGE OBJECT

  change the definition of a large object
 

 

ALTER LARGE OBJECT large_object_oid OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }

 

 
  
# Description

  
   ALTER LARGE OBJECT changes the definition of a
   large object.
  

  
   You must own the large object to use ALTER LARGE OBJECT.
   To alter the owner, you must also be able to SET ROLE to
   the new owning role.
   (However, a superuser can alter any large object anyway.)
   Currently, the only functionality is to assign a new owner, so both
   restrictions always apply.
  

 

 
  
# Parameters

  
   
    large_object_oid
    
     
      OID of the large object to be altered
     

    
   

   
    new_owner
    
     
      The new owner of the large object
     

    
   
  
 

 
  
# Compatibility

  
   There is no ALTER LARGE OBJECT statement in the SQL
   standard.
  

 

 
  
# See Also
