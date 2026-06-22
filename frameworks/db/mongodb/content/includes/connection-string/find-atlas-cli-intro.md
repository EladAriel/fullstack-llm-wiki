---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/connection-string/find-atlas-cli-intro.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To find your {+atlas+} connection string using the :atlascli:`Atlas CLI </>`, :atlascli:`install </install-atlas-cli/>` and :atlascli:`connect </connect-atlas-cli/>` from the Atlas CLI, then run the following command. Replace `<clusterName>` with the name of the {+atlas+} cluster and replace `<projectId>` with the project ID.

```
atlas clusters connectionStrings describe <clusterName> --projectId
<projectId>
```

To learn more, see :atlascli:`atlas clusters connectionStrings describe </command/atlas-clusters-connectionStrings-describe/>`.
