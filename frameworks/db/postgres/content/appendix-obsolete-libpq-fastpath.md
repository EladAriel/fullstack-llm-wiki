---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/appendix-obsolete-libpq-fastpath.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.473281Z"
---
# libpq Fast-Path Interface Removed

   
    fast path
   

   
    PQfn
   

   
    In PostgreSQL 19 and below,
    libpq supported a fast-path interface to send
    simple function calls to the server via the PQfn
    function.  This interface was unsafe and obsolete, and thus was removed in
    PostgreSQL 20.  The PQfn
    symbol still exists so that applications continue to link, but it now
    always fails.  One can achieve similar performance and greater
    functionality by setting up a prepared statement to define the function
    call.  Then, executing the statement with binary transmission of parameters
    and results substitutes for a fast-path function call.
