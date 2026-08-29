---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_server.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.536558Z"
---
ALTER SERVER
 

 
  
# ALTER SERVER

  7
  SQL - Language Statements
 

 
  
# ALTER SERVER

  change the definition of a foreign server
 

 

ALTER SERVER name [ VERSION 'new_version' ]
    [ OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] ) ]
ALTER SERVER name OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }
ALTER SERVER name RENAME TO new_name

 

 
  
# Description

  
   ALTER SERVER changes the definition of a foreign
   server.  The first form changes the server version string or the
   generic options of the server (at least one clause is required).
   The second form changes the owner of the server.
  

  
   To alter the server you must be the owner of the server.
   Additionally to alter the owner, you must be able to
   SET ROLE to the new owning role, and you must
   have USAGE privilege on the server's foreign-data
   wrapper.  (Note that superusers satisfy all these criteria
   automatically.)
  

 

 
  
# Parameters

  
   
    name
    
     
      The name of an existing server.
     

    
   

   
    new_version
    
     
      New server version.
     

    
   

   
    OPTIONS ( [ ADD | SET | DROP ] option ['value'] [, ... ] )
    
     
      Change options for the
      server.  ADD, SET, and DROP
      specify the action to be performed.  ADD is assumed
      if no operation is explicitly specified.  Option names must be
      unique; names and values are also validated using the server's
      foreign-data wrapper library.
     

    
   

   
    new_owner
    
     
      The user name of the new owner of the foreign server.
     

    
   

   
    new_name
    
     
      The new name for the foreign server.
     

    
   
  
 

 
  
# Examples

  
   Alter server foo, add connection options:

```

ALTER SERVER foo OPTIONS (host 'foo', dbname 'foodb');

```

  

  
   Alter server foo, change version,
   change host option:

```

ALTER SERVER foo VERSION '8.4' OPTIONS (SET host 'baz');

```

 

 
  
# Compatibility

  
   ALTER SERVER conforms to ISO/IEC 9075-9 (SQL/MED).
   The OWNER TO and RENAME forms are
   PostgreSQL extensions.
  

 

 
  
# See Also
