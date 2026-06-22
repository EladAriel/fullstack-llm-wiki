---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/config-settings-for-saslauthd-default-socket.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Or if using a `YAML format configuration file </reference/configuration-options>`, specify the following settings in the file:

```yaml
security:
   authorization: enabled

setParameter:
   saslauthdPath: ""
   authenticationMechanisms: PLAIN
```

Or, if using the :v2.4:`older configuration file format </reference/configuration-options>`:

```ini
auth=true
setParameter=saslauthdPath=""
setParameter=authenticationMechanisms=PLAIN
```
