---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/htmlLimitedBots.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: htmlLimitedBots
description: Specify a list of user agents that should receive blocking metadata.
---

The `htmlLimitedBots` config allows you to specify a list of user agents that should receive blocking metadata instead of [streaming metadata](/docs/app/api-reference/functions/generate-metadata#streaming-metadata).

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const config: NextConfig = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}

export default config
```

```js filename="next.config.js" switcher
module.exports = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}
```

## Default list

Next.js includes a default list of HTML limited bots, including:

- Google crawlers (e.g. Mediapartners-Google, AdsBot-Google, Google-PageRenderer)
- Bingbot
- Twitterbot
- Slackbot

See the full list [here](https://github.com/vercel/next.js/blob/canary/packages/next/src/shared/lib/router/utils/html-bots.ts).

Specifying a `htmlLimitedBots` config will override the Next.js' default list. However, this is advanced behavior, and the default should be sufficient for most cases.

```ts filename="next.config.ts" switcher
const config: NextConfig = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}

export default config
```

```js filename="next.config.js" switcher
module.exports = {
  htmlLimitedBots: /MySpecialBot|MyAnotherSpecialBot|SimpleCrawler/,
}
```

## Disabling

To fully disable streaming metadata:

```ts filename="next.config.ts"
import type { NextConfig } from 'next'

const config: NextConfig = {
  htmlLimitedBots: /.*/,
}

export default config
```

```js filename="next.config.js" switcher
module.exports = {
  htmlLimitedBots: /.*/,
}
```

## Version History

| Version | Changes                              |
| ------- | ------------------------------------ |
| 15.2.0  | `htmlLimitedBots` option introduced. |
