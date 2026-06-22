---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/02-pages/03-building-your-application/01-routing/05-custom-app.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: Custom App
description: Control page initialization and add a layout that persists for all pages by overriding the default App component used by Next.js.
---

Next.js uses the `App` component to initialize pages. You can override it and control the page initialization and:

- Create a shared layout between page changes
- Inject additional data into pages
- [Add global CSS](/docs/app/getting-started/css)

## Usage

To override the default `App`, create the file `pages/_app` as shown below:

```tsx filename="pages/_app.tsx" switcher
import type { AppProps } from 'next/app'

export default function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}
```

```jsx filename="pages/_app.jsx" switcher
export default function MyApp({ Component, pageProps }) {
  return <Component {...pageProps} />
}
```

The `Component` prop is the active `page`, so whenever you navigate between routes, `Component` will change to the new `page`. Therefore, any props you send to `Component` will be received by the `page`.

`pageProps` is an object with the initial props that were preloaded for your page by one of our [data fetching methods](/docs/pages/building-your-application/data-fetching), otherwise it's an empty object.

> **Good to know**:
>
> - If your app is running and you added a custom `App`, you'll need to restart the development server. Only required if `pages/_app.js` didn't exist before.
> - `App` does not support Next.js [Data Fetching methods](/docs/pages/building-your-application/data-fetching) like [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props) or [`getServerSideProps`](/docs/pages/building-your-application/data-fetching/get-server-side-props).

## `getInitialProps` with `App`

Using [`getInitialProps`](/docs/pages/api-reference/functions/get-initial-props) in `App` will disable [Automatic Static Optimization](/docs/pages/building-your-application/rendering/automatic-static-optimization) for pages without [`getStaticProps`](/docs/pages/building-your-application/data-fetching/get-static-props).

**We do not recommend using this pattern.** Instead, consider [incrementally adopting](/docs/app/guides/migrating/app-router-migration) the App Router, which allows you to more easily fetch data for pages and layouts.

```tsx filename="pages/_app.tsx" switcher
import App, { AppContext, AppInitialProps, AppProps } from 'next/app'

type AppOwnProps = { example: string }

export default function MyApp({
  Component,
  pageProps,
  example,
}: AppProps & AppOwnProps) {
  return (
    <>
      <p>Data: {example}</p>
      <Component {...pageProps} />
    </>
  )
}

MyApp.getInitialProps = async (
  context: AppContext
): Promise<AppOwnProps & AppInitialProps> => {
  const ctx = await App.getInitialProps(context)

  return { ...ctx, example: 'data' }
}
```

```jsx filename="pages/_app.jsx" switcher
import App from 'next/app'

export default function MyApp({ Component, pageProps, example }) {
  return (
    <>
      <p>Data: {example}</p>
      <Component {...pageProps} />
    </>
  )
}

MyApp.getInitialProps = async (context) => {
  const ctx = await App.getInitialProps(context)

  return { ...ctx, example: 'data' }
}
```
