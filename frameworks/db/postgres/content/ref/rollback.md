---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/rollback.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.596452Z"
---
ROLLBACK
 

 
  
# ROLLBACK

  7
  SQL - Language Statements
 

 
  
# ROLLBACK

  abort the current transaction
 

 

ROLLBACK [ WORK | TRANSACTION ] [ AND [ NO ] CHAIN ]

 

 
  
# Description

  
   ROLLBACK rolls back the current transaction and causes
   all the updates made by the transaction to be discarded.
  

 

 
  
# Parameters

  
   chained transactions
  

  
   
    WORK
    TRANSACTION
    
     
      Optional key words. They have no effect.
     

    
   

   
    AND CHAIN
    
     
      If AND CHAIN is specified, a new (not aborted)
      transaction is immediately started with the same transaction
      characteristics (see ) as the
      just finished one.  Otherwise, no new transaction is started.
     

    
   
  
 

 
  
# Notes

  
   Use COMMIT to
   successfully terminate a transaction.
  

  
   Issuing ROLLBACK outside of a transaction
   block emits a warning and otherwise has no effect.  ROLLBACK AND
   CHAIN outside of a transaction block is an error.
  

 

 
  
# Examples

  
   To abort all changes:

```

ROLLBACK;

```

 

 
  
# Compatibility

  
   The command ROLLBACK conforms to the SQL standard.  The
   form ROLLBACK TRANSACTION is a PostgreSQL extension.
  

 

 
  
# See Also
