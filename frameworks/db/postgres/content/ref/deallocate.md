---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/deallocate.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.541245Z"
---
DEALLOCATE
 

 
  prepared statements
  removing
 

 
  
# DEALLOCATE

  7
  SQL - Language Statements
 

 
  
# DEALLOCATE

  deallocate a prepared statement
 

 

DEALLOCATE [ PREPARE ] { name | ALL }

 

 
  
# Description

  
   DEALLOCATE is used to deallocate a previously
   prepared SQL statement. If you do not explicitly deallocate a
   prepared statement, it is deallocated when the session ends.
  

  
   For more information on prepared statements, see .
  

 

 
  
# Parameters

  
   
    PREPARE
    
     
      This key word is ignored.
     

    
   

   
    name
    
     
      The name of the prepared statement to deallocate.
     

    
   

   
    ALL
    
     
      Deallocate all prepared statements.
     

    
   
  
 

 
  
# Compatibility

  
   The SQL standard includes a DEALLOCATE
   statement, but it is only for use in embedded SQL.
  

 

 
  
# See Also
