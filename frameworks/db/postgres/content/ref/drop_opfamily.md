---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_opfamily.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.585821Z"
---
DROP OPERATOR FAMILY
 

 
  
# DROP OPERATOR FAMILY

  7
  SQL - Language Statements
 

 
  
# DROP OPERATOR FAMILY

  remove an operator family
 

 

DROP OPERATOR FAMILY [ IF EXISTS ] name USING index_method [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP OPERATOR FAMILY drops an existing operator family.
   To execute this command you must be the owner of the operator family.
  

  
   DROP OPERATOR FAMILY includes dropping any operator
   classes contained in the family, but it does not drop any of the operators
   or functions referenced by the family.  If there are any indexes depending
   on operator classes within the family, you will need to specify
   CASCADE for the drop to complete.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the operator family does not exist.
      A notice is issued in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of an existing operator family.
     

    
   

   
    index_method
    
     
      The name of the index access method the operator family is for.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the operator family,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the operator family if any objects depend on it.
      This is the default.
     

    
   
  
 

 
  
# Examples

  
   Remove the B-tree operator family float_ops:

```

DROP OPERATOR FAMILY float_ops USING btree;

```

   This command will not succeed if there are any existing indexes
   that use operator classes within the family.  Add CASCADE to
   drop such indexes along with the operator family.
  

 

 
  
# Compatibility

  
   There is no DROP OPERATOR FAMILY statement in the
   SQL standard.
  

 

 
  
# See Also
