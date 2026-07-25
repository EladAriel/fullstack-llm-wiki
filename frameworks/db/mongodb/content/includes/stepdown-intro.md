---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/stepdown-intro.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Instructs the `primary` of the replica set to become a `secondary`. After the primary steps down, eligible secondaries hold an `election for primary <replica-set-election-internals>`.

The |command-method| does not immediately step down the primary. If no :rsconf:`electable <members[n].priority>` secondaries are up to date with the primary, the primary waits up to `secondaryCatchUpPeriodSecs` (by default 10 seconds) for a secondary to catch up. Once an electable secondary is available, the |command-method| steps down the primary.

Once stepped down, the original primary becomes a secondary and is ineligible from becoming primary again for the remainder of time specified by |stepdown-secs|.

For a detailed explanation of the |command-method| 's execution, see |behavior-ref|.

> **Note:** The |command-method| is only valid against the primary and throws an
error if run on a non-primary member.
