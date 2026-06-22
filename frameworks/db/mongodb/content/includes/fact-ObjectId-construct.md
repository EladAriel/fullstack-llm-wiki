---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-ObjectId-construct.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- A 4-byte timestamp, representing the ObjectId's creation, measured in seconds since the
Unix epoch.

- A 5-byte random value generated once per client-side process. This random value is unique to the
machine and process. If the process restarts or the primary node of the process changes, this value is re-generated.

- A 3-byte incrementing counter per client-side process, initialized to a random value.
The counter resets when a process restarts.

For timestamp and counter values, the most significant bytes appear first in the byte sequence (big-endian). This is unlike other BSON values, where the least significant bytes appear first (little-endian).

If an integer value is used to create an ObjectId, the integer replaces the timestamp.
