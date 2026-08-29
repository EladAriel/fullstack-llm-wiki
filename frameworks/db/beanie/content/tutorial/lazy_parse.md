---
type: "Framework Learn Page"
framework: "Beanie"
source_repo: "https://github.com/BeanieODM/beanie"
source_branch: "main"
source_path: "docs/tutorial/lazy_parse.md"
source_commit: "aa290b5739b52c7f62e43e37724b63038d1e5a81"
source_commit_short: "aa290b5"
source_commit_date: "2026-08-07T10:16:44-06:00"
generated_at: "2026-08-29T09:38:56.939822Z"
---
# Lazy_Parse

## Using Lazy Parsing in Queries
Lazy parsing allows you to skip the parsing and validation process for documents and instead call it on demand for each field separately. This can be useful for optimizing performance in certain scenarios.

To use lazy parsing in your queries, you can pass the `lazy_parse=True` parameter to your find method.

Here's an example of how to use lazy parsing in a find query:

```python
await Sample.find(Sample.number == 10, lazy_parse=True).to_list()
```

By setting lazy_parse=True, the parsing and validation process will be skipped and be called on demand when the respective fields will be used. This can potentially improve the performance of your query by reducing the amount of processing required upfront. However, keep in mind that using lazy parsing may also introduce some additional overhead when accessing the fields later on.