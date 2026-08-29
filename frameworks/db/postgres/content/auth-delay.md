---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/auth-delay.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.425050Z"
---
# auth_delay — pause on authentication failure

 
  auth_delay
 

 
  auth_delay causes the server to pause briefly before
  reporting authentication failure, to make brute-force attacks on database
  passwords more difficult.  Note that it does nothing to prevent
  denial-of-service attacks, and may even exacerbate them, since processes
  that are waiting before reporting authentication failure will still consume
  connection slots.
 

 
  In order to function, this module must be loaded via
   in postgresql.conf.
 

 
  Configuration Parameters

  
   
    
     auth_delay.milliseconds (integer)
     
      auth_delay.milliseconds configuration parameter
     
    
    
     
      The number of milliseconds to wait before reporting an authentication
      failure.  The default is 0.
     
    
   
  

  
   These parameters must be set in postgresql.conf.
   Typical usage might be:
  

# postgresql.conf
shared_preload_libraries = 'auth_delay'

auth_delay.milliseconds = '500'

 

 
  Author

  
   KaiGai Kohei kaigai@ak.jp.nec.com
