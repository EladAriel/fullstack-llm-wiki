---
type: "Framework Learn Page"
framework: "PostgreSQL"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/ref/move.sgml"
source_commit: "6c5f1d6074208146930b67c2054509c3e82f6f7f"
source_commit_short: "6c5f1d6"
source_commit_date: "2026-08-28T23:24:47+02:00"
generated_at: "2026-08-29T09:39:24.540144Z"
---
MOVE
 

 
  cursor
  MOVE
 

 
  
# MOVE

  7
  SQL - Language Statements
 

 
  
# MOVE

  position a cursor
 

 

MOVE [ direction ] [ FROM | IN ] cursor_name

where direction can be one of:

    NEXT
    PRIOR
    FIRST
    LAST
    ABSOLUTE count
    RELATIVE count
    count
    ALL
    FORWARD
    FORWARD count
    FORWARD ALL
    BACKWARD
    BACKWARD count
    BACKWARD ALL

 

 
  
# Description

  
   MOVE repositions a cursor without retrieving any data.
   MOVE works exactly like the FETCH
   command, except it only positions the cursor and does not return rows.
  

  
   The parameters for the MOVE command are identical to
   those of the FETCH command; refer to
   
   for details on syntax and usage.
  

 

 
  
# Outputs

  
   On successful completion, a MOVE command returns a command
   tag of the form

```

MOVE count

```

   The count is the number
   of rows that a FETCH command with the same parameters
   would have returned (possibly zero).
  

 

 
  
# Examples

```

BEGIN WORK;
DECLARE liahona CURSOR FOR SELECT * FROM films;

-- Skip the first 5 rows:
MOVE FORWARD 5 IN liahona;
MOVE 5

-- Fetch the 6th row from the cursor liahona:
FETCH 1 FROM liahona;
 code  | title  | did | date_prod  |  kind  |  len
-------+--------+-----+------------+--------+-------
 P_303 | 48 Hrs | 103 | 1982-10-22 | Action | 01:37
(1 row)

-- Close the cursor liahona and end the transaction:
CLOSE liahona;
COMMIT WORK;

```

 

 
  
# Compatibility

  
   There is no MOVE statement in the SQL standard.
  

 

 
  
# See Also
