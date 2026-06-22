---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/release-19.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## Release 19

## Release date: 2026-??-??, AS OF 2026-06-17

## Overview

PostgreSQL 19 contains many new features and enhancements, including:

- fill in later

The above items and other new features of PostgreSQL 19 are explained in more detail in the sections below.

## Migration to Version 19

A dump/restore using `app-pg-dumpall` or use of `pgupgrade` or logical replication is required for those wishing to migrate data from any previous release. See `upgrading` for general information on migrating to new major releases.

Version 19 contains a number of changes that may affect compatibility with previous releases. Observe the following incompatibilities:

- Add server variable password_expiration_warning_threshold to warn about password expiration (Gilles Darold, Nathan Bossart) [§](commit_baseurl1d92e0c2c) The default warning period is seven days.
- Issue a warning after successful MD5 password authentication (Nathan Bossart) [§](commit_baseurlbc60ee860) The warning can be disabled via server variable md5_password_warnings. MD5 passwords were marked as deprecated in PostgreSQL 18.
- Remove RADIUS support (Thomas Munro) [§](commit_baseurla1643d40b) PostgreSQL only supported RADIUS over UDP, which is unfixably insecure.
- Force standard_conforming_strings to always be `on` in the database server (Tom Lane) [§](commit_baseurl457620845) Dumps created using pre-PostgreSQL 19 versions of pg_dump or pg_dumpall, and using `standard_conforming_strings = off`, will not properly load into PostgreSQL 19 and later servers. Users should create dumps using PostgreSQL 19 or later versions of these applications, or use `standard_conforming_strings = on`. Client applications still support operations with servers having `standard_conforming_strings = off`, for compatibility with old servers. The server variable `escape_string_warning` has been removed as unnecessary.
- Disallow carriage returns and line feeds in database, role, and tablespace names (Mahendra Singh Thalor) [§](commit_baseurlb380a56a3) pg_upgrade will also disallow upgrading of clusters that use such names. This was changed to avoid security problems.
- Change the default index opclasses for inet and cidr data types from `btree-gist` to GiST (Tom Lane) [§](commit_baseurlb3b0b4571) [§](commit_baseurlb352d3d80) The `btree-gist` `inet`/`cidr` opclasses are broken because they can exclude rows that should be returned. pg_upgrade will disallow upgrading of clusters with `btree-gist` `inet`/`cidr` indexes.
- Stop reordering non-schema objects created by CREATE SCHEMA (Tom Lane, Jian He) [§](commit_baseurla9c350d9e) [§](commit_baseurl404db8f9e) The goal of the reordering was to avoid dependencies, but it was imperfect. PostgreSQL now uses the specified object ordering, except for foreign keys which are created last.
- Disallow system columns from being used in COPY FROM ... WHERE (Tom Lane) [§](commit_baseurl21c69dc73) The values of such columns were not well-defined.
- Change a json_array() call which returns no rows to return an empty JSON array (Richard Guo) [§](commit_baseurl8d829f5a0) This previously returned `NULL`.
- Cause transactions to pass their `READ ONLY` and `DEFERRABLE` status to `postgres-fdw` sessions (Etsuro Fujita) [§](commit_baseurlde28140de) This means `READ ONLY` transactions can no longer modify rows processed by `postgres-fdw` sessions.
- Change default of max_locks_per_transaction from 64 to 128 (Heikki Linnakangas) [§](commit_baseurl79534f906) Lock size allocation has changed, so effectively settings must now be doubled to match their capacity in previous releases.
- Change JIT to be disabled by default (Jelte Fennema-Nio) [§](commit_baseurl7f8c88c2b) Previously JIT was enabled by default, and activated based on optimizer costs, but this costing has been determined to be unreliable. This change requires sites that are doing many large analytical queries to manually enable JIT.
- Rename column `sync_error_count` to `sync_table_error_count` in system view pg_stat_subscription_stats (Vignesh C) [§](commit_baseurl3edaf29fa) This is necessary since sequence errors are now tracked separately.
- Rename wait event type `BUFFERPIN` to `BUFFER` (Andres Freund) [§](commit_baseurl6c5c393b7)
- Change index access method handlers to use a static IndexAmRoutines structure, rather than dynamically allocated ones (Matthias van de Meent) [§](commit_baseurlbc6374cd7)
- Remove optimizer hook get_relation_info_hook and add better-placed hook build_simple_rel_hook (Robert Haas) [§](commit_baseurl91f33a2ae)
- Remove `MULE_INTERNAL` encoding (Thomas Munro) [§](commit_baseurl77645d44e) This encoding was complex and rarely used. Databases using it will need to be dumped and restored with a different encoding.

## Changes

Below you will find a detailed account of the changes between PostgreSQL 19 and the previous major release.

## Server

## Optimizer

