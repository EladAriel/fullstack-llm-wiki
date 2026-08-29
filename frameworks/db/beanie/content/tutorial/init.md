---
type: "Framework Learn Page"
framework: "Beanie"
source_repo: "https://github.com/BeanieODM/beanie"
source_branch: "main"
source_path: "docs/tutorial/init.md"
source_commit: "aa290b5739b52c7f62e43e37724b63038d1e5a81"
source_commit_short: "aa290b5"
source_commit_date: "2026-08-07T10:16:44-06:00"
generated_at: "2026-08-29T09:38:56.938793Z"
---
# Init

Beanie uses Async PyMongo as an async database engine. 
To initialize previously created documents, you should provide an Async PyMongo database instance 
and a list of your document models to the `init_beanie(...)` function, as it is shown in the example:

```python
from beanie import init_beanie, Document
from pymongo import AsyncMongoClient

class Sample(Document):
    name: str

async def init():
    # Create Async PyMongo client
    client = AsyncMongoClient(
        "mongodb://user:pass@host:27017"
    )

    # Initialize beanie with the Sample document class and a database
    await init_beanie(database=client.db_name, document_models=[Sample])
```

This creates the collection (if necessary) and sets up any indexes that are defined.


`init_beanie` supports not only a list of classes as the document_models argument, 
but also strings with dot-separated paths:

```python
await init_beanie(
        database=client.db_name,
        document_models=[
            "app.models.DemoDocument",
        ],
    )
```

### Warning

`init_beanie` supports the parameter named `allow_index_dropping` that will drop indexes from your collections. 
`allow_index_dropping` is by default set to `False`. If you set this to `True`, 
ensure that you are not managing your indexes in another manner. 
If you are, these will be deleted when setting `allow_index_dropping=True`.