---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/installation/remix.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.943110Z"
---
# Remix

---
title: Remix
description: Install and configure shadcn/ui for Remix.
---

<Callout>

**Note:** This guide is for Remix. For React Router, see the [React Router](/docs/installation/react-router) guide.

</Callout>

<Steps>

### Create project

Start by creating a new Remix project using `create-remix`:

```bash
npx create-remix@latest my-app
```

### Run the CLI

Run the `shadcn` init command to set up your project:

```bash
npx shadcn@latest init
```

### That's it

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```tsx {1,6} showLineNumbers title="app/routes/index.tsx"
import { Button } from "~/components/ui/button"

export default function Home() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

</Steps>
