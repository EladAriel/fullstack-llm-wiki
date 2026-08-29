---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/json-active-active-command-differences.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.096060Z"
---
# Json Active Active Command Differences

## Command differences

Some JSON commands work differently for Active-Active databases.

### `JSON.CLEAR`

[`JSON.CLEAR`]({{< relref "commands/json.clear" >}}) resets JSON arrays and objects. It supports concurrent updates to JSON documents from different instances in an Active-Active database and allows the results to be merged.
