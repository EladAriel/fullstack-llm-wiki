---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/create_access_method.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.558022Z"
---
CREATE ACCESS METHOD
 

 
  
# CREATE ACCESS METHOD

  7
  SQL - Language Statements
 

 
  
# CREATE ACCESS METHOD

  define a new access method
 

 

CREATE ACCESS METHOD name
    TYPE access_method_type
    HANDLER handler_function

 

 
  
# Description

  
   CREATE ACCESS METHOD creates a new access method.
  

  
   The access method name must be unique within the database.
  

  
   Only superusers can define new access methods.
  

 

 
  
# Parameters

  
   
    name
    
     
      The name of the access method to be created.
     

    
   

   
    access_method_type
    
     
      This clause specifies the type of access method to define.
      Only TABLE and INDEX
      are supported at present.
     

    
   

   
    handler_function
    
     
      handler_function is the
      name (possibly schema-qualified) of a previously registered function
      that represents the access method.  The handler function must be
      declared to take a single argument of type internal,
      and its return type depends on the type of access method;
      for TABLE access methods, it must
      be table_am_handler and for INDEX
      access methods, it must be index_am_handler.
      The C-level API that the handler function must implement varies
      depending on the type of access method. The table access method API
      is described in  and the index access method
      API is described in .
     

    
   
  
 

 
  
# Examples

  
   Create an index access method heptree with
   handler function heptree_handler:

```

CREATE ACCESS METHOD heptree TYPE INDEX HANDLER heptree_handler;

```

 

 
  
# Compatibility

  
   CREATE ACCESS METHOD is a
   PostgreSQL extension.
  

 

 
  
# See Also
