---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/config-settings-for-saslauthd-default-socket.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
