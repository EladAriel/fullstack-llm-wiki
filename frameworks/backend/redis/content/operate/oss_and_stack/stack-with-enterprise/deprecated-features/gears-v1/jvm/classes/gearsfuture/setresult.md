---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture/setresult.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: SetResult
alwaysopen: false
categories:
- docs
- operate
- stack
description: Sets a computation to run asynchronously.
linkTitle: setResult
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsfuture/setresult/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public void setResult​(I result) 
	throws java.lang.Exception
```

Sets a computation to run asynchronously.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| result | template type I | The result of a computation |

## Returns

None

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).map(r->r.getKey()).
	asyncFilter(r->{
		GearsFuture<Boolean> f = new GearsFuture<Boolean>();
		try {
			f.setResult(r.equals("x"));	
		} catch (Exception e) {
			e.printStackTrace();
		}			
		return f;
});
```
