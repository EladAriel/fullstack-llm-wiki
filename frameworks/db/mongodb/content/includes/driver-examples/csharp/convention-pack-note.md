---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/driver-examples/csharp/convention-pack-note.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Note:** The C# classes on this page use Pascal case for their property names, but the
field names in the MongoDB collection use camel case. To account for this difference,
you can use the following code to register a `ConventionPack` when your
application starts:
.. code-block:: csharp
   var camelCaseConvention = new ConventionPack { new CamelCaseElementNameConvention() };
   ConventionRegistry.Register("CamelCase", camelCaseConvention, type => true);
