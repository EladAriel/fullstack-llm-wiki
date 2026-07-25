---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-rdi-secrets-permissions.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

```json
{
    "Version" : "2012-10-17",
    "Statement" : [ {
        "Sid" : "RedisDataIntegrationRoleAccess",
        "Effect" : "Allow",
        "Principal" : "*",
        "Action" : [ "secretsmanager:GetSecretValue", "secretsmanager:DescribeSecret" ],
        "Resource" : "*",
        "Condition" : {
            "StringLike" : {
                "aws:PrincipalArn" : "arn:aws:iam::<AWS ACCOUNT ID>:role/redis-data-pipeline-secrets-role"
            }
        }
    } ]
}
```

After you store this secret, you can view and copy the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#iam-resources) of your secret on the secret details page. Save the secret ARN to use when you [define your source database]({{<relref "/operate/rc/rdi/define">}}).