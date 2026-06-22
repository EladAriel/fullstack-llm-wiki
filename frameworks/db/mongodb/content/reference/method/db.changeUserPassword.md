---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.changeUserPassword.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# db.changeUserPassword() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/access-change-password.rst

## Behavior

.. include:: /includes/fact-cleartext-passwords-tls.rst

## Example

The following operation changes the password of the user named `accountUser` in the `products` database to `SOh3TbYhx8ypJPxmt1oOfL`:

> **Tip:** .. include:: /includes/extracts/4.2-changes-passwordPrompt.rst

```javascript
use products
db.changeUserPassword("accountUser", passwordPrompt())
```

When prompted in :binary:`~bin.mongosh` for the password, enter the new password.

You can also pass the new password directly to :method:`db.changeUserPassword()`:

```javascript
use products
db.changeUserPassword("accountUser", "SOh3TbYhx8ypJPxmt1oOfL")
```
