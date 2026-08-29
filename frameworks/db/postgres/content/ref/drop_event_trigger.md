---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_event_trigger.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.549322Z"
---
DROP EVENT TRIGGER
 

 
  
# DROP EVENT TRIGGER

  7
  SQL - Language Statements
 

 
  
# DROP EVENT TRIGGER

  remove an event trigger
 

 

DROP EVENT TRIGGER [ IF EXISTS ] name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP EVENT TRIGGER removes an existing event trigger.
   To execute this command, the current user must be the owner of the event
   trigger.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the event trigger does not exist. A notice
      is issued in this case.
     

    
   

   
    name
    
     
      The name of the event trigger to remove.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the trigger,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the trigger if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  
   Destroy the trigger snitch:

```

DROP EVENT TRIGGER snitch;

```

 

 
  
# Compatibility

  
   There is no DROP EVENT TRIGGER statement in the
   SQL standard.
  

 

 
  
# See Also