- Allow `NOT IN` clauses to be converted to more efficient `ANTI JOIN`s when NULLs are not present (Richard Guo) [§](commit_baseurl383eb21eb)
- Allow more `LEFT JOIN`s to be converted to `ANTI JOIN`s (Tender Wang, Richard Guo) [§](commit_baseurlcf74558fe)
- Allow use of Memoize for `ANTI JOIN`s with unique inner sides (Richard Guo) [§](commit_baseurl0da29e4cb)
- Allow some aggregate processing to be performed before joins (Richard Guo, Antonin Houska) [§](commit_baseurl8e1185910) [§](commit_baseurlbd94845e8) [§](commit_baseurl3a08a2a8b) This can reduce the number of rows needed to be processed.
- Improve hash join's handling of tuples with `NULL` join keys (Tom Lane) [§](commit_baseurl1811f1af9)
- Improve the planning of semijoins (Richard Guo) [§](commit_baseurl24225ad9a)
- Allow Append and MergeAppend to consider explicit incremental sorts (Richard Guo) [§](commit_baseurl55a780e94)
- Convert IS [NOT] DISTINCT FROM NULL to `IS [NOT] NULL` during constant folding (Richard Guo) [§](commit_baseurlf41ab5157) The latter form is more easily optimized.
- Simplify IS [NOT] DISTINCT FROM to equality/inequality operators when inputs are proven non-nullable (Richard Guo) [§](commit_baseurl0a3796125)
- Perform earlier constant folding of `var` `IS [NOT] NULL` in the optimizer (Richard Guo) [§](commit_baseurle2debb643) This allows for later optimizations.
- Simplify COALESCE() and `ROW(...) IS [NOT] NULL` to avoid evaluating unnecessary arguments (Richard Guo) [§](commit_baseurl10c4fe074) [§](commit_baseurlcb7b7ec7a)
- Simplify `IS [NOT] TRUE/FALSE/UNKNOWN` to plain boolean expressions when the input is proven non-nullable (Richard Guo) [§](commit_baseurl0aaf0de7f)
- Speed up join selectivity computations for large optimizer statistics targets (Ilia Evdokimov, David Geier) [§](commit_baseurl057012b20)
- Enable proper optimizer statistics for functions returning boolean values (Tom Lane) [§](commit_baseurl1eccb9315)
- Allow extended statistics on virtual generated columns (Yugo Nagata) [§](commit_baseurlf7f4052a4)
- Allow function pg_restore_extended_stats() to restore optimizer extended statistics (Corey Huinker, Michael Paquier, Chao Li) [§](commit_baseurl0e80f3f88) [§](commit_baseurl302879bd6) [§](commit_baseurlefbebb4e8) [§](commit_baseurlba97bf9cb)
- Add function pg_clear_extended_stats() to remove extended statistics (Corey Huinker, Michael Paquier) [§](commit_baseurld756fa101)
- Adjust the optimizer to consider startup costs of partial paths (Robert Haas, Tomas Vondra) [§](commit_baseurl8300d3ad4)
- Allow negative values of pg_aggregate.aggtransspace to indicate unbounded memory usage (Richard Guo) [§](commit_baseurl185e30426) This information is used by the optimizer in planning memory usage.

## General Performance

- Improve performance of foreign key constraint checks (Junwang Zhao, Amit Langote, Chao Li) [§](commit_baseurl2da86c1ef) [§](commit_baseurle484b0eea) [§](commit_baseurlb7b27eb41) [§](commit_baseurl5c54c3ed1)
- Improve asynchronous I/O read-ahead scheduling for large requests (Andres Freund) [§](commit_baseurla9ee66881) [§](commit_baseurl8ca147d58) [§](commit_baseurlf63ca3379)
- Allow io_method method `worker` to automatically control needed background workers (Thomas Munro) [§](commit_baseurld1c01b79d) The new server variables are io_min_workers, io_max_workers, io_worker_idle_timeout, and io_worker_launch_interval.
- Allow query table scans to mark pages as all-visible in the visibility map (Melanie Plageman) [§](commit_baseurlb46e1e54d) Previously only VACUUM and COPY ... FREEZE could do this.
- Allow autovacuum to use parallel autovacuum workers (Daniil Davydov) [§](commit_baseurl1ff3180ca) [§](commit_baseurl2a3d2f9f6) The maximum number of workers is controlled by server variable autovacuum_max_parallel_workers and per-table storage parameter `autovacuum_parallel_workers`.
- Allow TID Range Scans to be parallelized (Cary Huang, David Rowley) [§](commit_baseurl0ca3b1697)
- Improve COPY FROM performance for text and CSV input using SIMD CPU instructions (Nazir Bilal Yavuz, Shinya Kato) [§](commit_baseurle0a3a3fd5)
- Improve NOTIFY to only wake up backends that are listening to specified notifications (Joel Jacobson) [§](commit_baseurl282b1cde9) Previously most backends were woken by NOTIFY.
- Change the default TOAST compression method from `pglz` to the more efficient `lz4` (Euler Taveira) [§](commit_baseurl34dfca293) This is done by changing the default for server variable default_toast_compression.
- Improve performance of internal row deformation (David Rowley) [§](commit_baseurlc456e3911)
- Improve performance of repeated UTF-8 case-folding operations (Andreas Karlsson) [§](commit_baseurlc4ff35f10)
- Improve performance of hash index bulk-deletion and GIN index vacuuming using streaming reads (Xuneng Zhou) [§](commit_baseurlbfa3c4f10) [§](commit_baseurl6c228755a)
- Improve sort performance using radix sort (John Naylor) [§](commit_baseurlef3c3cf6d)
- Improve timing performance measurements (Lukas Fittl, Andres Freund, David Geier) [§](commit_baseurl294520c44) [§](commit_baseurl16fca4825) This benefits EXPLAIN (ANALYZE, TIMING) and pg_test_timing, and is controlled via server variable timing_clock_source.
- Optimize plpgsql syntax `SELECT simple-expression INTO` `var` (Tom Lane) [§](commit_baseurlce8d5fe0e)

