---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/contrib-spi.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.458045Z"
---
# spi — Server Programming Interface features/examples

 
  SPI
  examples
 

 
  The spi module provides several workable examples
  of using the Server Programming Interface
  (SPI) and triggers.  While these functions are of
  some value in
  their own right, they are even more useful as examples to modify for
  your own purposes.  The functions are general enough to be used
  with any table, but you have to specify table and field names (as described
  below) while creating a trigger.
 

 
  Each of the groups of functions described below is provided as a
  separately-installable extension.
 

 
  autoinc — Functions for Autoincrementing Fields

  
   autoinc() is a trigger that stores the next value of
   a sequence into an integer field.  This has some overlap with the
   built-in serial column feature, but it is not the same.
   The trigger will replace the field's value only if that value is
   initially zero or null (after the action of the SQL statement that
   inserted or updated the row).  Also, if the sequence's next value is
   zero, nextval() will be called a second time in
   order to obtain a non-zero value.
  

  
   To use, create a BEFORE INSERT (or optionally BEFORE
   INSERT OR UPDATE) trigger using this function.  Specify two
   trigger arguments: the name of the integer column to be modified,
   and the name of the sequence object that will supply values.
   (Actually, you can specify any number of pairs of such names, if
   you'd like to update more than one autoincrementing column.)
  

  
   There is an example in autoinc.example.
  

 

 
  insert_username — Functions for Tracking Who Changed a Table

  
   insert_username() is a trigger that stores the current
   user's name into a text field.  This can be useful for tracking
   who last modified a particular row within a table.
  

  
   To use, create a BEFORE INSERT and/or UPDATE
   trigger using this function.  Specify a single trigger
   argument: the name of the text column to be modified.
  

  
   There is an example in insert_username.example.
  

 

 
  moddatetime — Functions for Tracking Last Modification Time

  
   moddatetime() is a trigger that stores the current
   time into a timestamp field.  This can be useful for tracking
   the last modification time of a particular row within a table.
  

  
   To use, create a BEFORE UPDATE
   trigger using this function.  Specify a single trigger
   argument: the name of the column to be modified.
   The column must be of type timestamp or timestamp with
   time zone.
  

  
   There is an example in moddatetime.example.
