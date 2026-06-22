---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/cluster-parameters/fleDisableSubstringPreviewParameterLimits.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# fleDisableSubstringPreviewParameterLimits

## Definition

## Syntax

To set `fleDisableSubstringPreviewParameterLimits` for your deployment, run the following command on the `admin` database:

```javascript
db.adminCommand(
   {
      setClusterParameter: {
         fleDisableSubstringPreviewParameterLimits: { shouldOverride: true }
      }
   }
)
```

To view the current value, run the following command on the `admin` database:

```javascript
db.adminCommand( { getClusterParameter: "fleDisableSubstringPreviewParameterLimits" } )
```

## Behavior

By default, MongoDB enforces soft limits for {+qe+} encrypted string fields with `substring queries <qe-substring-parameters>` enabled:

- `strMaxLength` is limited to 60 characters
- `strMaxQueryLength` is limited to 10 characters
- `strMinQueryLength` must be 2 or higher
This parameter overrides these restrictions.

> **Important:** Querying long encrypted strings strongly impacts performance. Limit
string length and query length whenever possible.
