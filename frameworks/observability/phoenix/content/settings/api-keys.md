---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/settings/api-keys.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.832881Z"
---
# Api Keys

---
title: "API Keys"
---
Phoenix offers three types of authentication credentials: **System API Keys, User API Keys, and the Admin Secret**

## System API Keys

System keys authenticate actions on behalf of the entire system rather than a specific user. These keys:

* Can only be created by administrators

* Are not tied to the admin who created them

* Persist even if the creating admin is deleted

* Are recommended for automated/programmatic interactions with Phoenix that don't involve user actions (such as querying REST APIs)

## User API Keys

User API keys authenticate actions on behalf of specific users. These keys:

* Are associated with and act on behalf of the user who created them

* Can be viewed and deleted by the user who owns them

* Are automatically deleted if the user account is deleted

* Are ideal for personal use cases (e.g., running experiments in a notebook)

## Admin Secret

The Admin Secret is a special authentication token that:

* Can be used as an alternative to API keys

* Authenticates as the first system user

* Must meet these requirements:

  * At least 32 characters long

  * Includes at least one digit and one lowercase letter

  * Must differ from `PHOENIX_SECRET`

  * Cannot be set if `PHOENIX_SECRET` is not configured

This key is particularly useful for:

* Provisioning Phoenix via REST APIs

* Deploying Phoenix as a sidecar application

* Programmatically generating authentication to send traces, datasets, etc. without requiring login

This secret is set via the `PHOENIX_ADMIN_SECRET` environment variable.

<Danger>
We recommend removing this value from your deployment once you have created a system key.

</Danger>

## Key Expiration

Both System and User API keys support expiration dates. Setting expirations can:

* Limit access to specific tasks or timeframes

* Support security through automated key rotation

* Reduce the risk of compromised credentials