## System Views

- Add system view pg_stat_lock and function pg_stat_get_lock() to report per-lock-type statistics (Bertrand Drouvot) [§](commit_baseurl4019f725f)
- Add system view pg_stat_recovery to report recovery status (Xuneng Zhou, Shinya Kato) [§](commit_baseurl01d485b14) [§](commit_baseurl2d4ead6f4)
- Add system view pg_stat_autovacuum_scores to report per-table autovacuum details (Sami Imseih) [§](commit_baseurl87f61f0c8)
- Add system view pg_dsm_registry_allocations to report dynamic shared memory details (Florents Tselai, Nathan Bossart) [§](commit_baseurl167ed8082) [§](commit_baseurlf894acb24)
- Add vacuum initiation details to system view pg_stat_progress_vacuum (Shinya Kato) [§](commit_baseurl0d7895206) The new `started_by` column reports the initiator of the vacuum, and `mode` indicates its aggressiveness.
- Add analyze initiation details to system view pg_stat_progress_analyze (Shinya Kato) [§](commit_baseurlab40db385) The new `started_by` column reports the initiator of the analyze.
- Add `mem_exceeded_count` column to system view pg_stat_replication_slots (Bertrand Drouvot) [§](commit_baseurld3b6183dd) This reports the number of times that logical_decoding_work_mem was exceeded.
- Add slot synchronization skip information to pg_stat_replication_slots and pg_replication_slots (Shlok Kyal) [§](commit_baseurl76b78721c) [§](commit_baseurle68b6adad) [§](commit_baseurl5db6a344a) The new columns are `slotsync_skip_count`, `slotsync_last_skip`, and `slotsync_skip_reason`.
- Add `update_deleted` column to system view pg_stat_subscription_stats (Zhijie Hou) [§](commit_baseurlfd5a1a0c3) This reports the number of rows where updates were ignored due to concurrent deletes. This requires the subscriber have `retain_dead_tuples` enabled.
- Add `sync_seq_error_count` column to system view pg_stat_subscription_stats to report sequence synchronization errors (Vignesh C) [§](commit_baseurlf6a4c498d) [§](commit_baseurl3edaf29fa)
- Add `stats_reset` column to system views pg_stat_all_tables, pg_stat_all_indexes, and pg_statio_all_sequences (Bertrand Drouvot, Sami Imseih, Shihao Zhong) [§](commit_baseurla5b543258) It also appears in the `sys` and `user` view variants.
- Add `stats_reset` column to system views pg_stat_user_functions and pg_stat_database_conflicts (Bertrand Drouvot, Shihao Zhong) [§](commit_baseurlb71bae41a) [§](commit_baseurl8fe315f18)
- Add `location` column to system views pg_available_extensions and pg_available_extension_versions to report the file system directory of extensions (Matheus Alcantara) [§](commit_baseurlf3c9e341c)
- Add `backup_type` column to system view pg_stat_progress_basebackup to report the type of backup (Shinya Kato) [§](commit_baseurldeb674454) Possible values are `full` or `incremental`.
- Add `connecting` value to system view column pg_stat_wal_receiver.status (Xuneng Zhou) [§](commit_baseurla36164e74)
- Add reporting of the bytes written to WAL for full page images (Shinya Kato) [§](commit_baseurlf9a09aa29) This is accessible via system view pg_stat_wal and function pg_stat_get_backend_wal().
- Add columns to system views pg_stats, pg_stats_ext, and pg_stats_ext_exprs (Corey Huinker) [§](commit_baseurl3b88e50d6) Adds table `OID` and attribute number columns to pg_stats, and table `OID` and statistics object `OID` columns to the other two.
- Add information about range type extended statistics to system view pg_stats_ext_exprs (Corey Huinker, Michael Paquier) [§](commit_baseurl307447e6d)

## Monitoring

- Allow log_min_messages log levels to be specified by process type (Euler Taveira) [§](commit_baseurl38e0190ce) The new format is `type`:`level`. A value without a colon controls all process types, allowing backward compatibility.
- Add server variable log_autoanalyze_min_duration to log long-running analyze operations by autovacuum operations (Shinya Kato) [§](commit_baseurldd3ae3783) Server variable log_autovacuum_min_duration now only controls logging of vacuum operations by autovacuum.
- Enable server variable log_lock_waits by default (Laurenz Albe) [§](commit_baseurl2aac62be8)
- Add server variable debug_print_raw_parse to log raw parse trees (Chao Li) [§](commit_baseurl06473f5a3) This is also enabled when the server is started with debug level three and higher.
- Make messages coming from remote servers appear in the server logs in the same format as local server messages (Vignesh C) [§](commit_baseurl112faf137) These include replication, `postgres-fdw`, and `dblink` servers.
- Add reporting of WAL full-page write bytes to VACUUM and ANALYZE logging (Shinya Kato) [§](commit_baseurlad25744f4)
- Add IO wait events for COPY FROM/TO on a pipe, file, or program (Nikolay Samokhvalov) [§](commit_baseurle05a24c2d)
- Add wait events for WAL write and flush LSNs (Xuneng Zhou) [§](commit_baseurl7a39f43d8)
- Have pg_get_sequence_data() return the sequence page LSN (Vignesh C) [§](commit_baseurlb93172ca5)
- Add function pg_get_multixact_stats() to report multixact activity (Naga Appani) [§](commit_baseurl97b101776)
- Issue warnings when the wraparound of xid and multi-xids is less than 100 million (Nathan Bossart) [§](commit_baseurl48f11bfa0) The previous warning was 40 million. Warnings are issued to clients and in the server log.

