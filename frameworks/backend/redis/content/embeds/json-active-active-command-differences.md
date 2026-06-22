---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/json-active-active-command-differences.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

## Command differences

Some JSON commands work differently for Active-Active databases.

### `JSON.CLEAR`

[`JSON.CLEAR`]({{< relref "commands/json.clear" >}}) resets JSON arrays and objects. It supports concurrent updates to JSON documents from different instances in an Active-Active database and allows the results to be merged.
