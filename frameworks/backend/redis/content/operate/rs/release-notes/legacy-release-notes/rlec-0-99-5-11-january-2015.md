---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/release-notes/legacy-release-notes/rlec-0-99-5-11-january-2015.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.542965Z"
---
# Rlec 0 99 5 11 January 2015

---
Title: RLEC 0.99.5-11 Release Notes (January 5, 2015)
alwaysopen: false
categories:
- docs
- operate
- rs
description: null
linkTitle: 0.99.5-11 (January 5, 2015)
weight: null
---
### New features

Initial release, everything is new!

### Changes

Initial release, no changes!

### Fixed issues

None.

### Known issues

- **Issue:** When taking a node offline or removing a node, if the
    node being taken offline or removed is currently serving as the web
    server for the web browser being used to view the management UI, the
    management UI appears down while the node is down.
    **Workaround:** If you are using the cluster name in order to
    connect to the management UI in the browser, and the cluster name is
    registered in your external DNS or you are using the mDNS option,
    then the DNS entries will be updated to point to another node in the
    cluster after a few seconds and the UI will open properly. If you
    are not using the cluster name but rather the node IP in order to
    connect to the management UI in the web browser, you have to use the
    IP of another node in the cluster to access the management UI.
