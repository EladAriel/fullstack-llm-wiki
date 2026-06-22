---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/atlas-search-commands/command-output/examples/single-doc-default-example-output.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

```javascript
[
  {
    id: '6524096020da840844a4c4a7',
    name: 'default',
    status: 'BUILDING',
    queryable: true,
    latestDefinitionVersion: {
      version: 2,
      createdAt: ISODate("2023-10-09T14:51:57.355Z")
    },
    latestDefinition: {
      mappings: { dynamic: true },
      storedSource: { include: [ 'awards.text' ] }
    },
    statusDetail: [
      {
        hostname: 'atlas-n1cm1j-shard-00-02',
        status: 'BUILDING',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:08:32.000Z")
          },
          definition: { mappings: { dynamic: true, fields: {} } }
        },
        stagedIndex: {
          status: 'PENDING',
          queryable: false,
          definitionVersion: {
            version: 1,
            createdAt: ISODate("2023-10-09T14:51:29.000Z")
          },
          definition: {
            mappings: { dynamic: true, fields: {} },
            storedSource: true
          }
        }
      },
      {
        hostname: 'atlas-n1cm1j-shard-00-01',
        status: 'BUILDING',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:08:32.000Z")
          },
          definition: { mappings: { dynamic: true, fields: {} } }
        },
        stagedIndex: {
          status: 'PENDING',
          queryable: false,
          definitionVersion: {
            version: 1,
            createdAt: ISODate("2023-10-09T14:51:29.000Z")
          },
          definition: {
            mappings: { dynamic: true, fields: {} },
            storedSource: true
          }
        }
      },
      {
        hostname: 'atlas-n1cm1j-shard-00-00',
        status: 'BUILDING',
        queryable: true,
        mainIndex: {
          status: 'READY',
          queryable: true,
          definitionVersion: {
            version: 0,
            createdAt: ISODate("2023-10-09T14:08:32.000Z")
          },
          definition: { mappings: { dynamic: true, fields: {} } }
        }
      }
    ]
  }
]
```
