---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_user_mapping.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.533460Z"
---
ALTER USER MAPPING
 

 
  
# ALTER USER MAPPING

  7
  SQL - Language Statements
 

 
  
# ALTER USER MAPPING

  change the definition of a user mapping
 

 

ALTER USER MAPPING FOR { user_name | USER | CURRENT_ROLE | CURRENT_USER | SESSION_USER | PUBLIC }
    SERVER server_name
    OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] )

 

 
  
# Description

  
   ALTER USER MAPPING changes the definition of a
   user mapping.
  

  
   The owner of a foreign server can alter user mappings for that
   server for any user.  Also, a user can alter a user mapping for
   their own user name if USAGE privilege on the server has
   been granted to the user.
  

 

 
  
# Parameters

  
   
    user_name
    
     
      User name of the mapping. CURRENT_ROLE, CURRENT_USER,
      and USER match the name of the current
      user. PUBLIC is used to match all present and future
      user names in the system.
     

    
   

   
    server_name
    
     
      Server name of the user mapping.
     

    
   

   
    OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] )
    
     
      Change options for the user mapping. The new options override
      any previously specified
      options.  ADD, SET, and DROP
      specify the action to be performed.  ADD is assumed
      if no operation is explicitly specified.  Option names must be
      unique; options are also validated by the server's foreign-data
      wrapper.
     

    
   
  
 

 
  
# Examples

  
   Change the password for user mapping bob, server foo:

```

ALTER USER MAPPING FOR bob SERVER foo OPTIONS (SET password 'public');

```

 

 
  
# Compatibility

  
   ALTER USER MAPPING conforms to ISO/IEC 9075-9
   (SQL/MED).  There is a subtle syntax issue: The standard omits
   the FOR key word.  Since both CREATE
   USER MAPPING and DROP USER MAPPING use
   FOR in analogous positions, and IBM DB2 (being
   the other major SQL/MED implementation) also requires it
   for ALTER USER MAPPING, PostgreSQL diverges from
   the standard here in the interest of consistency and
   interoperability.
  

 

 
  
# See Also
