---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/example-progress-monitor.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To set the `interval` to 1000 milliseconds and the `deadline` to 300 seconds, issue the following at startup:

```bash
mongos --setParameter 'progressMonitor={"interval": 1000, "deadline": 300}'
```

Or if using the :dbcommand:`setParameter` command in a :binary:`~bin.mongosh` session that is connected to a running :binary:`~bin.mongos`:

```javascript
db.adminCommand( 
 {
     setParameter: 1, 
     progressMonitor: { interval: 1000, deadline: 300 } )
 }
)
```

Parameters set with :dbcommand:`setParameter` do not persist across restarts. See the `setParameter page <setParameter-commands-not-persistent>` for details.

To make this setting persistent, set `progressMonitor` in your `mongos config file <configuration-options>` using the :setting:`setParameter` option as in the following example:

```yaml
setParameter:
  progressMonitor: "{ interval: 1000, deadline: 300 }"
```
