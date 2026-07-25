---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-timeZoneInfo.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** MongoDB uses the third-party `timelib` library to provide accurate
conversions between timezones. Due to a recent update, `timelib`
could create inaccurate time zone conversions in older versions of
MongoDB.
To explicitly link to the time zone database in versions of MongoDB
prior to 5.0, download the `time zone database
<https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip>`_.
and use the :option:`timeZoneInfo <mongod --timeZoneInfo>` parameter.