## Server Configuration

- Allow online enabling and disabling of data checksums (Daniel Gustafsson, Magnus Hagander, Tomas Vondra) [§](commit_baseurlf19c0ecca) [§](commit_baseurlb364828f8) Previously the checksum status could only be changed while the cluster was offline using pg_checksums.
- Add scoring system to control the order that tables are processed by autovacuum (Nathan Bossart) [§](commit_baseurld7965d65f) The new server variables are autovacuum_freeze_score_weight, autovacuum_multixact_freeze_score_weight, autovacuum_vacuum_score_weight, vacuum_insert_score_weight, and autovacuum_analyze_score_weight.
- Add server-side support for SNI (Server Name Indication) (Daniel Gustafsson, Jacob Champion) [§](commit_baseurl4f433025f) New configuration file PGDATA/pg_hosts.conf specifies hostname/key pairs.
- Add a new OAUTH flow hook PQAUTHDATA_OAUTH_BEARER_TOKEN_V2 (Jacob Champion) [§](commit_baseurle982331b5) [§](commit_baseurl0af4d402c) This is an improved version of PQAUTHDATA_OAUTH_BEARER_TOKEN by adding the issuer identifier and error message specification.
- Allow roles pg_read_all_data and pg_write_all_data to read/write large objects (Nitin Motiani, Nathan Bossart) [§](commit_baseurld98197602) These roles are designed to allow non-super users to run pg_dump.
- Allow background workers to be configured to terminate before database-level operations (Aya Iwata) [§](commit_baseurlf1e251be8) This allows database-level operations to complete more quickly since blocking background workers can now be terminated.
- Allow server variables that represent lists to be emptied by setting the value to `NULL` (Tom Lane) [§](commit_baseurlff4597acd)
- Update GB18030 encoding from version 2000 to 2022 (Chao Li, Zheng Tao) [§](commit_baseurl5334620ee) See the commit message for compatibility details.

## Streaming Replication and Recovery

- Add WAIT FOR command to allow standbys to wait for LSN values to be written, flushed, or replayed (Kartyshov Ivan, Alexander Korotkov, Xuneng Zhou) [§](commit_baseurl447aae13b) [§](commit_baseurl49a181b5d)
- Improve function pg_sync_replication_slots() to wait for replication synchronization completion (Ajin Cherian, Zhijie Hou) [§](commit_baseurl0d2d4a0ec) Previously, certain synchronization failures would not be reported.
- Add server variable wal_sender_shutdown_timeout to limit replica synchronization waits during shutdown (Andrey Silitskiy, Hayato Kuroda) [§](commit_baseurla8f45dee9) By default, senders still wait forever for synchronization.
- Allow wal_receiver_timeout to be set per-subscription and user (Fujii Masao) [§](commit_baseurl8a6af3ad0) [§](commit_baseurlfb80f388f) This allows subscribers to use different wal_receiver_timeout values.
- Add optional pid parameter to pg_replication_origin_session_setup() to allow parallelization of SQL-level replication solutions (Doruk Yilmaz, Hayato Kuroda) [§](commit_baseurl5b148706c)

## Logical Replication

- Allow sequence values stored in subscribers to match the publisher (Vignesh C) [§](commit_baseurlf0b3573c3) [§](commit_baseurl5509055d6) [§](commit_baseurl55cefadde) This is enabled during CREATE SUBSCRIPTION, ALTER SUBSCRIPTION ... REFRESH PUBLICATION, and ALTER SUBSCRIPTION ... REFRESH SEQUENCES. The latter only updates values, not sequence existence. Function pg_get_sequence_data() allows inspection of sequence synchronization.
- Allow CREATE/ALTER PUBLICATION to publish all sequences (Vignesh C, Tomas Vondra) [§](commit_baseurl96b378497) This is enabled with the `ALL SEQUENCES` clause.
- Allow ALTER SUBSCRIPTION on publications to synchronize the existence of sequences on subscribers to match the publisher (Vignesh C) [§](commit_baseurlf0b3573c3) This is enabled with the `REFRESH SEQUENCES` clause.
- Allow CREATE/ALTER PUBLICATION to exclude some tables (Vignesh C, Shlok Kyal) [§](commit_baseurl493f8c643) [§](commit_baseurl6b0550c45) [§](commit_baseurlfd366065e) [§](commit_baseurl5984ea868) This is controled with the `EXCEPT` clause, and is useful when specifying `ALL TABLES`.
- Add CREATE/ALTER PUBLICATION setting retain_dead_tuples to retain information needed for conflict resolution (Zhijie Hou) [§](commit_baseurl228c37086) [§](commit_baseurl0d48d393d) [§](commit_baseurla850be2fe) Also add setting max_retention_duration to limit `retain_dead_tuples` retention.
- Allow CREATE SUBSCRIPTION to use `postgres-fdw` foreign data wrapper connection parameters (Jeff Davis) [§](commit_baseurl8185bb534) The connection parameters are referenced via CREATE SUBSCRIPTION ... SERVER.
- When server variable wal_level is `replica`, allow automatic enablement of logical replication when needed (Masahiko Sawada) [§](commit_baseurl67c20979c) New server variable effective_wal_level reports the effective WAL level.

