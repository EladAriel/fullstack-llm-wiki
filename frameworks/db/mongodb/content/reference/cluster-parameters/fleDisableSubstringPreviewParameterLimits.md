---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/cluster-parameters/fleDisableSubstringPreviewParameterLimits.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
