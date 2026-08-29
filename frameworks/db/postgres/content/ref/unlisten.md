---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/unlisten.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.547857Z"
---
UNLISTEN
 

 
  
# UNLISTEN

  7
  SQL - Language Statements
 

 
  
# UNLISTEN

  stop listening for a notification
 

 

UNLISTEN { channel | * }

 

 
  
# Description

  
   UNLISTEN is used to remove an existing
   registration for NOTIFY events.
   UNLISTEN cancels any existing registration of
   the current PostgreSQL session as a
   listener on the notification channel named channel.  The special wildcard
   * cancels all listener registrations for the
   current session.
  

  
   
   contains a more extensive
   discussion of the use of LISTEN and
   NOTIFY.
  

 

 
  
# Parameters

  
   
    channel
    
     
      Name of a notification channel (any identifier).
     

    
   

   
    *
    
     
      All current listen registrations for this session are cleared.
     

    
   
  
 

 
  
# Notes

  
   You can unlisten something you were not listening for; no warning or error
   will appear.
  

  
   At the end of each session, UNLISTEN * is
   automatically executed.
  

  
   A transaction that has executed UNLISTEN cannot be
   prepared for two-phase commit.
  

 

 
  
# Examples

  
   To make a registration:

```

LISTEN virtual;
NOTIFY virtual;
Asynchronous notification "virtual" received from server process with PID 8448.

```

  

  
   Once UNLISTEN has been executed, further NOTIFY
   messages will be ignored:

```

UNLISTEN virtual;
NOTIFY virtual;
-- no NOTIFY event is received

```

 

 
  
# Compatibility

  
   There is no UNLISTEN command in the SQL standard.
  

 

 
  
# See Also
