---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/localaccumulateby.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: LocalAccumulateBy
alwaysopen: false
categories:
- docs
- operate
- stack
description: Groups records and reduces each group to a single record per group locally
  on each shard.
linkTitle: localAccumulateBy
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/localaccumulateby/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public <I extends java.io.Serializable> GearsBuilder<I> localAccumulateBy​(
	gears.operations.ExtractorOperation<T> extractor, 
	gears.operations.AccumulateByOperation<T,​I> accumulator)
```

The `localAccumulateBy` function is similar to [`accumulateBy`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/accumulateby" >}}), except it performs the operation locally on each shard without moving data between shards.

On each shard, it iterates through the records in the pipe, groups them based on the provided extractor, and then reduces each group to a single record per group with the accumulator function.

The initial value of the accumulator is null.

## Parameters
 
Type parameters:

| Name | Description |
|------|-------------|
| I | The template type of the returned builder |

Function parameters:

| Name | Type | Description |
|------|------|-------------|
| accumulator | <nobr>AccumulateByOperation<T,​I></nobr> | A function with logic to update the accumulator value with each record |
| extractor | ExtractorOperation<T> | Extracts a specific value from each record |

## Returns

Returns a GearsBuilder object with a new template type.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).
   	localAccumulateBy(r->{
   		return r.getStringVal();
   	},(k, a, r)->{
   		Integer ret = null;
   		if(a == null) {
   			ret = 0;
   		}else {
   			ret = (Integer)a;
   		}
   		return ret + 1;
});
```
