---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/cluster-parameters/changeStreamOptions.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================

# changeStreamOptions

## Definition

## Syntax

To set `changeStreamOptions` for your deployment, run the following command on the `admin` database:

```javascript
db.adminCommand( { setClusterParameter: { changeStreamOptions: <value> } } )
```

To view current values for the `changeStreamOptions` cluster parameter, run the following command on the `admin` database:

```javascript
db.adminCommand( { getClusterParameter: "changeStreamOptions" } )
```

## Parameter Fields

## Behavior

If a change stream event is removed from the oplog, then the corresponding pre- and post-images are also deleted regardless of the retention time specified with :parameter:`changeStreamOptions.preAndPostImages.expireAfterSeconds`.

## Example

The following example sets the retention time for pre- and post-images in change streams to `100` seconds:

```javascript
db.runCommand( {
   setClusterParameter: {
      changeStreamOptions: { preAndPostImages: { expireAfterSeconds: 100 } }
   }
} )
```
