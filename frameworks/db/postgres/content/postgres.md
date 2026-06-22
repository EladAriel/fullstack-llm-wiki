---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/postgres.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

%version;

%filelist;

]>

## PostgreSQL version Documentation

The PostgreSQL Global Development Group
PostgreSQL
version
legal

intro

## Tutorial

Welcome to the PostgreSQL Tutorial. The tutorial is intended to give an introduction to PostgreSQL, relational database concepts, and the SQL language. We assume some general knowledge about how to use computers and no particular Unix or programming experience is required. This tutorial is intended to provide hands-on experience with important aspects of the PostgreSQL system. It makes no attempt to be a comprehensive treatment of the topics it covers.

After you have successfully completed this tutorial, you will want to read the `sql` section to gain a better understanding of the SQL language, or `client-interfaces` for information about developing applications with PostgreSQL. Those who provision and manage their own PostgreSQL installation should also read `admin`.

start
query
advanced

## The SQL Language

This part describes the use of the SQL language in PostgreSQL. We start with describing the general syntax of SQL, then how to create tables, how to populate the database, and how to query it. The middle part lists the available data types and functions for use in SQL commands. Lastly, we address several aspects of importance for tuning a database.

The information is arranged so that a novice user can follow it from start to end and gain a full understanding of the topics without having to refer forward too many times. The chapters are intended to be self-contained, so that advanced users can read the chapters individually as they choose. The information is presented in narrative form with topical units. Readers looking for a complete description of a particular command are encouraged to review the `reference`.

Readers should know how to connect to a PostgreSQL database and issue SQL commands. Readers that are unfamiliar with these issues are encouraged to read `tutorial` first. SQL commands are typically entered using the PostgreSQL interactive terminal `psql`, but other programs that have similar functionality can be used as well.

syntax
ddl
dml
queries
datatype
func
typeconv
indices
textsearch
mvcc
perform
∥

## Server Administration

This part covers topics that are of interest to a PostgreSQL administrator. This includes installation, configuration of the server, management of users and databases, and maintenance tasks. Anyone running PostgreSQL server, even for personal use, but especially in production, should be familiar with these topics.

The information attempts to be in the order in which a new user should read it. The chapters are self-contained and can be read individually as desired. The information is presented in a narrative form in topical units. Readers looking for a complete description of a command are encouraged to review the `reference`.

The first few chapters are written so they can be understood without prerequisite knowledge, so new users who need to set up their own server can begin their exploration. The rest of this part is about tuning and management; that material assumes that the reader is familiar with the general use of the PostgreSQL database system. Readers are encouraged review the `tutorial` and `sql` parts for additional information.

installbin
installation
runtime
config
client-auth
user-manag
manage-ag
charset
maintenance
backup
high-availability
monitoring
wal
logical-replication
jit
®ress;

## Client Interfaces

This part describes the client programming interfaces distributed with PostgreSQL. Each of these chapters can be read independently. There are many external programming interfaces for client programs that are distributed separately. They contain their own documentation (`external-projects` lists some of the more popular ones). Readers of this part should be familiar with using SQL to manipulate and query the database (see `sql`) and of course with the programming language of their choice.

libpq
lobj
ecpg
infoschema

## Server Programming

This part is about extending the server functionality with user-defined functions, data types, triggers, etc. These are advanced topics which should be approached only after all the other user documentation about PostgreSQL has been understood. Later chapters in this part describe the server-side programming languages available in the PostgreSQL distribution as well as general issues concerning server-side programming. It is essential to read at least the earlier sections of `extend` (covering functions) before diving into the material about server-side programming.

extend
trigger
event-trigger
rules

xplang
plsql
pltcl
plperl
plpython

spi
bgworker
logicaldecoding
replication-origins
archive-modules
oauth-validators

reference

## Internals

This part contains assorted information that might be of use to PostgreSQL developers.

arch-dev
catalogs
system-views
protocol
sources
nls
plhandler
fdwhandler
tablesample-method
custom-scan
geqo
tableam
indexam
wal-for-extensions
indextypes
storage
transaction
bki
planstats
backup-manifest

## Appendixes

errcodes
datetime
keywords
features
release
contrib
external-projects
sourcerepo
docguide
limits
acronyms
glossary
color
obsolete

biblio
