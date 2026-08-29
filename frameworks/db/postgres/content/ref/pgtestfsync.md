---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/pgtestfsync.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.580360Z"
---
pg_test_fsync
 

 
  
# pg_test_fsync

  1
  Application
 

 
  
# pg_test_fsync

  determine fastest wal_sync_method for PostgreSQL
 

 
  
   pg_test_fsync
   option
  
 

 
  
# Description

 
  pg_test_fsync is intended to give you a reasonable
  idea of what the fastest  is on your
  specific system,
  as well as supplying diagnostic information in the event of an identified I/O
  problem.  However, differences shown by
  pg_test_fsync might not make any significant
  difference in real database throughput, especially since many database servers
  are not speed-limited by their write-ahead logs.
  pg_test_fsync reports average file sync operation
  time in microseconds for each wal_sync_method, which can also be used to
  inform efforts to optimize the value of .
 

 

 
  
# Options

   
    pg_test_fsync accepts the following
    command-line options:

    

     
      -f
      --filename
      
       
        Specifies the file name to write test data in.
        This file should be in the same file system that the
        pg_wal directory is or will be placed in.
        (pg_wal contains the WAL files.)
        The default is pg_test_fsync.out in the current
        directory.
       

      
     

     
      -s
      --secs-per-test
      
       
        Specifies the number of seconds for each test.  The more time
        per test, the greater the test's accuracy, but the longer it takes
        to run.  The default is 5 seconds, which allows the program to
        complete in under 2 minutes.
       

      
     

     
      -V
      --version
      
       
        Print the pg_test_fsync version and exit.
       

      
     

     
      -?
      --help
      
       
        Show help about pg_test_fsync command line
        arguments, and exit.
       

      
     
    
   

 

 
  
# Environment

  
   The environment variable PG_COLOR specifies whether to use
   color in diagnostic messages. Possible values are
   always, auto and
   never.
  

 

 
  
# See Also
