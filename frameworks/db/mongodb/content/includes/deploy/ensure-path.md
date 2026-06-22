---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/ensure-path.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The MongoDB binaries are in the `bin/` directory of the tarball. You can either:

- Copy the binaries into a directory listed in your `PATH`
variable, such as `/usr/local/bin` (Update `/path/to/the/mongodb-directory/` with your installation directory as appropriate)

```bash
  sudo cp /path/to/the/mongodb-directory/bin/* /usr/local/bin/
```

- Create symbolic links to the binaries from a directory listed
in your `PATH` variable, such as `/usr/local/bin` (Update `/path/to/the/mongodb-directory/` with your installation directory as appropriate):

```bash
  sudo ln -s  /path/to/the/mongodb-directory/bin/* /usr/local/bin/
```
