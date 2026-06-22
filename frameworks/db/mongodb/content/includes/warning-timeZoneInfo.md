---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/warning-timeZoneInfo.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** MongoDB uses the third-party `timelib` library to provide accurate
conversions between timezones. Due to a recent update, `timelib`
could create inaccurate time zone conversions in older versions of
MongoDB.
To explicitly link to the time zone database in versions of MongoDB
prior to 5.0, download the `time zone database
<https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip>`_.
and use the :option:`timeZoneInfo <mongod --timeZoneInfo>` parameter.
