---
type: "Framework Learn Page"
framework: "beanie"
source_repo: "https://github.com/BeanieODM/beanie"
source_branch: "main"
source_path: "docs/tutorial/delete.md"
source_commit: "00c0f745ef12c4be145209d2ef69c2181d4d3a17"
source_commit_short: "00c0f745"
source_commit_date: "2026-03-29T13:57:21+02:00"
generated_at: "2026-06-21T11:21:43Z"
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