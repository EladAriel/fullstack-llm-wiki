---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/installation/tanstack-router.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: TanStack Router
description: Install and configure shadcn/ui for TanStack Router.
---

<Steps>

### Create project

Start by creating a new TanStack Router project:

```bash
npx create-tsrouter-app@latest my-app --template file-router --tailwind --add-ons shadcn
```

### Add Components

You can now start adding components to your project.

```bash
npx shadcn@latest add button
```

The command above will add the `Button` component to your project. You can then import it like this:

```tsx title="src/routes/index.tsx" showLineNumbers {3,12}
import { createFileRoute } from "@tanstack/react-router"

import { Button } from "@/components/ui/button"

export const Route = createFileRoute("/")({
  component: App,
})

function App() {
  return (
    <div>
      <Button>Click me</Button>
    </div>
  )
}
```

</Steps>
