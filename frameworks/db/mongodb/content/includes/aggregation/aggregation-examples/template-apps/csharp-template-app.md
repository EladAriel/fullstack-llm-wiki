---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/template-apps/csharp-template-app.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Before you begin following this aggregation tutorial, you must set up a new C#/.NET app. You can use this app to connect to a MongoDB deployment, insert sample data into MongoDB, and run the aggregation pipeline.

> **Tip:** To learn how to install the driver and connect to MongoDB,
see the :driver:`C#/.NET Driver Quick Start guide </csharp/current/quick-start/>`.
To learn more about performing aggregations in the C#/.NET Driver, see the
:driver:`Aggregation guide </csharp/current/fundamentals/aggregation/>`.

After you install the driver, paste the following code into your `Program.cs` file to create an app template for the aggregation tutorials.

> **Important:** In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.
If you attempt to run the code without making any changes, you will
encounter a connection error.

For every tutorial, you must replace the connection string placeholder with your deployment's connection string.

> **Tip:** To learn how to locate your deployment's connection string, see the
:driver:`Set Up a Free Tier Cluster in Atlas </csharp/current/quick-start/#set-up-a-free-tier-cluster-in-atlas>`
step of the C# Quick Start guide.

For example, if your connection string is `"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles the following:

```csharp
var uri = "mongodb+srv://mongodb-example:27017";
```
