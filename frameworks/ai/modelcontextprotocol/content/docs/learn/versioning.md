---
type: "Framework Learn Page"
framework: "Model Context Protocol"
source_repo: "https://github.com/modelcontextprotocol/modelcontextprotocol"
source_branch: "main"
source_path: "docs/docs/learn/versioning.mdx"
source_commit: "47501e4ced7823014b83be168916d4c9e63b594e"
source_commit_short: "47501e4c"
source_commit_date: "2026-06-22T09:16:44-07:00"
generated_at: "2026-06-23T14:04:43Z"
---

---
title: Versioning
type: docs
weight: 10
---

The Model Context Protocol uses string-based version identifiers following the format
`YYYY-MM-DD`, to indicate the last date backwards incompatible changes were made.

<Info>

The protocol version will _not_ be incremented when the
protocol is updated, as long as the changes maintain backwards compatibility. This allows
for incremental improvements while preserving interoperability.

</Info>

## Revisions

Revisions may be marked as:

- **Draft**: in-progress specifications, not yet ready for consumption.
- **Current**: the current protocol version, which is ready for use and may continue to
  receive backwards compatible changes.
- **Final**: past, complete specifications that will not be changed.

The **current** protocol version is [**2025-11-25**](/specification/2025-11-25/).

## Feature States

Individual features of the specification may additionally be marked as
**Deprecated** under the
[feature lifecycle and deprecation policy](/community/feature-lifecycle):
the feature remains part of the specification, but is scheduled for removal.
Deprecated features document a migration path (or state that none is required)
and remain in the specification for at least twelve months, or at least
ninety days under the policy's
[expedited-removal exception](/community/feature-lifecycle#expedited-removal),
before they become eligible for removal, after which they may be **Removed**
in a future revision.

Features that are currently Deprecated are listed in the
[deprecated features registry](/specification/draft/deprecated).

## Negotiation

Version negotiation happens during
[initialization](/specification/latest/basic/lifecycle#initialization). Clients and
servers **MAY** support multiple protocol versions simultaneously, but they **MUST**
agree on a single version to use for the session.

The protocol provides appropriate error handling if version negotiation fails, allowing
clients to gracefully terminate connections when they cannot find a version compatible
with the server.
