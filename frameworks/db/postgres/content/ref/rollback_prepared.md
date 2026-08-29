---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/rollback_prepared.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.596210Z"
---
ROLLBACK PREPARED
 

 
  
# ROLLBACK PREPARED

  7
  SQL - Language Statements
 

 
  
# ROLLBACK PREPARED

  cancel a transaction that was earlier prepared for two-phase commit
 

 

ROLLBACK PREPARED transaction_id

 

 
  
# Description

  
   ROLLBACK PREPARED rolls back a transaction that is in
   prepared state.
  

 

 
  
# Parameters

  
   
    transaction_id
    
     
      The transaction identifier of the transaction that is to be
      rolled back.
     

    
   
  
 

 
  
# Notes

  
   To roll back a prepared transaction, you must be either the same user that
   executed the transaction originally, or a superuser.  But you do not
   have to be in the same session that executed the transaction.
  

  
   This command cannot be executed inside a transaction block. The prepared
   transaction is rolled back immediately.
  

  
   All currently available prepared transactions are listed in the
   pg_prepared_xacts
   system view.
  

 

 
  
# Examples

  
   Roll back the transaction identified by the transaction
   identifier foobar:

```

ROLLBACK PREPARED 'foobar';

```

 

 
  
# Compatibility

  
   ROLLBACK PREPARED is a
   PostgreSQL extension.  It is intended for use by
   external transaction management systems, some of which are covered by
   standards (such as X/Open XA), but the SQL side of those systems is not
   standardized.
  

 

 
  
# See Also
