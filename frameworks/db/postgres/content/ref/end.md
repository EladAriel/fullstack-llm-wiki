---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/end.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.621358Z"
---
END
 

 
  
# END

  7
  SQL - Language Statements
 

 
  
# END

  commit the current transaction
 

 

END [ WORK | TRANSACTION ] [ AND [ NO ] CHAIN ]

 

 
  
# Description

  
   END commits the current transaction. All changes
   made by the transaction become visible to others and are guaranteed
   to be durable if a crash occurs.  This command is a
   PostgreSQL extension
   that is equivalent to COMMIT.
  

 

 
  
# Parameters

  
   
    WORK
    TRANSACTION
    
     
      Optional key words. They have no effect.
     

    
   

   
    AND CHAIN
    
     
      If AND CHAIN is specified, a new transaction is
      immediately started with the same transaction characteristics (see ) as the just finished one.  Otherwise,
      no new transaction is started.
     

    
   
  
 

 
  
# Notes

  
   Use ROLLBACK to
   abort a transaction.
  

  
   Issuing END when not inside a transaction does
   no harm, but it will provoke a warning message.
  

 

 
  
# Examples

  
   To commit the current transaction and make all changes permanent:

```

END;

```

 

 
  
# Compatibility

  
   END is a PostgreSQL
   extension that provides functionality equivalent to COMMIT, which is
   specified in the SQL standard.
  

 

 
  
# See Also
