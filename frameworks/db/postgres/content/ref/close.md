---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/close.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.581131Z"
---
CLOSE
 

 
  cursor
  CLOSE
 

 
  
# CLOSE

  7
  SQL - Language Statements
 

 
  
# CLOSE

  close a cursor
 

 

CLOSE { name | ALL }

 

 
  
# Description

  
   CLOSE frees the resources associated with an open cursor.
   After the cursor is closed, no subsequent operations
   are allowed on it. A cursor should be closed when it is
   no longer needed.
  

  
   Every non-holdable open cursor is implicitly closed when a
   transaction is terminated by COMMIT or
   ROLLBACK.  A holdable cursor is implicitly
   closed if the transaction that created it aborts via
   ROLLBACK.  If the creating transaction
   successfully commits, the holdable cursor remains open until an
   explicit CLOSE is executed, or the client
   disconnects.
  

 

 
  
# Parameters

  
   
    name
    
     
      The name of an open cursor to close.
     

    
   

   
    ALL
    
     
      Close all open cursors.
     

    
   

  
 

 
  
# Notes

  
   PostgreSQL does not have an explicit
   OPEN cursor statement; a cursor is considered
   open when it is declared.  Use the
   DECLARE
   statement to declare a cursor.
  

  
   You can see all available cursors by querying the pg_cursors system view.
  

  
   If a cursor is closed after a savepoint which is later rolled back,
   the CLOSE is not rolled back; that is, the cursor
   remains closed.
  

 

 
  
# Examples

  
   Close the cursor liahona:

```

CLOSE liahona;

```

 

 
  
# Compatibility

  
   CLOSE is fully conforming with the SQL
   standard. CLOSE ALL is a PostgreSQL
   extension.
  

 

 
  
# See Also
