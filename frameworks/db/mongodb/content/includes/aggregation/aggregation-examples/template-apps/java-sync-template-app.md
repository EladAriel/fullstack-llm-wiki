---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/template-apps/java-sync-template-app.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Before you begin following an aggregation tutorial, you must set up a new Java app. You can use this app to connect to a MongoDB deployment, insert sample data into MongoDB, and run the aggregation pipeline.

> **Tip:** To learn how to install the driver and connect to MongoDB,
see the :driver:`Get Started with the Java Driver guide
</java/sync/current/get-started/>`.
To learn more about performing aggregations in the Java Sync Driver, see the
:driver:`Aggregation guide </java/sync/current/aggregation/>`.

After you install the driver, create a file called `AggTutorial.java`. Paste the following code in this file to create an app template for the aggregation tutorials.

> **Important:** In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.
If you attempt to run the code without making any changes, you will
encounter a connection error.

For every tutorial, you must replace the connection string placeholder with your deployment's connection string.

> **Tip:** To learn how to locate your deployment's connection string, see the
:driver:`Create a Connection String </java/sync/current/get-started/#create-a-connection-string>`
step of the Java Sync Quick Start guide.

For example, if your connection string is `"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles the following:

```java
String uri = "mongodb+srv://mongodb-example:27017";
```
