---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_routine.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.551122Z"
---
ALTER ROUTINE
 

 
  
# ALTER ROUTINE

  7
  SQL - Language Statements
 

 
  
# ALTER ROUTINE

  change the definition of a routine
 

 

ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    action [ ... ] [ RESTRICT ]
ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    RENAME TO new_name
ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }
ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    SET SCHEMA new_schema
ALTER ROUTINE name [ ( [ [ argmode ] [ argname ] argtype [, ...] ] ) ]
    [ NO ] DEPENDS ON EXTENSION extension_name

where action is one of:

    IMMUTABLE | STABLE | VOLATILE
    [ NOT ] LEAKPROOF
    [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER
    PARALLEL { UNSAFE | RESTRICTED | SAFE }
    COST execution_cost
    ROWS result_rows
    SET configuration_parameter { TO | = } { value | DEFAULT }
    SET configuration_parameter FROM CURRENT
    RESET configuration_parameter
    RESET ALL

 

 
  
# Description

  
   ALTER ROUTINE changes the definition of a routine, which
   can be an aggregate function, a normal function, or a procedure.  See
   under , ,
   and  for the description of the
   parameters, more examples, and further details.
  

 

 
  
# Examples

  
   To rename the routine foo for type
   integer to foobar:

```

ALTER ROUTINE foo(integer) RENAME TO foobar;

```

   This command will work independent of whether foo is an
   aggregate, function, or procedure.
  

 

 
  
# Compatibility

  
   This statement is partially compatible with the ALTER
   ROUTINE statement in the SQL standard.  See
   under 
   and  for more details.  Allowing
   routine names to refer to aggregate functions is
   a PostgreSQL extension.
  

 

 
  
# See Also

  
   
   
   
   
  

  
   Note that there is no CREATE ROUTINE command.
