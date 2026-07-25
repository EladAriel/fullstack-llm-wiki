---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/connection-string/atlas-aws-iam-example.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The following example connects to an Atlas cluster that has been configured to support authentication via [AWS IAM credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)_:

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```

Connecting to Atlas using AWS IAM credentials in this manner uses the `MONGODB-AWS` :urioption:`authentication mechanism <authMechanism>` and the `$external` :urioption:`authSource`.

If you use an [AWS session token](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html)_, specify an `AWS_SESSION_TOKEN` in the :urioption:`authMechanismProperties` value, as shown in the following example:

```bash
mongodb+srv://<aws access key id>:<aws secret access key>@cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS&authMechanismProperties=AWS_SESSION_TOKEN:<aws session token>
```

.. include:: /includes/fact-aws-key-pct-encode-uri.rst

You can also set these credentials on your platform using standard [AWS IAM environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list)_. :binary:`~bin.mongosh` checks for the following environment variables when you use the `MONGODB-AWS` :urioption:`authentication mechanism <authMechanism>`:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN`
If set, these credentials do not need to be specified in the connection string.

The following example sets these environment variables in the `bash` shell:

```bash
export AWS_ACCESS_KEY_ID='<aws access key id>'
export AWS_SECRET_ACCESS_KEY='<aws secret access key>'
export AWS_SESSION_TOKEN='<aws session token>'
```

Syntax for setting environment variables in other shells will be different. Consult the documentation for your platform for more information.

To verify that these environment variables have been set, run the following command:

```none
env | grep AWS
```

Once set, the following example connects to an Atlas cluster using these environment variables:

```bash
mongodb+srv://cluster0.example.com/testdb?authSource=$external&authMechanism=MONGODB-AWS
```
