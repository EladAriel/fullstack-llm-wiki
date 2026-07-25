---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/reference.sgml"
source_commit: "38afc3dcb25c45b744d4025029ce0a6c90b7059f"
source_commit_short: "38afc3dc"
source_commit_date: "2026-07-25T19:08:27+09:00"
generated_at: "2026-07-25T11:50:59Z"
---

## Reference

The entries in this Reference are meant to provide in reasonable length an authoritative, complete, and formal summary about their respective subjects. More information about the use of PostgreSQL, in narrative, tutorial, or example form, can be found in other parts of this book. See the cross-references listed on each reference page.

The reference entries are also available as traditional man pages.

## SQL Commands

This part contains reference information for the SQL commands supported by PostgreSQL. By SQL the language in general is meant; information about the standards conformance and compatibility of each command can be found on the respective reference page.

abort
alterAggregate
alterCollation
alterConversion
alterDatabase
alterDefaultPrivileges
alterDomain
alterEventTrigger
alterExtension
alterForeignDataWrapper
alterForeignTable
alterFunction
alterGroup
alterIndex
alterLanguage
alterLargeObject
alterMaterializedView
alterOperator
alterOperatorClass
alterOperatorFamily
alterPolicy
alterProcedure
alterPropertyGraph
alterPublication
alterRole
alterRoutine
alterRule
alterSchema
alterSequence
alterServer
alterStatistics
alterSubscription
alterSystem
alterTable
alterTableSpace
alterTSConfig
alterTSDictionary
alterTSParser
alterTSTemplate
alterTrigger
alterType
alterUser
alterUserMapping
alterView
analyze
begin
call
checkpoint
close
cluster
commentOn
commit
commitPrepared
©Table;
createAccessMethod
createAggregate
createCast
createCollation
createConversion
createDatabase
createDomain
createEventTrigger
createExtension
createForeignDataWrapper
createForeignTable
createFunction
createGroup
createIndex
createLanguage
createMaterializedView
createOperator
createOperatorClass
createOperatorFamily
createPolicy
createProcedure
createPropertyGraph
createPublication
createRole
createRule
createSchema
createSequence
createServer
createStatistics
createSubscription
createTable
createTableAs
createTableSpace
createTSConfig
createTSDictionary
createTSParser
createTSTemplate
createTransform
createTrigger
createType
createUser
createUserMapping
createView
deallocate
declare
delete
discard
do
dropAccessMethod
dropAggregate
dropCast
dropCollation
dropConversion
dropDatabase
dropDomain
dropEventTrigger
dropExtension
dropForeignDataWrapper
dropForeignTable
dropFunction
dropGroup
dropIndex
dropLanguage
dropMaterializedView
dropOperator
dropOperatorClass
dropOperatorFamily
dropOwned
dropPolicy
dropProcedure
dropPropertyGraph
dropPublication
dropRole
dropRoutine
dropRule
dropSchema
dropSequence
dropServer
dropStatistics
dropSubscription
dropTable
dropTableSpace
dropTSConfig
dropTSDictionary
dropTSParser
dropTSTemplate
dropTransform
dropTrigger
dropType
dropUser
dropUserMapping
dropView
end
execute
explain
fetch
grant
importForeignSchema
insert
listen
load
lock
merge
move
¬ify;
prepare
prepareTransaction
reassignOwned
refreshMaterializedView
reindex
releaseSavepoint
repack
reset
revoke
rollback
rollbackPrepared
rollbackTo
savepoint
securityLabel
select
selectInto
set
setConstraints
setRole
setSessionAuth
setTransaction
show
startTransaction
truncate
unlisten
update
vacuum
values
waitFor

## PostgreSQL Client Applications

This part contains reference information for PostgreSQL client applications and utilities. Not all of these commands are of general utility; some might require special privileges. The common feature of these applications is that they can be run on any host, independent of where the database server resides.

When specified on the command line, user and database names have their case preserved -- the presence of spaces or special characters might require quoting. Table names and other identifiers do not have their case preserved, except where documented, and might require quoting.

clusterdb
createdb
createuser
dropdb
dropuser
ecpgRef
pgamcheck
pgBasebackup
pgbench
pgCombinebackup
pgConfig
pgDump
pgDumpall
pgIsready
pgReceivewal
pgRecvlogical
pgRestore
pgVerifyBackup
psqlRef
reindexdb
vacuumdb

## PostgreSQL Server Applications

This part contains reference information for PostgreSQL server applications and support utilities. These commands can only be run usefully on the host where the database server resides. Other utility programs are listed in `reference-client`.

initdb
pgarchivecleanup
pgChecksums
pgControldata
pgCreateSubscriber
pgCtl
pgResetwal
pgRewind
pgtestfsync
pgtesttiming
pgupgrade
pgwaldump
pgwalsummary
PostgreSQL
