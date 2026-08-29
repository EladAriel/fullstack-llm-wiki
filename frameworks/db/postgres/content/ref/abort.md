---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/abort.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.614134Z"
---
ABORT
 

 
  
# ABORT

  7
  SQL - Language Statements
 

 
  
# ABORT

  abort the current transaction
 

 

ABORT [ WORK | TRANSACTION ] [ AND [ NO ] CHAIN ]

 

 
  
# Description

  
   ABORT rolls back the current transaction and causes
   all the updates made by the transaction to be discarded.
   This command is identical
   in behavior to the standard SQL command
   ROLLBACK,
   and is present only for historical reasons.
  

 

 
  
# Parameters

  
   
    WORK
    TRANSACTION
    
     
      Optional key words. They have no effect.
     

    
   

   
    AND CHAIN
    
     
      If AND CHAIN is specified, a new transaction is
      immediately started with the same transaction characteristics (see SET TRANSACTION) as the just finished one.  Otherwise,
      no new transaction is started.
     

    
   
  
 

 
  
# Notes

  
   Use COMMIT to
   successfully terminate a transaction.
  

  
   Issuing ABORT outside of a transaction block
   emits a warning and otherwise has no effect.
  

 

 
  
# Examples

  
   To abort all changes:

```

ABORT;

```

 

 
  
# Compatibility

  
   This command is a PostgreSQL extension
   present for historical reasons. ROLLBACK is the
   equivalent standard SQL command.
  

 

 
  
# See Also
