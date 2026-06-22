---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/clients/ioredis/connect.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
categories:
- docs
- develop
- stack
- oss
- rs
- rc
- oss
- kubernetes
- clients
description: Connect your Python application to a Redis database
linkTitle: Connect
title: Connect to the server
weight: 20
---

## Basic connection

Connect to localhost on port 6379:

```js
const redis = new Redis();
```

You can also specify a full set of connection options:

```js
const redis = new Redis({
  port: 6379,
  host: "127.0.0.1",
  username: "default",
  password: "my-password",
  db: 0,
});
```

Store and retrieve a simple string.

```js
await redis.set('foo', 'bar');
const value = await redis.get('foo');
console.log(value); // >>> bar
```

## Connect to a Redis cluster

To connect to a Redis cluster, use `Redis.Cluster()`, passing an array of
endpoints.

```js
const redis = new Redis.Cluster([
    {
        host: '127.0.0.1',
        port: 6380,
        password: 'my-password',
        username: 'default',
    },
    {
        host: '127.0.0.1',
        port: 6381,
        password: 'my-other-password',
        username: 'default',
    },
    // ...
]);
```

## Connect to your production Redis with TLS

When you deploy your application, use TLS and follow the [Redis security]({{< relref "/operate/oss_and_stack/management/security/" >}}) guidelines.

```js
const redis = new Redis({
  host: "localhost",
  //...
  tls: {
    key: readFileSync('./redis_user_private.key'),
    cert: readFileSync('./redis_user.crt'),
    ca: fs.readFileSync('./redis_ca.pem'),
  },
});
```
