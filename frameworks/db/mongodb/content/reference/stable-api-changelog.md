---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/stable-api-changelog.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# Stable API Changelog

This page contains a changelog of the Stable API. The Stable API is actively being expanded to include new database commands and functionality.

The commands and operators included in the Stable API depend on the MongoDB version you are using. This page describes the MongoDB and Stable API versions when a database command or specific sub-features of a command are available.

## Database Commands

The following table describes:

- The commands included in each version of the Stable API.
- The MongoDB version in which the command was added to the Stable API.
API V1 may not support all available options for these commands. Refer to the specific command documentation for limitations specific to API V1.

.. include:: /includes/fact-stable-api-explain.rst

## Aggregation

This section describes the aggregation stages and operators included in the Stable API.

### Unsupported Aggregation Stages

The following aggregation stages are **not included** in the Stable API:

.. include:: /includes/aggregation/stable-api-unsupported-stages.rst

For more information on aggregation in the Stable API, see the `Stable API <aggregate-command-stable-api-support>` section of the `aggregate` command page.

### Supported Aggregation Operators

The following aggregation operators are included in the Stable API:
