---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/pg_checksums.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.539892Z"
---
pg_checksums
 

 
  
# pg_checksums

  1
  Application
 

 
  
# pg_checksums

  enable, disable or check data checksums in a PostgreSQL database cluster
 

 
  
   pg_checksums
   option
   
    
     -D
     --pgdata
    
    datadir
   
  
 

 
  
# Description

  
   pg_checksums checks, enables or disables data
   checksums in a PostgreSQL cluster.  The server
   must be shut down cleanly before running pg_checksums.
   Checksums can also be enabled while the cluster is running using
    processing, see
    for further details on the different approaches.
   When verifying checksums, the exit
   status is zero if there are no checksum errors, and nonzero if at least one
   checksum failure is detected. When enabling or disabling checksums, the
   exit status is nonzero if the operation failed.
  

  
   When enabling checksums with pg_checksums, if
   checksums were in the process of being enabled using
     when the cluster was shut
   down, pg_checksums will still process all
   relation files regardless of the progress of online checksum processing.
  

  
   When verifying checksums, every file in the cluster is scanned. When
   enabling checksums, each relation file block with a changed checksum is
   rewritten in-place.
   Disabling checksums only updates the file pg_control.
  

 

 
  
# Options

   
    The following command-line options are available:

    
     
      -D datadir
      --pgdata=datadir
      
       
        Specifies the directory where the database cluster is stored.
       

      
     

     
      -c
      --check
      
       
        Checks checksums. This is the default mode if nothing else is
        specified.
       

      
     

     
      -d
      --disable
      
       
        Disables checksums.
       

      
     

     
      -e
      --enable
      
       
        Enables checksums.
       

      
     

     
      -f filenode
      --filenode=filenode
      
       
        Only validate checksums in the relation with filenode
        filenode.
       

      
     

     
      -N
      --no-sync
      
       
        By default, pg_checksums will wait for all files
        to be written safely to disk.  This option causes
        pg_checksums to return without waiting, which is
        faster, but means that a subsequent operating system crash can leave
        the updated data directory corrupt.  Generally, this option is useful
        for testing but should not be used on a production installation.
        This option has no effect when using --check.
       

      
     

     
      -P
      --progress
      
       
        Enable progress reporting. Turning this on will deliver a progress
        report while checking or enabling checksums.
       

      
     

     
      --sync-method=method
      
       
        When set to fsync, which is the default,
        pg_checksums will recursively open and synchronize
        all files in the data directory.  The search for files will follow
        symbolic links for the WAL directory and each configured tablespace.
       

       
        On Linux, syncfs may be used instead to ask the
        operating system to synchronize the whole file systems that contain the
        data directory, the WAL files, and each tablespace.  See
         for information about
        the caveats to be aware of when using syncfs.
       

       
        This option has no effect when --no-sync is used.
       

      
     

     
      -v
      --verbose
      
       
        Enable verbose output. Lists all checked files.
       

      
     

     
       -V
       --version
       
       
        Print the pg_checksums version and exit.
       

       
     

     
      -?
      --help
       
        
         Show help about pg_checksums command line
         arguments, and exit.
        

       
      
    
   

 

 
  
# Environment

  
   
    PGDATA

    
     
      Specifies the directory where the database cluster is
      stored; can be overridden using the -D option.
     

    
   

   
    PG_COLOR
    
     
      Specifies whether to use color in diagnostic messages. Possible values
      are always, auto and
      never.
     

    
   
  
 

 
  
# Notes

  
   Enabling checksums in a large cluster can potentially take a long time.
   During this operation, the cluster or other programs that write to the
   data directory must not be started or else data loss may occur.
  

  
   When using a replication setup with tools which perform direct copies
   of relation file blocks (for example ),
   enabling or disabling checksums can lead to page corruptions in the
   shape of incorrect checksums if the operation is not done consistently
   across all nodes. When enabling or disabling checksums in a replication
   setup, it is thus recommended to stop all the clusters before switching
   them all consistently. Destroying all standbys, performing the operation
   on the primary and finally recreating the standbys from scratch is also
   safe.
  

  
   If pg_checksums is aborted or killed while
   enabling or disabling checksums, the cluster's data checksum configuration
   remains unchanged, and pg_checksums can be
   re-run to perform the same operation.
  

  
   The target cluster must have the same major version as
   pg_checksums.
