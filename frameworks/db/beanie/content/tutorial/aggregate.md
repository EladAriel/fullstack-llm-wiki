---
type: "Framework Learn Page"
framework: "beanie"
source_repo: "https://github.com/BeanieODM/beanie"
source_branch: "main"
source_path: "docs/tutorial/aggregate.md"
source_commit: "00c0f745ef12c4be145209d2ef69c2181d4d3a17"
source_commit_short: "00c0f745"
source_commit_date: "2026-03-29T13:57:21+02:00"
generated_at: "2026-06-21T11:21:43Z"
---

# Aggregations

You can perform aggregation queries through beanie as well. For example, to calculate the average:

```python
# With a search:
avg_price = await Product.find(
    Product.category.name == "Chocolate"
).avg(Product.price)

# Over the whole collection:
avg_price = await Product.avg(Product.price)
```

A full list of available methods can be found [here](../api-documentation/interfaces.md/#aggregatemethods).

You can also use the native PyMongo syntax by calling the `aggregate` method. 
However, as Beanie will not know what output to expect, you will have to supply a projection model yourself. 
If you do not supply a projection model, then a dictionary will be returned.

```python
class OutputItem(BaseModel):
    id: str = Field(None, alias="_id")
    total: float


result = await Product.find(
    Product.category.name == "Chocolate").aggregate(
    [{"$group": {"_id": "$category.name", "total": {"$avg": "$price"}}}],
    projection_model=OutputItem
).to_list()

```
