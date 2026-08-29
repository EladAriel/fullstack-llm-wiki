---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/pgtesttiming.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.567147Z"
---
pg_test_timing
 

 
  
# pg_test_timing

  1
  Application
 

 
  
# pg_test_timing

  measure timing overhead
 

 
  
   pg_test_timing
   option
  
 

 
  
# Description

 
  pg_test_timing is a tool to measure the
  timing overhead on your system and confirm that the system time never
  moves backwards.  It reads supported clock sources over and over again
  as fast as it can for a specified length of time, and then prints
  statistics about the observed differences in successive clock readings,
  as well as which clock source will be used.
 

 
  Smaller (but not zero) differences are better, since they imply both
  more-precise clock hardware and less overhead to collect a clock reading.
  Systems that are slow to collect timing data can give less accurate
  EXPLAIN ANALYZE results.
 

 
  This tool is also helpful to determine if
  the track_io_timing configuration parameter is likely
  to produce useful results, and whether the
  TSC clock source (see
  ) is available and if it will be
  used by default.
 

 

 
  
# Options

   
    pg_test_timing accepts the following
    command-line options:

    

     
      -c cutoff
      --cutoff=cutoff
      
       
        Specifies the cutoff percentage for the list of exact observed
        timing durations (that is, the changes in the system clock value
        from one reading to the next).  The list will end once the running
        percentage total reaches or exceeds this value, except that the
        largest observed duration will always be printed.  The default
        cutoff is 99.99.
       

      
     

     
      -d duration
      --duration=duration
      
       
        Specifies the test duration, in seconds. Longer durations
        give slightly better accuracy, and are more likely to discover
        problems with the system clock moving backwards. The default
        test duration is 3 seconds.
       

      
     

     
      -V
      --version
      
       
        Print the pg_test_timing version and exit.
       

      
     

     
      -?
      --help
      
       
        Show help about pg_test_timing command line
        arguments, and exit.
       

      
     

    
   

 

 
  
# Usage

 
  
# Interpreting Results

  
   The first block of output has four columns, with rows showing a
   shifted-by-one log2(ns) histogram of timing durations (that is, the
   differences between successive clock readings).  This is not the
   classic log2(n+1) histogram as it counts zeros separately and then
   switches to log2(ns) starting from value 1.
  

  
   The columns are:
   
    
     nanosecond value that is >= the durations in this
     bucket
    
    
     percentage of durations in this bucket
    
    
     running-sum percentage of durations in this and previous
     buckets
    
    
     count of durations in this bucket
    
   
  

  
   The second block of output goes into more detail, showing the exact
   timing differences observed.  For brevity this list is cut off when the
   running-sum percentage exceeds the user-selectable cutoff value.
   However, the largest observed difference is always shown.
  

  
   On platforms that support the TSC clock source,
   additional output sections are shown for the RDTSCP
   instruction (used for general timing needs, such as
   track_io_timing) and the RDTSC
   instruction (used for EXPLAIN ANALYZE).  At the end
   of the output, the TSC frequency, which may either be
   sourced from CPU information directly, or the alternate calibration
   mechanism are shown, as well as whether the TSC clock
   source will be used by default.
  

  
   The example results below show system clock timing where 99.99% of loops
   took between 16 and 63 nanoseconds.  In the second block, we can see that
   the typical loop time is 40 nanoseconds, and the readings appear to have
   full nanosecond precision.  Following the system clock results, the
   TSC clock source results are shown, in the same fashion.
   The RDTSCP instruction shows most loops completing in
   20–30 nanoseconds, while the RDTSC instruction is
   the fastest with an average loop time of 20 nanoseconds.  In this example
   the TSC clock source will be used by default, but can be
   disabled by setting timing_clock_source to
   system.
  

  

```

```

  

 
 

 
  
# See Also

  
   
   
   Wiki
   discussion about timing
