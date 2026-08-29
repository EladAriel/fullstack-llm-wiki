---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_sequence.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.555802Z"
---
DROP SEQUENCE
 

 
  
# DROP SEQUENCE

  7
  SQL - Language Statements
 

 
  
# DROP SEQUENCE

  remove a sequence
 

 

DROP SEQUENCE [ IF EXISTS ] name [, ...] [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP SEQUENCE removes sequence number
   generators. A sequence can only be dropped by its owner or a superuser.
  

 

 
  
# Parameters

  
   
    IF EXISTS
    
     
      Do not throw an error if the sequence does not exist. A notice is issued
      in this case.
     

    
   

   
    name
    
     
      The name (optionally schema-qualified) of a sequence.
     

    
   

   
    CASCADE
    
     
      Automatically drop objects that depend on the sequence,
      and in turn all objects that depend on those objects
      (see ).
     

    
   

   
    RESTRICT
    
     
      Refuse to drop the sequence if any objects depend on it.  This
      is the default.
     

    
   
  
 

 
  
# Examples

  
   To remove the sequence serial:

```

DROP SEQUENCE serial;

```

 

 
  
# Compatibility

  
   DROP SEQUENCE conforms to the SQL
   standard, except that the standard only allows one
   sequence to be dropped per command, and apart from the
   IF EXISTS option, which is a PostgreSQL
   extension.
  

 

 
  
# See Also
