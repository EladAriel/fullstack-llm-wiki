---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/func/func-logical.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.525335Z"
---
# Logical Operators

   
    operator
    logical
   

   
    Boolean
    operators
    operators, logical
   

   
    The usual logical operators are available:

    
     AND (operator)
    

    
     OR (operator)
    

    
     NOT (operator)
    

    
     conjunction
    

    
     disjunction
    

    
     negation
    

boolean AND boolean boolean
boolean OR boolean boolean
NOT boolean boolean

    SQL uses a three-valued logic system with true,
    false, and null, which represents unknown.
    Observe the following truth tables:

    
     
      
       
        a
        b
        a AND b
        a OR b
       
      

      
       
        TRUE
        TRUE
        TRUE
        TRUE
       

       
        TRUE
        FALSE
        FALSE
        TRUE
       

       
        TRUE
        NULL
        NULL
        TRUE
       

       
        FALSE
        FALSE
        FALSE
        FALSE
       

       
        FALSE
        NULL
        FALSE
        NULL
       

       
        NULL
        NULL
        NULL
        NULL
       
      
     
    

    
     
      
       
        a
        NOT a
       
      

      
       
        TRUE
        FALSE
       

       
        FALSE
        TRUE
       

       
        NULL
        NULL
       
      
     
    
   

   
    The operators AND and OR are
    commutative, that is, you can switch the left and right operands
    without affecting the result.  (However, it is not guaranteed that
    the left operand is evaluated before the right operand.  See  for more information about the
    order of evaluation of subexpressions.)
