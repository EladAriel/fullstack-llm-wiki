---
type: "Framework Learn Page"
framework: "Beanie"
source_repo: "https://github.com/BeanieODM/beanie"
source_branch: "main"
source_path: "docs/tutorial/revision.md"
source_commit: "aa290b5739b52c7f62e43e37724b63038d1e5a81"
source_commit_short: "aa290b5"
source_commit_date: "2026-08-07T10:16:44-06:00"
generated_at: "2026-08-29T09:38:56.939959Z"
---
# Revision

This feature helps with concurrent operations. 
It stores `revision_id` together with the document and changes it on each document update. 
If the application with an older local copy of the document tries to change it, an exception will be raised. 
Only when the local copy is synced with the database, the application will be allowed to change the data. 
This helps to avoid data losses.

### Be aware
revision id feature may work incorrectly with BulkWriter.

### Usage

This feature must be explicitly turned on in the `Settings` inner class:

```python
class Sample(Document):
    num: int
    name: str

    class Settings:
        use_revision = True
```

Any changing operation will check if the local copy of the document has the up-to-date `revision_id` value:

```python
s = await Sample.find_one(Sample.name="TestName")
s.num = 10

# If a concurrent process already changed the doc, the next operation will raise an error
await s.replace()
```

If you want to ignore revision and apply all the changes even if the local copy is outdated, 
you can use the `ignore_revision` parameter:

```python
await s.replace(ignore_revision=True)
```
