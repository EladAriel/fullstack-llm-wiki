---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/alter_conversion.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.568161Z"
---
ALTER CONVERSION
 

 
  
# ALTER CONVERSION

  7
  SQL - Language Statements
 

 
  
# ALTER CONVERSION

  change the definition of a conversion
 

 

ALTER CONVERSION name RENAME TO new_name
ALTER CONVERSION name OWNER TO { new_owner | CURRENT_ROLE | CURRENT_USER | SESSION_USER }
ALTER CONVERSION name SET SCHEMA new_schema

 

 
  
# Description

  
   ALTER CONVERSION changes the definition of a
   conversion.
  

  
   You must own the conversion to use ALTER CONVERSION.
   To alter the owner, you must be able to SET ROLE to the
   new owning role, and that role must have CREATE
   privilege on the conversion's schema.
   (These restrictions enforce that altering the
   owner doesn't do anything you couldn't do by dropping and recreating the
   conversion. However, a superuser can alter ownership of any conversion
   anyway.)
  

 

 
  
# Parameters

  
   
    name
    
     
      The name (optionally schema-qualified) of an existing conversion.
     

    
   

   
    new_name
    
     
      The new name of the conversion.
     

    
   

   
    new_owner
    
     
      The new owner of the conversion.
     

    
   

   
    new_schema
    
     
      The new schema for the conversion.
     

    
   
  
 

 
  
# Examples

  
   To rename the conversion iso_8859_1_to_utf8 to
   latin1_to_unicode:

```

ALTER CONVERSION iso_8859_1_to_utf8 RENAME TO latin1_to_unicode;

```

  

  
   To change the owner of the conversion iso_8859_1_to_utf8 to
   joe:

```

ALTER CONVERSION iso_8859_1_to_utf8 OWNER TO joe;

```

 

 
  
# Compatibility

  
   There is no ALTER CONVERSION statement in the SQL
   standard.
  

 

 
  
# See Also
