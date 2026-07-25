---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/ensure-binaries-in-path.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The MongoDB binaries are in the `bin/` directory of the tarball. You can either:

- Copy the binaries into a directory listed in your `PATH` variable, such as
`/usr/local/bin`. Replace `/path/to/the/mongodb-directory/` with your installation directory.

```bash
   sudo cp /path/to/the/mongodb-directory/bin/* /usr/local/bin/ 
```

- Create symbolic links to the binaries from a directory listed in your `PATH`
variable, such as `/usr/local/bin`. Replace `/path/to/the/mongodb-directory/` with your installation directory.

```bash
   sudo ln -s  /path/to/the/mongodb-directory/bin/* /usr/local/bin/
```
