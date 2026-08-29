---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture/setresult.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.263283Z"
---
# Setresult

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
