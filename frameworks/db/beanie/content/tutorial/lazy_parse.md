---
type: "Framework Learn Page"
framework: "beanie"
source_repo: "https://github.com/BeanieODM/beanie"
source_branch: "main"
source_path: "docs/tutorial/lazy_parse.md"
source_commit: "00c0f745ef12c4be145209d2ef69c2181d4d3a17"
source_commit_short: "00c0f745"
source_commit_date: "2026-03-29T13:57:21+02:00"
generated_at: "2026-06-21T11:21:43Z"
---

## Using Lazy Parsing in Queries
Lazy parsing allows you to skip the parsing and validation process for documents and instead call it on demand for each field separately. This can be useful for optimizing performance in certain scenarios.

To use lazy parsing in your queries, you can pass the `lazy_parse=True` parameter to your find method.

Here's an example of how to use lazy parsing in a find query:

```python
await Sample.find(Sample.number == 10, lazy_parse=True).to_list()
```

By setting lazy_parse=True, the parsing and validation process will be skipped and be called on demand when the respective fields will be used. This can potentially improve the performance of your query by reducing the amount of processing required upfront. However, keep in mind that using lazy parsing may also introduce some additional overhead when accessing the fields later on.