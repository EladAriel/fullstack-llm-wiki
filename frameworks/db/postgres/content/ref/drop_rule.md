---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_rule.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.590994Z"
---
DROP RULE
 

 
  
# DROP RULE

  7
  SQL - Language Statements
 

 
  
# DROP RULE

  remove a rewrite rule
 

 

DROP RULE [ IF EXISTS ] name ON table_name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP RULE drops a rewrite rule.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the rule does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name of the rule to drop.
     

    
   

   
    table_name
    
     
      The name (optionally schema-qualified) of the table or view that
      the rule applies to.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the rule,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the rule if any objects depend on it.  This is
      the default.
     

    
   
  
 

 
  
# Examples

  
   To drop the rewrite rule newrule:

```

DROP RULE newrule ON mytable;

```

 

 
  
# Compatibility

  
   DROP RULE is a
   PostgreSQL language extension, as is the
   entire query rewrite system.
  

 

 
  
# See Also
