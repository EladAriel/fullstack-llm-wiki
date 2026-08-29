---
type: "Framework Learn Page"
framework: "Beanie"
source_repo: "https://github.com/BeanieODM/beanie"
source_branch: "main"
source_path: "docs/tutorial/delete.md"
source_commit: "aa290b5739b52c7f62e43e37724b63038d1e5a81"
source_commit_short: "aa290b5"
source_commit_date: "2026-08-07T10:16:44-06:00"
generated_at: "2026-08-29T09:38:56.940662Z"
---
# Delete documents

Beanie supports single and batch deletions:

## Single

```python

await Product.find_one(Product.name == "Milka").delete()

# Or
bar = await Product.find_one(Product.name == "Milka")
await bar.delete()
```

## Many

```python

await Product.find(Product.category.name == "Chocolate").delete()
```

## All

```python

await Product.delete_all()
# Or
await Product.all().delete()

```