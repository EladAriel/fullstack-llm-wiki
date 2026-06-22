---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/forbidden.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: forbidden.js
description: API reference for the forbidden.js special file.
related:
  links:
    - app/api-reference/functions/forbidden
version: experimental
---

The **forbidden** file is used to render UI when the [`forbidden`](/docs/app/api-reference/functions/forbidden) function is invoked during authentication. Along with allowing you to customize the UI, Next.js will return a `403` status code.

```tsx filename="app/forbidden.tsx" switcher
import Link from 'next/link'

export default function Forbidden() {
  return (
    <div>
      <h2>Forbidden</h2>
      <p>You are not authorized to access this resource.</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```

```jsx filename="app/forbidden.jsx" switcher
import Link from 'next/link'

export default function Forbidden() {
  return (
    <div>
      <h2>Forbidden</h2>
      <p>You are not authorized to access this resource.</p>
      <Link href="/">Return Home</Link>
    </div>
  )
}
```

## Reference

### Props

`forbidden.js` components do not accept any props.

## Version History

| Version   | Changes                    |
| --------- | -------------------------- |
| `v15.1.0` | `forbidden.js` introduced. |
