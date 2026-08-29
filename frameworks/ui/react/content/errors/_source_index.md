---
type: "Framework Learn Page"
framework: "React"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/errors/index.md"
source_commit: "7c36f7ac329fe3cf2e11222edce9a535158c2cab"
source_commit_short: "7c36f7a"
source_commit_date: "2026-08-24T10:33:57-07:00"
generated_at: "2026-08-29T09:40:25.475749Z"
---
# Index

<Intro>

In the minified production build of React, we avoid sending down full error messages in order to reduce the number of bytes sent over the wire.

</Intro>


We highly recommend using the development build locally when debugging your app since it tracks additional debug info and provides helpful warnings about potential problems in your apps, but if you encounter an exception while using the production build, the error message will include just a link to the docs for the error.

For an example, see: [https://react.dev/errors/149](/errors/149).