## Query Commands

- Add support for SQL Property Graph Queries (SQL/PGQ) (Peter Eisentraut, Ashutosh Bapat) [§](commit_baseurl2f094e7ac) [§](commit_baseurlc5b3253b8) [§](commit_baseurla0dd0702e) Internally these are processed like views so are written as standard relational queries.
- Add `FOR PORTION OF` clause to UPDATE and DELETE (Paul A. Jungwirth) [§](commit_baseurl8e72d914c) [§](commit_baseurlb6ccd30d8) This allows operations on temporal ranges.
- Add `GROUP BY ALL` syntax to SELECT to automatically group all non-aggregate and non-window-function target list parameters (David Christensen) [§](commit_baseurlef38a4d97)
- Allow `GROUP BY` to process target list subqueries that have expressions referencing non-subquery columns (Tom Lane) [§](commit_baseurl415100aa6) Also fix a bug in how GROUPING() handles target list subquery aliases.
- Allow window functions to ignore NULLs with the `IGNORE NULLS`/`RESPECT NULLS` clause (Oliver Ford, Tatsuo Ishii) [§](commit_baseurl25a30bbd4) Supported window functions are `lead()`, `lag()`, `first_value()`, `last_value()`, and `nth_value()`.
- Add support for INSERT ... ON CONFLICT DO SELECT ... RETURNING (Andreas Karlsson, Marko Tiikkaja, Viktor Holmberg) [§](commit_baseurl88327092f) This allows conflicting rows to be returned, and optionally locked with `FOR UPDATE`/`SHARE`.

## Utility Commands

- Add REPACK command which replaces VACUUM FULL and CLUSTER (Antonin Houska) [§](commit_baseurlac58465e0) The two former commands did similar things, but with confusing names, so unify them as REPACK. The old commands have been retained for compatibility.
- Allow REPACK to rebuild tables without access-exclusive locking (Antonin Houska, Mihail Nikalayeu, Álvaro Herrera) [§](commit_baseurl28d534e2a) [§](commit_baseurl8fb95a8ab) [§](commit_baseurle76d8c749) This is enabled via the `CONCURRENTLY` option. Server variable max_repack_replication_slots was also added.
- Allow partitions to be merged and split using ALTER TABLE ... MERGE/SPLIT PARTITIONS (Dmitry Koval, Alexander Korotkov, Tender Wang, Richard Guo, Dagfinn Ilmari Mannsåker, Fujii Masao, Jian He) [§](commit_baseurlf2e4cc427) [§](commit_baseurl4b3d17362)
- Allow GRANT/REVOKE to specify the effective role performing the privileges adjustment (Nathan Bossart, Tom Lane) [§](commit_baseurldd1398f13) The `GRANTED BY` clause controls this.
- Allow CREATE SCHEMA to create more types of objects in newly-created schemas (Kirill Reshke, Jian He, Tom Lane) [§](commit_baseurld51697484)
- Allow CHECKPOINT to accept a list of options (Christoph Berg) [§](commit_baseurla4f126516) [§](commit_baseurl2f698d7f4) [§](commit_baseurl8d33fbacb) Supported options are `MODE` and `FLUSH_UNLOGGED`.
- Add `CONNECTION` clause to CREATE FOREIGN DATA WRAPPER to specify a function to be called for subscription connection parameters (Jeff Davis, Noriyoshi Shinoda) [§](commit_baseurl8185bb534) [§](commit_baseurl90630ec42)
- Add memory usage and parallelism reporting to VACUUM (VERBOSE) and autovacuum logs (Tatsuya Kawata, Daniil Davydov) [§](commit_baseurl736f754ee) [§](commit_baseurladcdbe938)

## Constraints

- Allow ALTER TABLE ALTER CONSTRAINT ... [NOT] ENFORCED for `CHECK` constraints (Jian He) [§](commit_baseurl342051d73) Previously enforcement changes were only supported for foreign key constraints.
- Allow ALTER TABLE ... COLUMN SET EXPRESSION to succeed on virtual columns with `CHECK` constraints (Jian He) [§](commit_baseurlf80bedd52) This was previously prohibited.

## `sql-copy`

- Allow multiple headers lines to be skipped by COPY FROM (Shinya Kato, Fujii Masao) [§](commit_baseurlbc2f348e8) Previously only a single header line could be skipped.
- Allow COPY FROM to set invalid input values to `NULL` (Jian He, Kirill Reshke) [§](commit_baseurl2a525cc97) This is done using the COPY option `ON_ERROR SET_NULL`.
- Allow COPY TO to output JSON format (Joe Conway, Jian He, Andrew Dunstan) [§](commit_baseurl7dadd38cd) [§](commit_baseurl4c0390ac5) JSON output can also be a single JSON array using the COPY option `FORCE_ARRAY`.
- Allow COPY TO to process partitioned tables (Jian He, Ajin Cherian) [§](commit_baseurl4bea91f21) [§](commit_baseurl266543a62) Previously COPY (SELECT ...) had to be used to output partitioned tables. This also improves logical replication table synchronization.

