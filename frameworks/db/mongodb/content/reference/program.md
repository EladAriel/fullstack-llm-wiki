---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/program.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==========================

# MongoDB Package Components

## Core Processes

The core components in the MongoDB package are:

## Contents

- mongod </reference/program/mongod>
- mongos </reference/program/mongos>

## Windows Services

The :binary:`mongod.exe` and :binary:`mongos.exe` binaries configure MongoDB as a Windows Service. They provide a superset of the :binary:`~bin.mongod` and :binary:`~bin.mongos` options.

- `/reference/program/mongod.exe`
- `/reference/program/mongos.exe`
## Contents

- mongod.exe </reference/program/mongod.exe>
- mongos.exe </reference/program/mongos.exe>

## Security Tools

:binary:`~bin.mongoldap` validates a system's LDAP configuration, and :binary:`~bin.mongokerberos` validates a system's Kerberos configuration. Both tools test that authentication succeeds for a specified username.

## Contents

- mongokerberos </reference/program/mongokerberos>
- mongoldap </reference/program/mongoldap>

## MongoDB Compass

MongoDB is packaged with an `install_compass` script, which is a platform-specific installer for `MongoDB Compass Community Edition <compass-index>`.

## Contents

- install_compass </reference/program/install_compass>

## Contents

- Database Tools <https://www.mongodb.com/docs/database-tools/>
