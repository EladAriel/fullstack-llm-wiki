---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/func/func-tid.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.522506Z"
---
# TID Functions

  
   TID
   functions
  

  
   tid_block
  

  
   tid_offset
  

  
    lists functions for
   the tid data type (tuple identifier).
  

  
   TID Functions
   
    
     
      
       Function
      
      
       Description
      
      
       Example(s)
      
     
    

    
     
      
       tid_block ( tid )
       bigint
      
      
       Extracts the block number from a tuple identifier.
      
      
       tid_block('(42,7)'::tid)
       42
      
     

     
      
       tid_offset ( tid )
       integer
      
      
       Extracts the tuple offset within the block from a tuple identifier.
      
      
       tid_offset('(42,7)'::tid)
       7
