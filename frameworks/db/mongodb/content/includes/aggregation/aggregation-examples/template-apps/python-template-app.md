---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/template-apps/python-template-app.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Before you begin following this aggregation tutorial, you must set up a new Python app. You can use this app to connect to a MongoDB deployment, insert sample data into MongoDB, and run the aggregation pipeline.

> **Tip:** To learn how to install PyMongo and connect to MongoDB,
see the `Get Started with PyMongo
<https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/>`__
tutorial.
To learn more about performing aggregations in PyMongo, see the
`Aggregation guide
<https://www.mongodb.com/docs/languages/python/pymongo-driver/current/aggregation/>`__.

After you install the library, create a file called `agg_tutorial.py`. Paste the following code in this file to create an app template for the aggregation tutorials.

> **Important:** In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.
If you attempt to run the code without making any changes, you will
encounter a connection error.

For every tutorial, you must replace the connection string placeholder with your deployment's connection string.

> **Tip:** To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/php-library/current/get-started/#create-a-connection-string)_
step of the Get Started with the PHP Library tutorial.

For example, if your connection string is `"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles the following:

```php
uri = "mongodb+srv://mongodb-example:27017"
```
