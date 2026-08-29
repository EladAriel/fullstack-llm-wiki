---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/create_user_mapping.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.560055Z"
---
CREATE USER MAPPING
 

 
  
# CREATE USER MAPPING

  7
  SQL - Language Statements
 

 
  
# CREATE USER MAPPING

  define a new mapping of a user to a foreign server
 

 

CREATE USER MAPPING [ IF NOT EXISTS ] FOR { user_name | USER | CURRENT_ROLE | CURRENT_USER | PUBLIC }
    SERVER server_name
    [ OPTIONS ( option 'value' [ , ... ] ) ]

 

 
  
# Description

  
   CREATE USER MAPPING defines a mapping of a user
   to a foreign server.  A user mapping typically encapsulates
   connection information that a foreign-data wrapper uses together
   with the information encapsulated by a foreign server to access an
   external data resource.
  

  
   The owner of a foreign server can create user mappings for that
   server for any user.  Also, a user can create a user mapping for
   their own user name if USAGE privilege on the server has
   been granted to the user.
  

 

 
  
# Parameters

  
  
    IF NOT EXISTS
    
     
      Do not throw an error if a mapping of the given user to the given foreign
      server already exists. A notice is issued in this case.  Note that there
      is no guarantee that the existing user mapping is anything like the one
      that would have been created.
     

    
   

   
    user_name
    
     
      The name of an existing user that is mapped to foreign server.
      CURRENT_ROLE, CURRENT_USER, and USER match the name of
      the current user.  When PUBLIC is specified, a
      so-called public mapping is created that is used when no
      user-specific mapping is applicable.
     

    
   

   
    server_name
    
     
      The name of an existing server for which the user mapping is
      to be created.
     

    
   

   
    OPTIONS ( option 'value' [, ... ] )
    
     
      This clause specifies the options of the user mapping.  The
      options typically define the actual user name and password of
      the mapping.  Option names must be unique.  The allowed option
      names and values are specific to the server's foreign-data wrapper.
     

    
   
  
 

 
  
# Examples

  
   Create a user mapping for user bob, server foo:

```

CREATE USER MAPPING FOR bob SERVER foo OPTIONS (user 'bob', password 'secret');

```

 

 
  
# Compatibility

  
   CREATE USER MAPPING conforms to ISO/IEC 9075-9 (SQL/MED).
  

 

 
  
# See Also
