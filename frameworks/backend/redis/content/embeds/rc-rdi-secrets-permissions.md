---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-rdi-secrets-permissions.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.095652Z"
---
# Rc Rdi Secrets Permissions

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