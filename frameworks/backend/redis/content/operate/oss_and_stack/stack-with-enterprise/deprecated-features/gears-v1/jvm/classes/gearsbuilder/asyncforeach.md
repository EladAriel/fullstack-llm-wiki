---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/asyncforeach.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.268424Z"
---
# Asyncforeach

---
Title: AsyncForeach
alwaysopen: false
categories:
- docs
- operate
- stack
description: For each record in the pipe, asynchronously runs some operations.
linkTitle: asyncForeach
weight: 50
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/classes/gearsbuilder/asyncforeach/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

```java
public GearsBuilder<T> asyncForeach​(
    gears.operations.AsyncForeachOperation<T> foreach)
```

The `asyncForeach` function allows you to use a [`GearsFuture`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture" >}}) object to define a set of operations and run them asynchronously for each record in the pipe.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| foreach | AsyncForeachOperation<T> | The set of operations to run for each record |

## Returns

Returns a GearsBuilder object with a new template type.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).map(r->r.getKey()).
	asyncForeach(r->{
		GearsFuture<Serializable> f = new GearsFuture<Serializable>();
		new Thread(new Runnable() {
				
			@Override
			public void run() {
				try {
					Thread.sleep(1);
						
					f.setResult(r);
				} catch (Exception e) {
					e.printStackTrace();
				}					
			}
		}).start();
		return f;
});
```