---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/release-notes/drivers-write-concern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:orphan:

============================

# Default Write Concern Change

These release notes outline a change to all driver interfaces released in November 2012. See release notes for specific drivers for additional information.

## Changes

As of the releases listed below, there are two major changes to all drivers:

#. All drivers will add a new top-level connection class that will increase consistency for all MongoDB client interfaces.

This change is non-backward breaking: existing connection classes will remain in all drivers for a time, and will continue to operate as expected. However, those previous connection classes are now deprecated as of these releases, and will eventually be removed from the driver interfaces.

The new top-level connection class is named `MongoClient`, or similar depending on how host languages handle namespacing.

#. The default write concern on the new `MongoClient` class will be to acknowledge all write operations [#without-arguments]_. This will allow your application to receive acknowledgment of all write operations.

See the documentation of `Write Concern <write-concern>` for more information about write concern in MongoDB.

Please migrate to the new `MongoClient` class expeditiously.

arguments, which is logically equivalent to the `w: 1` option.

However, this operation allows `replica set` users to override the default write concern with the :rsconf:`settings.getLastErrorDefaults` setting in the `/reference/replica-configuration`.

`getLastError` is removed starting in MongoDB 5.1. See `wc-specs` for alternatives.

## Releases

The following driver releases will include the changes outlined in `write-concern-change-notes`. See each driver's release notes for a full account of each release as well as other related driver-specific changes.

- C#, version 1.7
- Java, version 2.10.0
- Node.js, version 1.2
- Perl, version 0.501.1
- Legacy PHP, version 1.4
- Python, version 2.4
- Ruby, version 1.8
