---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_subscription.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.552376Z"
---
DROP SUBSCRIPTION
 

 
  
# DROP SUBSCRIPTION

  7
  SQL - Language Statements
 

 
  
# DROP SUBSCRIPTION

  remove a subscription
 

 

DROP SUBSCRIPTION [ IF EXISTS ] name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP SUBSCRIPTION removes a subscription from the
   database cluster.
  

  
   To execute this command the user must be the owner of the subscription.
  

  
   DROP SUBSCRIPTION cannot be executed inside a
   transaction block if the subscription is associated with a replication
   slot.  (You can use ALTER SUBSCRIPTION to unset the
   slot.)
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the subscription does not exist. A notice is
      issued in this case.
     

    
   

   
    name
    
     
      The name of a subscription to be dropped.
     

    
   

   
    CASCADE
    RESTRICT

    
     
      These key words do not have any effect, since there are no dependencies
      on subscriptions.
     

    
   

  
 

 
  
# Notes

  
   When dropping a subscription that is associated with a replication slot on
   the remote host (the normal state), DROP SUBSCRIPTION
   will connect to the remote host and try to drop the replication slot (and
   any remaining table synchronization slots) as
   part of its operation.  This is necessary so that the resources allocated
   for the subscription on the remote host are released.  If this fails,
   either because the remote host is not reachable or because the remote
   replication slot cannot be dropped or does not exist or never existed,
   the DROP SUBSCRIPTION command will fail.  To proceed
   in this situation, first disable the subscription by executing
   
   ALTER SUBSCRIPTION ... DISABLE, and then disassociate
   it from the replication slot by executing
   
   ALTER SUBSCRIPTION ... SET (slot_name = NONE).
   After that, DROP SUBSCRIPTION will not attempt to drop
   the subscription's own replication slot.  It may still connect to the publisher
   to drop internally-created table synchronization slots if some table
   synchronization is left unfinished; if the publisher is unreachable, those
   slots (and the main slot, if it still exists) must be dropped manually.  Otherwise
   it/they will continue to reserve WAL and might eventually cause the disk to
   fill up.  See also
   .
  

  
   If a subscription is associated with a replication slot, then DROP
   SUBSCRIPTION cannot be executed inside a transaction block.
  

  
   If a conflict log table exists for the subscription (that is, when
   
   conflict_log_destination is set to table
   or all), DROP SUBSCRIPTION automatically drops
   the associated conflict log table.
  

 

 
  
# Examples

  
   Drop a subscription:

```

DROP SUBSCRIPTION mysub;

```

 

 
  
# Compatibility

  
   DROP SUBSCRIPTION is a PostgreSQL
   extension.
  

 

 
  
# See Also
