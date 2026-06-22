---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/change-own-password-and-custom-data.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# Change Your Password and Custom Data

## Overview

Users with appropriate privileges can change their own passwords and custom data. `Custom data <admin.system.users.customData>` stores optional user information.

## Considerations

To generate a strong password for use in this procedure, you can use the `openssl` utility's `rand` command. For example, issue `openssl rand` with the following options to create a base64-encoded string of 48 pseudo-random bytes:

```bash
openssl rand -base64 48
```

## Prerequisites

.. include:: /includes/access-change-own-password-and-custom-data.rst

.. include:: /includes/steps/change-own-password-and-custom-data-prereq.rst

## Procedure

.. include:: /includes/steps/change-own-password-and-custom-data.rst
