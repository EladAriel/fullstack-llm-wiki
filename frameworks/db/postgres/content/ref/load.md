---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/load.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.542761Z"
---
LOAD
 

 
  
# LOAD

  7
  SQL - Language Statements
 

 
  
# LOAD

  load a shared library file
 

 

LOAD 'filename'

 

 
  
# Description

  
   This command loads a shared library file into the PostgreSQL
   server's address space.  If the file has been loaded already,
   the command does nothing.  Shared library files that contain C functions
   are automatically loaded whenever one of their functions is called.
   Therefore, an explicit LOAD is usually only needed to
   load a library that modifies the server's behavior through hooks
   rather than providing a set of functions.
  

  
   The library file name is typically given as just a bare file name,
   which is sought in the server's library search path (set
   by ).  Alternatively it can be
   given as a full path name.  In either case the platform's standard shared
   library file name extension may be omitted.
   See  for more information on this topic.
  

  
   $libdir/plugins
  

  
   Non-superusers can only apply LOAD to library files
   located in $libdir/plugins/ — the specified
   filename must begin
   with exactly that string.  (It is the database administrator's
   responsibility to ensure that only safe libraries
   are installed there.)
  

 

 
  
# Compatibility

  
   LOAD is a PostgreSQL
   extension.
  

 

 
  
# See Also
