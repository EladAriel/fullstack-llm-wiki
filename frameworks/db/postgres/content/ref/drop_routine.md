---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_routine.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.553829Z"
---
DROP ROUTINE
 

 
  
# DROP ROUTINE

  7
  SQL - Language Statements
 

 
  
# DROP ROUTINE

  remove a routine
 

 

DROP ROUTINE [ IF EXISTS ] name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ] [, ...]
    [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP ROUTINE removes the definition of one or more
   existing routines.  The term routine includes
   aggregate functions, normal functions, and procedures.  See
   under , ,
   and  for the description of the
   parameters, more examples, and further details.
  

 

 
  
# Notes

  
   The lookup rules used by DROP ROUTINE are
   fundamentally the same as for DROP PROCEDURE; in
   particular, DROP ROUTINE shares that command's
   behavior of considering an argument list that has
   no argmode markers to be
   possibly using the SQL standard's definition that OUT
   arguments are included in the list.  (DROP AGGREGATE
   and DROP FUNCTION do not do that.)
  

  
   In some cases where the same name is shared by routines of different
   kinds, it is possible for DROP ROUTINE to fail with
   an ambiguity error when a more specific command (DROP
   FUNCTION, etc.) would work.  Specifying the argument type
   list more carefully will also resolve such problems.
  

  
   These lookup rules are also used by other commands that
   act on existing routines, such as ALTER ROUTINE
   and COMMENT ON ROUTINE.
  

 

 
  
# Examples

  
   To drop the routine foo for type
   integer:

```

DROP ROUTINE foo(integer);

```

   This command will work independent of whether foo is an
   aggregate, function, or procedure.
  

 

 
  
# Compatibility

  
   This command conforms to the SQL standard, with
   these PostgreSQL extensions:
   
    
     The standard only allows one routine to be dropped per command.

    
    
     The IF EXISTS option is an extension.

    
    
     The ability to specify argument modes and names is an
     extension, and the lookup rules differ when modes are given.

    
    
     User-definable aggregate functions are an extension.

    
   

 

 
  
# See Also

  
   
   
   
   
  

  
   Note that there is no CREATE ROUTINE command.
