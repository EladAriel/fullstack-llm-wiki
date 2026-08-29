---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/pg_controldata.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.591525Z"
---
pg_controldata
 

 
  
# pg_controldata

  1
  Application
 

 
  
# pg_controldata

  display control information of a PostgreSQL database cluster
 

 
  
   pg_controldata
   option
   
    
     -D
     --pgdata
    
    datadir
   
  
 

 
  
# Description

  
   pg_controldata prints information initialized during
   initdb, such as the catalog version.
   It also shows information about write-ahead logging and checkpoint
   processing.  This information is cluster-wide, and not specific to any one
   database.
  

  
   This utility can only be run by the user who initialized the cluster because
   it requires read access to the data directory.
   You can specify the data directory on the command line, or use
   the environment variable PGDATA.
  

 

 
  
# Options

   
    
     
      -D datadir
      --pgdata=datadir
      
       
        Specifies the directory where the database cluster is stored.
       

      
     

     
       -V
       --version
       
       
        Print the pg_controldata version and exit.
       

       
     

     
      -?
      --help
       
        
         Show help about pg_controldata command line
         arguments, and exit.
        

       
      
    
   

 

 
  
# Environment

  
   
    PGDATA

    
     
      Default data directory location
     

    
   

   
    PG_COLOR
    
     
      Specifies whether to use color in diagnostic messages. Possible values
      are always, auto and
      never.
