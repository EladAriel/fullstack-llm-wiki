---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/dfunc.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.473791Z"
---
# Compiling and Linking Dynamically-Loaded Functions

 
  Before you are able to use your
  PostgreSQL extension functions written in
  C, they must be compiled and linked in a special way to produce a
  file that can be dynamically loaded by the server.  To be precise, a
  shared library needs to be
  created.shared library

 

 
  For information beyond what is contained in this section
  you should read the documentation of your
  operating system, in particular the manual pages for the C compiler,
  cc, and the link editor, ld.
  In addition, the PostgreSQL source code
  contains several working examples in the
  contrib directory.  If you rely on these
  examples you will make your modules dependent on the availability
  of the PostgreSQL source code, however.
 

 
  Creating shared libraries is generally analogous to linking
  executables: first the source files are compiled into object files,
  then the object files are linked together.  The object files need to
  be created as position-independent code
  (PIC),PIC which
  conceptually means that they can be placed at an arbitrary location
  in memory when they are loaded by the executable.  (Object files
  intended for executables are usually not compiled that way.)  The
  command to link a shared library contains special flags to
  distinguish it from linking an executable (at least in theory
  — on some systems the practice is much uglier).
 

 
  In the following examples we assume that your source code is in a
  file foo.c and we will create a shared library
  foo.so.  The intermediate object file will be
  called foo.o unless otherwise noted.  A shared
  library can contain more than one object file, but we only use one
  here.
 

  
   
    
     FreeBSD
     FreeBSDshared library
    
    
     
      The compiler flag to create PIC is
      -fPIC.  To create shared libraries the compiler
      flag is -shared.

cc -fPIC -c foo.c
cc -shared -o foo.so foo.o

      This is applicable as of version 13.0 of
      FreeBSD, older versions used
      the gcc compiler.
     
    
   

   
    
     Linux
     Linuxshared library
    
    
     
      The compiler flag to create PIC is
      -fPIC.
      The compiler flag to create a shared library is
      -shared.  A complete example looks like this:

cc -fPIC -c foo.c
cc -shared -o foo.so foo.o

     
    
   

   
    
     macOS
     macOSshared library
    
    
     
      Here is an example.  It assumes the developer tools are installed.

cc -c foo.c
cc -bundle -flat_namespace -undefined suppress -o foo.so foo.o

     
    
   

   
    
     NetBSD
     NetBSDshared library
    
    
     
      The compiler flag to create PIC is
      -fPIC.  For ELF systems, the
      compiler with the flag -shared is used to link
      shared libraries.  On the older non-ELF systems, ld
      -Bshareable is used.

gcc -fPIC -c foo.c
gcc -shared -o foo.so foo.o

     
    
   

   
    
     OpenBSD
     OpenBSDshared library
    
    
     
      The compiler flag to create PIC is
      -fPIC.  ld -Bshareable is
      used to link shared libraries.

gcc -fPIC -c foo.c
ld -Bshareable -o foo.so foo.o

     
    
   

   
    
     Solaris
     Solarisshared library
    
    
     
      The compiler flag to create PIC is
      -fPIC with GCC.  To
      link shared libraries, the compiler option is
      -shared with GCC.

gcc -fPIC -c foo.c
gcc -shared -o foo.so foo.o

     
    
   

  

 
  
   If this is too complicated for you, you should consider using
   
   GNU Libtool,
   which hides the platform differences behind a uniform interface.
  
 

 
  The resulting shared library file can then be loaded into
  PostgreSQL.  When specifying the file name
  to the CREATE FUNCTION command, one must give it
  the name of the shared library file, not the intermediate object file.
  Note that the system's standard shared-library extension (usually
  .so or .sl) can be omitted from
  the CREATE FUNCTION command, and normally should
  be omitted for best portability.
 

 
  Refer back to  about where the
  server expects to find the shared library files.
