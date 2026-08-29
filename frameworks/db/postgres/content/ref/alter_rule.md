---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_rule.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.564396Z"
---
ALTER RULE
 

 
  
# ALTER RULE

  7
  SQL - Language Statements
 

 
  
# ALTER RULE

  change the definition of a rule
 

 

ALTER RULE name ON table_name RENAME TO new_name

 

 
  
# Description

  
   ALTER RULE changes properties of an existing
   rule.  Currently, the only available action is to change the rule's name.
  

  
   To use ALTER RULE, you must own the table or view that
   the rule applies to.
  

 

 
  
# Parameters

  
   
    name
    
     
      The name of an existing rule to alter.
     

    
   

   
    table_name
    
     
      The name (optionally schema-qualified) of the table or view that the
      rule applies to.
     

    
   

   
    new_name
    
     
      The new name for the rule.
     

    
   
  
 

 
  
# Examples

  
   To rename an existing rule:

```

ALTER RULE notify_all ON emp RENAME TO notify_me;

```

 

 
  
# Compatibility

  
   ALTER RULE is a
   PostgreSQL language extension, as is the
   entire query rewrite system.
  

 

 
  
# See Also
