---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_index.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.541019Z"
---
DROP INDEX
 

 
  
# DROP INDEX

  7
  SQL - Language Statements
 

 
  
# DROP INDEX

  remove an index
 

 

DROP INDEX [ CONCURRENTLY ] [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP INDEX drops an existing index from the database
   system. To execute this command you must be the owner of
   the index.
  

 

 
  
# Parameters

  
   
    CONCURRENTLY
    
     
      Drop the index without locking out concurrent selects, inserts, updates,
      and deletes on the index's table.  A normal DROP INDEX
      acquires an ACCESS EXCLUSIVE lock on the table,
      blocking other accesses until the index drop can be completed.  With
      this option, the command instead waits until conflicting transactions
      have completed.
     

     
      There are several caveats to be aware of when using this option.
      Only one index name can be specified, and the CASCADE option
      is not supported.  (Thus, an index that supports a UNIQUE or
      PRIMARY KEY constraint cannot be dropped this way.)
      Also, regular DROP INDEX commands can be
      performed within a transaction block, but
      DROP INDEX CONCURRENTLY cannot.
      Lastly, indexes on partitioned tables cannot be dropped using this
      option.
     

     
      For temporary tables, DROP INDEX is always
      non-concurrent, as no other session can access them, and
      non-concurrent index drop is cheaper.
     

    
   

   
    IF EXISTS
    
     
      Do not throw an error if the index does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of an index to remove.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the index,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the index if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  
   This command will remove the index title_idx:

```

DROP INDEX title_idx;

```

 

 
  
# Compatibility

  
   DROP INDEX is a
   PostgreSQL language extension.  There
   are no provisions for indexes in the SQL standard.
  

 

 
  
# See Also
