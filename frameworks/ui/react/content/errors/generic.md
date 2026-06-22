---
type: "Framework Learn Page"
framework: "react"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/errors/generic.md"
source_commit: "8bb31acb86bf68fa33d97dd0f1b834dfa71e2b1a"
source_commit_short: "8bb31acb"
source_commit_date: "2026-06-17T13:38:02-04:00"
generated_at: "2026-06-21T12:23:02Z"
---

<Intro>

In the minified production build of React, we avoid sending down full error messages in order to reduce the number of bytes sent over the wire.

</Intro>

We highly recommend using the development build locally when debugging your app since it tracks additional debug info and provides helpful warnings about potential problems in your apps, but if you encounter an exception while using the production build, this page will reassemble the original error message.

The full text of the error you just encountered is:

<ErrorDecoder />
