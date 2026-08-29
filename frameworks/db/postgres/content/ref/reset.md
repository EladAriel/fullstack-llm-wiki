---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/reset.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.557645Z"
---
RESET
 

 
  
# RESET

  7
  SQL - Language Statements
 

 
  
# RESET

  restore the value of a run-time parameter to the default value
 

 

RESET configuration_parameter
RESET ALL

 

 
  
# Description

  
   RESET restores run-time parameters to their
   default values.  RESET is an alternative
   spelling for

SET configuration_parameter TO DEFAULT

   Refer to  for
   details.
  

  
   The default value is defined as the value that the parameter would
   have had, if no SET had ever been issued for it in the
   current session.  The actual source of this value might be a
   compiled-in default, the configuration file, command-line options,
   or per-database or per-user default settings.  This is subtly different
   from defining it as the value that the parameter had at session
   start, because if the value came from the configuration file, it
   will be reset to whatever is specified by the configuration file now.
   See  for details.
  

  
   The transactional behavior of RESET is the same as
   SET: its effects will be undone by transaction rollback.
  

 

 
  
# Parameters

  
   
    configuration_parameter
    
     
      Name of a settable run-time parameter.  Available parameters are
      documented in  and on the
       reference page.
     

    
   

   
    ALL
    
     
      Resets all settable run-time parameters to default values.
     

    
   
  
 

 
  
# Examples

  
   Set the timezone configuration variable to its default value:

```

RESET timezone;

```

 

 
  
# Compatibility

  
   RESET is a PostgreSQL extension.
  

 

 
  
# See Also
