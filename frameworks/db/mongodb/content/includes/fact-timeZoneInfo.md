---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-timeZoneInfo.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The full path from which to load the time zone database. If this option is not provided, then MongoDB uses its built-in time zone database.

The configuration file included with Linux and macOS packages sets the time zone database path to `/usr/share/zoneinfo` by default.

The built-in time zone database is a copy of the [Olson/IANA time zone database](https://www.iana.org/time-zones). It is updated along with MongoDB releases, but the time zone database release cycle differs from the MongoDB release cycle. The most recent release of the time zone database is available on our [download site](https://downloads.mongodb.org/olson_tz_db/timezonedb-latest.zip).