## `sql-explain`

- Add EXPLAIN ANALYZE option `IO` to report asynchronous IO activity (Tomas Vondra) [§](commit_baseurl681daed93) [§](commit_baseurl3b1117d6e) [§](commit_baseurle157fe6f7)
- Add reporting of WAL full-page write bytes to EXPLAIN (ANALYZE, WAL) output (Shinya Kato) [§](commit_baseurl5ab0b6a24)
- Add Memoize cache and lookup estimates to EXPLAIN output (Ilia Evdokimov, Lukas Fittl) [§](commit_baseurl4bc62b868) This can show why Memoize was chosen.

## Data Types

- Add the 64-bit unsigned data type oid8 (Michael Paquier) [§](commit_baseurlb139bd3b6)
- Add more jsonpath string methods (Florents Tselai, David E. Wheeler) [§](commit_baseurlbd4f879a9) They are ltrim(), rtrim(), btrim(), lower(), upper(), initcap(), replace(), and split_part(). These are immutable like their non-JSON string variants.
- Allow casts between bytea and uuid data types (Dagfinn Ilmari Mannsåker, Aleksander Alekseev) [§](commit_baseurlba21f5bf8)
- Add ability to cast between database names and oid8s using regdatabase (Ian Lawrence Barwick) [§](commit_baseurlbd09f024a)
- Add functions tid_block() and tid_offset() to extract block numbers and offsets from tid values (Ayush Tiwari) [§](commit_baseurldf6949ccf)

## Functions

- Add date, timestamp, and timestamptz versions of random(min, max) (Damien Clochard, Dean Rasheed) [§](commit_baseurlfaf071b55) [§](commit_baseurl9c24111c4)
- Allow encode() and decode() to process data in `base64url` and `base32hex` formats (Andrey Borodin, Aleksander Alekseev, Florents Tselai) [§](commit_baseurl497c1170c) [§](commit_baseurle752a2ccc) [§](commit_baseurle1d917182) This format retains ordering, unlike `base32`.
- Add functions to return a set of ranges resulting from range subtraction (Paul A. Jungwirth) [§](commit_baseurl5eed8ce50) The functions are range_minus_multi() and multirange_minus_multi(). This is useful to represent range subtraction results with gaps.
- Add function error_on_null() to return the supplied parameter, or error on `NULL` input (Joel Jacobson) [§](commit_baseurl2b75c38b7)
- Allow IS JSON to work on domains defined over supported base types (Jian He) [§](commit_baseurl3b4c2b9db) The supported base types are TEXT, JSON, JSONB, and BYTEA.
- Add full text stemmers for Polish and Esperanto (Tom Lane) [§](commit_baseurl7dc95cc3b) The Dutch stemmer has also been updated. The old Dutch stemmer is available via dutch_porter.
- Add function pg_get_role_ddl() to output role creation commands (Mario Gonzalez, Bryan Green, Andrew Dunstan, Euler Taveira) [§](commit_baseurl76e514ebb)
- Add function pg_get_tablespace_ddl() to output tablespace creation commands (Nishant Sharma, Manni Wood, Andrew Dunstan, Euler Taveira) [§](commit_baseurlb99fd9fd7)
- Add function pg_get_database_ddl() to output database creation commands (Akshay Joshi, Andrew Dunstan, Euler Taveira) [§](commit_baseurla4f774cf1)
- Allow event triggers to be written using PL/Python (Euler Taveira, Dimitri Fontaine) [§](commit_baseurl53eff471c)

## Libpq

- Allow libpq connections to specify a service file via servicefile (Torsten Förtsch, Ryo Kanbayashi) [§](commit_baseurl092f3c63e)
- Add special libpq protocol version 3.9999 for version testing (Jelte Fennema-Nio) [§](commit_baseurld8d7c5dc8)
- Add libpq function PQgetThreadLock() to retrieve the current locking callback (Jacob Champion) [§](commit_baseurlb8d768583)
- Add libpq connection parameter oauth_ca_file to specify the OAUTH certificate authority file (Jonathan Gonzalez V., Jacob Champion) [§](commit_baseurl993368113) This can also be set via the PGOAUTHCAFILE environment variable. The default is to use `curl`'s built-in certificates.
- Allow custom OAUTH validators to register custom pg_hba.conf authentication options (Jacob Champion) [§](commit_baseurlb977bd308)
- Allow OAUTH validators to supply failure details (Jacob Champion) [§](commit_baseurld438a3659) This is done by setting the ValidatorModuleResult structure member error_detail.
- Allow libpq environment variable PGOAUTHDEBUG to specify particular debug options (Zsolt Parragi, Jacob Champion) [§](commit_baseurl6d00fb904) The `UNSAFE` option still generates all debugging output.

## `app-psql`

