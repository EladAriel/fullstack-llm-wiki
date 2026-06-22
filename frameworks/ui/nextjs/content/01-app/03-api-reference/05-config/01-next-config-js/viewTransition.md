---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/viewTransition.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: viewTransition
description: Enable ViewTransition API from React in App Router
version: experimental
---

`viewTransition` enables React's [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) integration in Next.js. This lets you animate navigations, loading states, and content changes using the native browser View Transitions API.

To enable this feature, you need to set the `viewTransition` property to `true` in your `next.config.js` file.

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    viewTransition: true,
  },
}

module.exports = nextConfig
```

> [!NOTE]
> The [`<ViewTransition>`](https://react.dev/reference/react/ViewTransition) component is provided by React.
> The `experimental.viewTransition` flag enables Next.js integration, such as triggering
> transitions during route navigations.

## Usage

You can import the [`<ViewTransition>` Component](https://react.dev/reference/react/ViewTransition) from React in your application:

```jsx
import { ViewTransition } from 'react'
```

### Live Demo

Check out the [View Transitions Demo](https://react-view-transitions-demo.labs.vercel.dev) to see this feature in action, or read the [designing view transitions guide](/docs/app/guides/view-transitions) for a step-by-step walkthrough.

The View Transitions API is a baseline web standard, and browser support continues to expand. As React's [`<ViewTransition>`](https://react.dev/reference/react/ViewTransition) component evolves, more transition patterns and use cases will become available.
