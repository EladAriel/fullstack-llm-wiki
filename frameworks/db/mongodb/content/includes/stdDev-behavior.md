---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/stdDev-behavior.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Behavior with values in a :pipeline:`$setWindowFields` stage `window <setWindowFields-window>`:

- Ignores non-numeric values, `null` values, and missing fields in a
window.

- If the window is empty, returns `null`.
- If the window contains a `NaN` value, returns `null`.
- If the window contains `Infinity` values, returns `null`.
- If none of the previous points apply, returns a `double` value.
