---
type: "Framework Learn Page"
framework: "beanie"
source_repo: "https://github.com/BeanieODM/beanie"
source_branch: "main"
source_path: "docs/tutorial/cache.md"
source_commit: "00c0f745ef12c4be145209d2ef69c2181d4d3a17"
source_commit_short: "00c0f745"
source_commit_date: "2026-03-29T13:57:21+02:00"
generated_at: "2026-06-21T11:21:43Z"
---

# Cache
All query results could be locally cached.

This feature must be explicitly turned on in the `Settings` inner class.

```python
class Sample(Document):
    num: int
    name: str

    class Settings:
        use_cache = True
```

Beanie uses LRU cache with expiration time. 
You can set `capacity` (the maximum number of the cached queries) and expiration time in the `Settings` inner class.

```python
class Sample(Document):
    num: int
    name: str

    class Settings:
        use_cache = True
        cache_expiration_time = datetime.timedelta(seconds=10)
        cache_capacity = 5
```

Any query will be cached for this document class.

```python
# on the first call it will go to the database
samples = await Sample.find(num>10).to_list()

# on the second - it will use cache instead
samples = await Sample.find(num>10).to_list()

await asyncio.sleep(15)

# if the expiration time was reached it will go to the database again
samples = await Sample.find(num>10).to_list()
```