---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/server-sessions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Server Sessions

## Overview

MongoDB's server sessions, or logical sessions, are the underlying framework used by client sessions to support `causal-consistency` and `retryable writes <retryable-writes>`.

> **Important:** Applications use client sessions to interface with server sessions.

Server sessions are available for replica sets and sharded clusters only.

## Command Options

.. include:: /includes/extracts/sessions-options.rst

## Sessions Commands

.. include:: /includes/extracts/sessions-commands.rst

## Sessions and Access Control

If the deployment enforces authentication/authorization, the user must be authenticated to start a session, and only that user can use the session.

.. include:: /includes/extracts/sessions-external-username-limit.rst

If the deployment does not enforce authentication/authorization, a created session has no owner and can be used by any user on any connection. If a user authenticates and creates a session for a deployment that does not enforce authentication/authorization, that user owns the session. However, any user on any connection may use the session.

If the deployment transitions to authentication without any downtime, any sessions without an owner cannot be used.

> **Seealso:** :parameter:`maxSessions`
