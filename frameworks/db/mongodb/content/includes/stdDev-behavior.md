---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/stdDev-behavior.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Behavior with values in a :pipeline:`$setWindowFields` stage `window <setWindowFields-window>`:

- Ignores non-numeric values, `null` values, and missing fields in a
window.

- If the window is empty, returns `null`.
- If the window contains a `NaN` value, returns `null`.
- If the window contains `Infinity` values, returns `null`.
- If none of the previous points apply, returns a `double` value.
