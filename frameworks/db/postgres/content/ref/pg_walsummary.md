---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/pg_walsummary.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.584190Z"
---
pg_walsummary
 

 
  
# pg_walsummary

  1
  Application
 

 
  
# pg_walsummary

  print contents of WAL summary files
 

 
  
   pg_walsummary
   option
   filename
  
 

 
  
# Description

  
   pg_walsummary is used to print the contents of
   WAL summary files. These binary files are found in the
   pg_wal/summaries subdirectory of the data directory,
   and can be converted to text using this tool. This is not ordinarily
   necessary, since WAL summary files primarily exist to support
   incremental backup,
   but it may be useful for debugging purposes.
  

  
   A WAL summary file is indexed by tablespace OID, relation OID, and relation
   fork. For each relation fork, it stores the list of blocks that were
   modified by WAL within the range summarized in the file. It can also
   store a "limit block," which is 0 if the relation fork was created or
   truncated within the relevant WAL range, and otherwise the shortest length
   to which the relation fork was truncated. If the relation fork was not
   created, deleted, or truncated within the relevant WAL range, the limit
   block is undefined or infinite and will not be printed by this tool.
  

 

 
  
# Options

   
    
     
      filename
      
       
        Specifies the name of a WAL summary file, found in the
        pg_wal/summaries subdirectory of the data directory.
       

      
     

     
      -i
      --individual
      
       
        By default, pg_walsummary prints one line of output
        for each range of one or more consecutive modified blocks. This can
        make the output a lot briefer, since a relation where all blocks from
        0 through 999 were modified will produce only one line of output rather
        than 1000 separate lines. This option requests a separate line of
        output for every modified block.
       

      
     

     
      -q
      --quiet
      
       
        Do not print any output, except for errors. This can be useful
        when you want to know whether a WAL summary file can be successfully
        parsed but don't care about the contents.
       

      
     

     
      -V
      --version
      
       
        Display version information, then exit.
       

      
     

     
       -?
       --help
       
       
       Shows help about pg_walsummary command line
       arguments, and exits.
       

       
     

    
   

 

 
  
# Environment

  
   The environment variable PG_COLOR specifies whether to use
   color in diagnostic messages. Possible values are
   always, auto and
   never.
  

 

 
  
# See Also
