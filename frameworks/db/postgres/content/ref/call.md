---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/call.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.571369Z"
---
CALL
 

 
  
# CALL

  7
  SQL - Language Statements
 

 
  
# CALL

  invoke a procedure
 

 

CALL name ( [ argument ] [, ...] )

 

 
  
# Description

  
   CALL executes a procedure.
  

  
   If the procedure has any output parameters, then a result row will be
   returned, containing the values of those parameters.
  

 

 
  
# Parameters

  
   
    name
    
     
      The name (optionally schema-qualified) of the procedure.
     

    
   

  
    argument
    
     
      An argument expression for the procedure call.
     

     
      Arguments can include parameter names, using the syntax
      name => value.
      This works the same as in ordinary function calls; see
       for details.
     

     
      Arguments must be supplied for all procedure parameters that lack
      defaults, including OUT parameters.  However,
      arguments matching OUT parameters are not evaluated,
      so it's customary to just write NULL for them.
      (Writing something else for an OUT parameter
      might cause compatibility problems with
      future PostgreSQL versions.)
     

    
   
  
 

 
  
# Notes

  
   The user must have EXECUTE privilege on the procedure in
   order to be allowed to invoke it.
  

  
   To call a function (not a procedure), use SELECT instead.
  

  
   If CALL is executed in a transaction block, then the
   called procedure cannot execute transaction control statements.
   Transaction control statements are only allowed if CALL
   is executed in its own transaction.
  

  
   PL/pgSQL handles output parameters
   in CALL commands differently;
   see .
  

 

 
  
# Examples

```

CALL do_db_maintenance();

```

 

 
  
# Compatibility

  
   CALL conforms to the SQL standard,
   except for the handling of output parameters.  The standard
   says that users should write variables to receive the values
   of output parameters.
  

 

 
  
# See Also
