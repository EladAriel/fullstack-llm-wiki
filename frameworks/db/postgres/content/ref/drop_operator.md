---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_operator.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.613234Z"
---
DROP OPERATOR
 

 
  
# DROP OPERATOR

  7
  SQL - Language Statements
 

 
  
# DROP OPERATOR

  remove an operator
 

 

DROP OPERATOR [ IF EXISTS ] name ( { left_type | NONE } , right_type ) [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP OPERATOR drops an existing operator from
   the database system.  To execute this command you must be the owner
   of the operator.
  

 

 
  
# Parameters

  

   
    IF EXISTS
    
     
      Do not throw an error if the operator does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of an existing operator.
     

    
   

   
    left_type
    
     
      The data type of the operator's left operand; write
      NONE if the operator has no left operand.
     

    
   

   
    right_type
    
     
      The data type of the operator's right operand.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the operator (such as views
      using it), and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the operator if any objects depend on it.  This
      is the default.
     

    
   
  
 

 
  
# Examples

  
   Remove the power operator a^b for type integer:

```

DROP OPERATOR ^ (integer, integer);

```

  

  
   Remove the bitwise-complement prefix operator
   ~b for type bit:

```

DROP OPERATOR ~ (none, bit);

```

  

  
   Remove multiple operators in one command:

```

DROP OPERATOR ~ (none, bit), ^ (integer, integer);

```

 

 
  
# Compatibility

  
   There is no DROP OPERATOR statement in the SQL standard.
  

 

 
  
# See Also
