---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/execute.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.533690Z"
---
EXECUTE
 

 
  prepared statements
  executing
 

 
  
# EXECUTE

  7
  SQL - Language Statements
 

 
  
# EXECUTE

  execute a prepared statement
 

 

EXECUTE name [ ( parameter [, ...] ) ]

 

 
  
# Description

  
   EXECUTE is used to execute a previously prepared
   statement. Since prepared statements only exist for the duration of a
   session, the prepared statement must have been created by a
   PREPARE statement executed earlier in the
   current session.
  

  
   If the PREPARE statement that created the statement
   specified some parameters, a compatible set of parameters must be
   passed to the EXECUTE statement, or else an
   error is raised. Note that (unlike functions) prepared statements are
   not overloaded based on the type or number of their parameters; the
   name of a prepared statement must be unique within a database session.
  

  
   For more information on the creation and usage of prepared statements,
   see .
  

 

 
  
# Parameters

  
   
    name
    
     
      The name of the prepared statement to execute.
     

    
   

   
    parameter
    
     
      The actual value of a parameter to the prepared statement.  This
      must be an expression yielding a value that is compatible with
      the data type of this parameter, as was determined when the
      prepared statement was created.
     

    
   
  
 

 
  
# Outputs

   
   The command tag returned by EXECUTE
   is that of the prepared statement, and not EXECUTE.
  

 

 
  
# Examples

  
    Examples are given in 
    in the  documentation.
   

 

 
  
# Compatibility

  
   The SQL standard includes an EXECUTE statement,
   but it is only for use in embedded SQL.  This version of the
   EXECUTE statement also uses a somewhat different
   syntax.
  

 

 
  
# See Also
