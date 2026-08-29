---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/show.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.569810Z"
---
SHOW
 

 
  
# SHOW

  7
  SQL - Language Statements
 

 
  
# SHOW

  show the value of a run-time parameter
 

 

SHOW name
SHOW ALL

 

 
  
# Description

  
   SHOW will display the current setting of
   run-time parameters. These variables can be set using the
   SET statement, by editing the
   postgresql.conf configuration file, through
   the PGOPTIONS environmental variable (when using
   libpq or a libpq-based
   application), or through command-line flags when starting the
   postgres server.  See  for details.
  

 

 
  
# Parameters

  
   
    name
    
     
      The name of a run-time parameter.  Available parameters are
      documented in  and on the  reference page.  In
      addition, there are a few parameters that can be shown but not
      set:

      
       
        SERVER_VERSION
        
         
          Shows the server's version number.
         

        
       

       
        SERVER_ENCODING
        
         
          Shows the server-side character set encoding.  At present,
          this parameter can be shown but not set, because the
          encoding is determined at database creation time.
         

        
       

       
        IS_SUPERUSER
        
         
          True if the current role has superuser privileges.
         

        
       
      

    
   

   
    ALL
    
     
      Show the values of all configuration parameters, with descriptions.
     

    
   
  
 

 
  
# Notes

  
   The function current_setting produces
   equivalent output; see .
   Also, the
   pg_settings
   system view produces the same information.

  

 

 
  
# Examples

  
   Show the current setting of the parameter DateStyle:

```

SHOW DateStyle;
 DateStyle
-----------
 ISO, MDY
(1 row)

```

  

  
   Show the current setting of the parameter geqo:

```

SHOW geqo;
 geqo
------
 on
(1 row)

```

  

  
   Show all settings:

```

SHOW ALL;
            name         | setting |                description
-------------------------+---------+-------------------------------------------------
 allow_system_table_mods | off     | Allows modifications of the structure of ...
    .
    .
    .
 xmloption               | content | Sets whether XML data in implicit parsing ...
 zero_damaged_pages      | off     | Continues processing past damaged page headers.
(196 rows)

```

 

 
  
# Compatibility

  
   The SHOW command is a
   PostgreSQL extension.
  

 

 
  
# See Also