- Allow the search path to appear in the psql prompt via %S (Florents Tselai) [§](commit_baseurlb3ce55f41) This works when psql is connected to PostgreSQL 18 or later.
- Allow the hot standby status to appear in the psql prompt via %i (Jim Jones) [§](commit_baseurldddbbc253)
- Modify psql backslash commands to show comments for publications, subscriptions, and extended statistics (Fujii Masao, Jim Jones) [§](commit_baseurlaecc55866) The modified commands are \dRp+, \dRs+, and \dX+.
- Allow control over how booleans are displayed in psql (David G. Johnston) [§](commit_baseurl645cb44c5) The \pset variables are display_true and display_false.
- Add psql variable SERVICEFILE to reference the service file location (Ryo Kanbayashi) [§](commit_baseurl6b1c4d326)
- Allow psql to more accurately determine if the pagerl is needed (Erik Wienhold) [§](commit_baseurl27da1a796)
- Add or improve psql tab completion (Yamaguchi Atsuo, Yugo Nagata, Haruna Miwa, Xuneng Zhou, Dagfinn Ilmari Mannsåker, Fujii Masao, Álvaro Herrera, Jian He, Tatsuya Kawata, Ian Lawrence Barwick, Vasuki M) [§](commit_baseurl5fa7837d9) [§](commit_baseurlc6a7d3bab) [§](commit_baseurl81966c545) [§](commit_baseurla1f7f91be) [§](commit_baseurl6d2ff1de4) [§](commit_baseurl02fd47dbf) [§](commit_baseurl14ee8e640) [§](commit_baseurlff0bcb248) [§](commit_baseurl86c539c5a) [§](commit_baseurla604affad) [§](commit_baseurla4c10de92) [§](commit_baseurl28c4b8a05) [§](commit_baseurl0bf7d4ca9) [§](commit_baseurl344b572e3)

## Server Applications

- Change vacuumdb's `--analyze-only` and `--analyze-in-stages` options to analyze partitioned tables when no targets are specified (Laurenz Albe, Mircea Cadariu, Chao Li) [§](commit_baseurl6429e5b77) [§](commit_baseurl95b6ec52e) Previously it skipped partitioned tables. This now matches the behavior of ANALYZE.
- Allow vacuumdb to report its commands without running them using option `--dry-run` (Corey Huinker) [§](commit_baseurld107176d2)
- Allow pg_verifybackup to read WAL files stored in `tar` archives (Amul Sul) [§](commit_baseurlb3cf461b3) Add option `--wal-path` as an alias for the existing and deprecated `--wal-directory` option.
- Allow pg_waldump to read WAL files stored in `tar` archives (Amul Sul) [§](commit_baseurlb15c15139)
- Improve performance of pg_upgrade copying large object metadata (Nathan Bossart) [§](commit_baseurl3bcfcd815) [§](commit_baseurl158408fef) [§](commit_baseurl161a3e8b6) [§](commit_baseurlb33f75361) Various methods are used, depending on the PostgreSQL version of the old cluster.
- Allow pg_upgrade to process non-default tablespaces stored in the `PGDATA` directory (Nathan Bossart) [§](commit_baseurl412036c22) Previously such tablespaces generated an error.
- Add pgbench option `--continue-on-error` to continue after SQL errors (Rintaro Ikeda, Yugo Nagata, Fujii Masao) [§](commit_baseurl0ab208fa5)
- Improve the usability of pg_test_timing (Hannu Krosing, Tom Lane) [§](commit_baseurl0b096e379) [§](commit_baseurl9dcc76414) Report nanoseconds instead of microseconds. In addition to histogram output, output a second table that reports exact timings, with an optional cutoff set by `--cutoff`.

## pg_dump/pg_dumpall/pg_restore

- Allow pg_dump to include restorable extended statistics (Corey Huinker) [§](commit_baseurlc32fb29e9)

## pg_createsubscriber

- Allow pg_createsubscriber to ignore specified publications that already exist (Shubham Khanna) [§](commit_baseurl85ddcc2f4) Previously this generated an error.
- Change the way pg_createsubscriber stores recovery parameters (Alyona Vinter) [§](commit_baseurl639352d90) Changes are stored in optionally-included `pg_createsubscriber.conf` rather than directly in `postgresql.auto.conf`.
- Add pg_createsubscriber option `-l`/`--logdir` to redirect output to files (Gyan Sreejith, Hayato Kuroda) [§](commit_baseurl6b5b7eae3)

## Source Code

