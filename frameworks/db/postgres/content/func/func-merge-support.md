---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/func/func-merge-support.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.523747Z"
---
# Merge Support Functions

  
   MERGE
   RETURNING
  

  
   PostgreSQL includes one merge support function
   that may be used in the RETURNING list of a
    command to identify the action taken for each
   row; see .
  

  
   Merge Support Functions

   
    
     
      
       Function
      
      
       Description
      
     
    

    
     
      
       
        merge_action
       
       merge_action ( )
       text
      
      
       Returns the merge action command executed for the current row.  This
       will be 'INSERT', 'UPDATE', or
       'DELETE'.
      
     
    
   
  

  
   Example:
 0 THEN
    UPDATE SET in_stock = true, quantity = s.quantity
  WHEN MATCHED THEN
    UPDATE SET in_stock = false, quantity = 0
  WHEN NOT MATCHED THEN
    INSERT (product_id, in_stock, quantity)
      VALUES (s.product_id, true, s.quantity)
  RETURNING merge_action(), p.*;

 merge_action | product_id | in_stock | quantity
--------------+------------+----------+----------
 UPDATE       |       1001 | t        |       50
 UPDATE       |       1002 | f        |        0
 INSERT       |       1003 | t        |       10
]]>
  

  
   Note that this function can only be used in the RETURNING
   list of a MERGE command.  It is an error to use it in any
   other part of a query.
