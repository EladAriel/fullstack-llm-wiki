---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-scram.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====

# SCRAM

Salted Challenge Response Authentication Mechanism (SCRAM) is the default authentication mechanism for MongoDB.

When a user `authenticates <authentication-auth-as-user>` themselves, MongoDB uses SCRAM to verify the supplied user credentials against the user's `name <admin.system.users.user>`, `password <admin.system.users.credentials>` and `authentication database <admin.system.users.db>`.

SCRAM is based on the IETF [RFC 5802](https://tools.ietf.org/html/rfc5802) standard that defines best practices for challenge-response authentication with passwords.

> **Important:** .. include:: /includes/security/fact-no-dual-auth-with-scram.rst

## Features

The SCRAM implementation in MongoDB provides:

- A tunable work factor (the iteration count)
- Per-user random salts
- Bi-directional authentication between server and client
### SCRAM Mechanisms

MongoDB supports the following SCRAM mechanisms:

When you create or update a SCRAM user, you can indicate:

- the SCRAM mechanism to use
- whether the server or the client digests the password
When you use `SCRAM-SHA-256`, MongoDB requires server-side password hashing, which means that the server digests the password. For more information, see :method:`db.createUser()` and :method:`db.updateUser()`.

## Driver Support

The minimum driver versions that support `SCRAM` are:

.. include:: /includes/list-table-3.0-driver-compatibility.rst

## Additional Information

.. include:: /includes/md5-and-scram-sha-1.rst

## Contents

- Authenticate Clients </tutorial/configure-scram-client-authentication>