- Restore support for AIX (Aditya Kamath, Srirama Kucherlapati, Peter Eisentraut) [§](commit_baseurlecae09725) [§](commit_baseurl4a1b05caa) This uses `gcc` and only supports 64-bit builds.
- Change Solaris to use unnamed POSIX semaphores (Tom Lane) [§](commit_baseurl0123ce131) Previously it used System V semaphores.
- Require Visual Studio 2019 or later (Peter Eisentraut) [§](commit_baseurl8fd9bb1d9)
- Allow MSVC to create PL/Python using the Python Limited API (Bryan Green) [§](commit_baseurl2bc60f862)
- Allow building on AArch64 using MSVC (Niyas Sait, Greg Burd, Dave Cramer) [§](commit_baseurla516b3f00)
- Allow execution stack backtraces on Windows using `DbgHelp` (Bryan Green) [§](commit_baseurl65707ed9a)
- Change the supported C language version to C11 (Peter Eisentraut) [§](commit_baseurlf5e0186f8) [§](commit_baseurl4fbe01514) Previously C99 was used.
- Use standard C23 and C++ attributes if available (Peter Eisentraut) [§](commit_baseurl76f4b92ba)
- Use AVX2 CPU instructions for calculating page checksums (Matthew Sterrett, Andrew Kim) [§](commit_baseurl5e13b0f24)
- Use ARM Crypto Extension to Compute CRC32C (John Naylor) [§](commit_baseurlfbc57f2bc)
- Change hex_encode() and hex_decode() to use SIMD CPU instructions (Nathan Bossart, Chiranmoy Bhattacharya) [§](commit_baseurlec8719ccb)
- Require Meson version 0.57.2 or later (Peter Eisentraut) [§](commit_baseurlf039c2244)
- Add `Meson` option to build both shared and static libraries, or only shared (Peter Eisentraut) [§](commit_baseurl78727dcba)
- Update Unicode data to version 17.0.0 (Peter Eisentraut) [§](commit_baseurl57ee39795)
- Add hooks `planner_setup_hook`, `planner_shutdown_hook`, `joinrel_setup_hook`, and `join_path_setup_hook` (Robert Haas) [§](commit_baseurl94f3ad396) [§](commit_baseurl4020b370f)
- Allow extensions to replace set-returning functions in the `FROM` clause with SQL queries (Paul A. Jungwirth) [§](commit_baseurlb140c8d7a)
- Make multixid members 64-bit (Maxim Orlov) [§](commit_baseurlbd8d9c9bd)
- Change function prototypes to use `uint*` instead of `bit*` typedefs (Nathan Bossart) [§](commit_baseurlbab2f27ea)
- Allow logical decoding plugins to specify if they do not access shared catalogs (Antonin Houska) [§](commit_baseurl0d3dba38c)
- Add simplified and improved shared memory registration function ShmemRequestStruct() (Heikki Linnakangas, Ashutosh Bapat) [§](commit_baseurl283e823f9) Functions ShmemInitStruct() and ShmemInitHash() remain for backward compatibility.
- Add server variable debug_exec_backend to report how parameters are passed to new backends (Daniel Gustafsson) [§](commit_baseurlb3fe098d3)
- Add documentation section about temporal tables (Paul A. Jungwirth) [§](commit_baseurle4d8a2af0)
- Document the environment variables that control the regression tests (Michael Paquier) [§](commit_baseurl02976b0a1)
- Update documented systemd example to include a restart setting (Andrew Jackson) [§](commit_baseurlb30656ce0)

## Additional Modules

- Add `pgplanadvice` module to stabilize and control planner decisions (Robert Haas) [§](commit_baseurl5883ff30b) [§](commit_baseurl6455e55b0)
- Add extension `pgstashadvice` to allow per-query-id advice to be specified (Robert Haas, Lukas Fittl) [§](commit_baseurle8ec19aa3) [§](commit_baseurlc10edb102)
- Show sizes of FETCH queries as constants in `pgstatstatements` (Sami Imseih) [§](commit_baseurlbee23ea4d) Fetches of different sizes will now be grouped together in `pgstatstatements` output.
- Add generic and custom plan counts to `pgstatstatements` (Sami Imseih) [§](commit_baseurl3357471cf)
- Refactor `pgbuffercache` reporting of shared memory mapping (Bertrand Drouvot) [§](commit_baseurl4b203d499) New function `pg_buffercache_os_pages()` and system view `pg_buffercache_os_pages` allow reporting of shared memory mapping; the function optionally includes NUMA details. Function `pg_buffercache_numa_pages()` remains for backward compatibility.
- Add functions to `pgbuffercache` to mark buffers as dirty (Nazir Bilal Yavuz) [§](commit_baseurl9ccc049df) The functions are `pg_buffercache_mark_dirty()`, `pg_buffercache_mark_dirty_relation()`, and `pg_buffercache_mark_dirty_all()`.
- Allow pushdown of array comparisons in prepared statements to `postgres-fdw` foreign servers (Alexander Pyhalov) [§](commit_baseurl62c3b4cd9)
- Allow the retrieval of statistics from foreign data wrapper servers (Corey Huinker, Etsuro Fujita) [§](commit_baseurl28972b6fc) This is enabled for `postgres-fdw` by using the option `restore_stats`. The default is for ANALYZE to retrieve rows from the remote server to locally generate statistics.
- Allow `file-fdw` to read files or program output that uses multi-line headers (Shinya Kato) [§](commit_baseurl26cb14aea)
- Add server variable `auto_explain.log_io` to add IO reporting to auto_explain (Tomas Vondra) [§](commit_baseurl61c36a34a)
- Allow auto_explain to add extension-specific EXPLAIN options via server variable `auto_explain.log_extension_options` (Robert Haas) [§](commit_baseurle972dff6c)
- Change `btree-gin` to support all btree-supported cross-type comparisons (Tom Lane) [§](commit_baseurle2b64fcef) [§](commit_baseurlfc896821c)
- Improve performance of `bloom` indexes by using streaming reads (Xuneng Zhou) [§](commit_baseurl4c910f3bb) [§](commit_baseurld841ca2d1)
- Improve performance of `pgstattuple` by using streaming reads (Xuneng Zhou) [§](commit_baseurl213f0079b) [§](commit_baseurlae58189a4)
- Allow `fuzzystrmatch`'s `dmetaphone()` to use single-byte encodings beyond ASCII (Peter Eisentraut) [§](commit_baseurle39ece034)
- Modify oid2name `--extended` to report the relation file path (David Bidoc) [§](commit_baseurl3c5ec35de)

## Acknowledgments

The following individuals (in alphabetical order) have contributed to this release as patch authors, committers, reviewers, testers, or reporters of issues.
