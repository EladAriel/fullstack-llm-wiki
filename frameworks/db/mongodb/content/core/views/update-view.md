---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/views/update-view.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================

# Modify or Remove a View

To remove a view, use the :method:`db.collection.drop()` method on the view.

To modify a view, you can either:

- Drop and recreate the view.
- Use the :dbcommand:`collMod` command.
## Example

Consider the following view named `lowStock`:

```javascript
db.createView(
   "lowStock",
   "products",
   [ { $match: { quantity: { $lte: 20 } } } ]
)
```

### Drop and Recreate the View

The following commands modify `lowStock` by dropping and recreating the view:

```javascript
db.lowStock.drop()

db.createView(
   "lowStock",
   "products",
   [ { $match: { quantity: { $lte: 10 } } } ]
)
```

### Use the `collMod` Command

Alternatively, you can use the `collMod` command to modify the view:

```javascript
db.runCommand( {
   collMod: "lowStock",
   viewOn: "products",
   "pipeline": [ { $match: { quantity: { $lte: 10 } } } ]
} )
```
