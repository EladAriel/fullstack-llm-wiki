---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/commit.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.620170Z"
---
COMMIT
 

 
  
# COMMIT

  7
  SQL - Language Statements
 

 
  
# COMMIT

  commit the current transaction
 

 

COMMIT [ WORK | TRANSACTION ] [ AND [ NO ] CHAIN ]

 

 
  
# Description

  
   COMMIT commits the current transaction. All
   changes made by the transaction become visible to others
   and are guaranteed to be durable if a crash occurs.
  

  
   If the transaction is in an aborted state then no changes will be made
   and the effect of the COMMIT will be identical to that
   of ROLLBACK, including the command tag output.
  

  
   In either case, if the AND CHAIN parameter is
   specified then a new, identically configured, transaction is started.
  

  
   For more information regarding transactions see
   .
  

 

 
  
# Parameters

  
   chained transactions
  

  
   
    WORK
    TRANSACTION
    
     
      Optional key words. They have no effect.
     

    
   

   
    AND CHAIN
    
     
      If AND CHAIN is specified, a new transaction is
      immediately started with the same transaction characteristics (see ) as the just finished one.  Otherwise,
      no new transaction is started.
     

    
   
  
 

 
  
# Outputs

  
   On successful completion of a non-aborted transaction,
   a COMMIT command returns a command tag of the form

```

COMMIT

```

  

  
   However, in an aborted transaction, a COMMIT
   command returns a command tag of the form

```

ROLLBACK

```

  

 

 
  
# Notes

  
   Use  to
   abort a transaction.
  

  
   Issuing COMMIT when not inside a transaction does
   no harm, but it will provoke a warning message.  COMMIT AND
   CHAIN when not inside a transaction is an error.
  

 

 
  
# Examples

  
   To commit the current transaction and make all changes permanent:

```

COMMIT;

```

 

 
  
# Compatibility

  
   The command COMMIT conforms to the SQL standard, except
   that no exception condition is raised in the case where the transaction
   was already aborted.
  

  
   The form COMMIT TRANSACTION is a PostgreSQL extension.
  

 

 
  
# See Also
