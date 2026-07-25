---
type: "Framework Learn Page"
framework: "react"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/errors/index.md"
source_commit: "7b6c3ceb9dd97249e9dce4a8a94e61aed6424698"
source_commit_short: "7b6c3ceb"
source_commit_date: "2026-07-20T15:31:48+02:00"
generated_at: "2026-07-25T11:50:43Z"
generated_filename: "_source_index.md"
---

<Intro>

In the minified production build of React, we avoid sending down full error messages in order to reduce the number of bytes sent over the wire.

</Intro>


We highly recommend using the development build locally when debugging your app since it tracks additional debug info and provides helpful warnings about potential problems in your apps, but if you encounter an exception while using the production build, the error message will include just a link to the docs for the error.

For an example, see: [https://react.dev/errors/149](/errors/149).
