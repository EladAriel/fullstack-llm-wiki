---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/driver-examples/csharp/convention-pack-note.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Note:** The C# classes on this page use Pascal case for their property names, but the
field names in the MongoDB collection use camel case. To account for this difference,
you can use the following code to register a `ConventionPack` when your
application starts:
.. code-block:: csharp
   var camelCaseConvention = new ConventionPack { new CamelCaseElementNameConvention() };
   ConventionRegistry.Register("CamelCase", camelCaseConvention, type => true);
