---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/register.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Register
alwaysopen: false
categories:
- docs
- operate
- stack
description: Registers the pipeline of functions to run when certain events occur.
linkTitle: register
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/register/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public java.lang.String register()

public java.lang.String register​(ExecutionMode mode)

public java.lang.String register​(
    ExecutionMode mode, 
    gears.operations.OnRegisteredOperation onRegister, 
    gears.operations.OnUnregisteredOperation onUnregistered)
```

Registers the pipeline of functions to run when certain [events]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/register-events" >}}) occur. The registered functions will run each time the event occurs.

Execution modes:

| Name | Description |
|------|-------------|
| ASYNC | Runs asynchronously on all of the shards. |
| ASYNC_LOCAL | Runs asynchronously but only on the current shard that generated the event. |
| SYNC | Runs synchronously only on the same shard that generated the event. |

{{<note>}}
If you call `register()` without specifying an execution mode, it will default to `ASYNC`. 
{{</note>}}

## Parameters

| Name | Type | Description |
|------|------|-------------|
| mode | ExecutionMode | The execution mode to use (ASYNC/ASYNC_LOCAL/SYNC) |
| onRegister | OnRegisteredOperation | Register callback that will be called on each shard upon register |
| onUnregistered | OnUnregisteredOperation | Unregister callback that will be called on each shard upon unregister |

## Returns

Returns a registration ID.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).register();
```