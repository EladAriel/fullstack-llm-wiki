---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/api/examples/manage-cloud-accounts.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Create and manage cloud accounts
alwaysopen: false
categories:
- docs
- operate
- rc
description: Cloud accounts specify which account to use when creating and modifying
  infrastructure resources.
linkTitle: Manage cloud accounts
weight: 80
draft: true
---
<!-- This article is removed since it was duplicated with the REST API reference. I decided to keep it as a draft just in case. -->

You can use the Redis Cloud REST API to create and manage cloud accounts.

These examples use the [`cURL` utility]({{< relref "/operate/rc/api/get-started/use-rest-api#use-the-curl-http-client" >}}); you can use any REST client to work with the Redis Cloud REST API.

## Create a cloud account

To create a cloud account, use the `POST /v1/cloud-accounts` endpoint.

The created cloud account is defined by a JSON document that is sent as the body of the request.

```sh
POST https://[host]/v1/cloud-accounts
{
  "accessKeyId": "$ACCESS_KEY_ID",
  "accessSecretKey": "$ACCESS_SECRET_KEY",
  "consolePassword": "$CONSOLE_PASSWORD",
  "consoleUsername": "$CONSOLE_USERNAME",
  "name": "My new Cloud Account",
  "provider": "AWS",
  "signInLoginUrl": "https://$AWS_ACCOUNT_IDENTIFIER.signin.aws.amazon.com/console"
}
```

The POST response is a JSON document that contains the `taskId`. You can use `GET /v1/tasks/<taskId>` to track the status of the cloud account creation.
