---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_policy.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.592595Z"
---
DROP POLICY
 

 
  
# DROP POLICY

  7
  SQL - Language Statements
 

 
  
# DROP POLICY

  remove a row-level security policy from a table
 

 

DROP POLICY [ IF EXISTS ] name ON table_name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP POLICY removes the specified policy from the table.
   Note that if the last policy is removed for a table and the table still has
   row-level security enabled via ALTER TABLE, then the
   default-deny policy will be used.  ALTER TABLE ... DISABLE ROW
   LEVEL SECURITY can be used to disable row-level security for a
   table, whether policies for the table exist or not.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the policy does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name of the policy to drop.
     

    
   

   
    table_name
    
     
      The name (optionally schema-qualified) of the table that
      the policy is on.
     

    
   

   
    CASCADE
    RESTRICT

    
     
      These key words do not have any effect, since there are no
      dependencies on policies.
     

    
   

  
 

 
  
# Examples

  
   To drop the policy called p1 on the table named
   my_table:

```

DROP POLICY p1 ON my_table;

```

 

 
  
# Compatibility

  
   DROP POLICY is a PostgreSQL extension.
  

 

 
  
# See Also
