---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/discard.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.574236Z"
---
DISCARD
 

 
  
# DISCARD

  7
  SQL - Language Statements
 

 
  
# DISCARD

  discard session state
 

 

DISCARD { ALL | PLANS | SEQUENCES | TEMPORARY | TEMP }

 

 
  
# Description

  
   DISCARD releases internal resources associated with a
   database session.  This command is useful for partially or fully
   resetting the session's state.  There are several subcommands to
   release different types of resources; the DISCARD ALL
   variant subsumes all the others, and also resets additional state.
  

 

 
  
# Parameters

  

   
    PLANS
    
     
      Releases all cached query plans, forcing re-planning to occur
      the next time the associated prepared statement is used.
     

    
   

   
    SEQUENCES
    
     
      Discards all cached sequence-related state,
      including currval()/lastval()
      information and any preallocated sequence values that have not
      yet been returned by nextval().
      (See  for a description of
      preallocated sequence values.)
     

    
   

   
    TEMPORARY or TEMP
    
     
      Drops all temporary tables created in the current session.
     

    
   

   
    ALL
    
     
      Releases all temporary resources associated with the current
      session and resets the session to its initial state.
      Currently, this has the same effect as executing the following sequence
      of statements:

```

CLOSE ALL;
SET SESSION AUTHORIZATION DEFAULT;
RESET ALL;
DEALLOCATE ALL;
UNLISTEN *;
SELECT pg_advisory_unlock_all();
DISCARD PLANS;
DISCARD TEMP;
DISCARD SEQUENCES;

```

    
   

  
 

 
  
# Notes

   
    DISCARD ALL cannot be executed inside a transaction block.
   

 

 
  
# Compatibility

  
   DISCARD is a PostgreSQL extension.
