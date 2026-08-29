---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/drop_conversion.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.550861Z"
---
DROP CONVERSION
 

 
  
# DROP CONVERSION

  7
  SQL - Language Statements
 

 
  
# DROP CONVERSION

  remove a conversion
 

 

DROP CONVERSION [ IF EXISTS ] name [ CASCADE | RESTRICT ]

 

 
  
# Description

  
   DROP CONVERSION removes a previously defined conversion.
   To be able to drop a conversion, you must own the conversion.
  

 

 
  
# Parameters

   
    
     IF EXISTS
     
      
       Do not throw an error if the conversion does not exist.
       A notice is issued in this case.
      

     
    

    
     name

     
      
       The name of the conversion. The conversion name can be
       schema-qualified.
      

     
    

    
     CASCADE
     RESTRICT

     
      
       These key words do not have any effect, since there are no
       dependencies on conversions.
      

     
    
   
 

 
  
# Examples

  
   To drop the conversion named myname:

```

DROP CONVERSION myname;

```

 

 
  
# Compatibility

  
   There is no DROP CONVERSION statement in the SQL
   standard, but a DROP TRANSLATION statement that
   goes along with the CREATE TRANSLATION statement
   that is similar to the CREATE CONVERSION
   statement in PostgreSQL.
  

 

 
  
# See Also
