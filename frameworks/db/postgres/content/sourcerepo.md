---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/sourcerepo.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## The Source Code Repository

Git

The PostgreSQL source code is stored and managed using the Git version control system. A public mirror of the master repository is available; it is updated within a minute of any change to the master repository.

Our wiki, [https://wiki.postgresql.org/wiki/Working_with_Git](https://wiki.postgresql.org/wiki/Working_with_Git), has some discussion on working with Git.

## Getting the Source via Git

With Git you will make a copy of the entire code repository on your local machine, so you will have access to all history and branches offline. This is the fastest and most flexible way to develop or test patches.

## Git

You will need an installed version of Git, which you can get from [https://git-scm.com](https://git-scm.com). Many systems already have a recent version of `Git` installed by default, or available in their package distribution system.

To begin using the Git repository, make a clone of the official mirror:

```
git clone https://git.postgresql.org/git/postgresql.git
```

This will copy the full repository to your local machine, so it may take a while to complete, especially if you have a slow Internet connection. The files will be placed in a new subdirectory `postgresql` of your current directory.

Whenever you want to get the latest updates in the system, `cd` into the repository, and run:

```
git fetch
```

Git can do a lot more things than just fetch the source. For more information, consult the Git man pages, or see the website at [https://git-scm.com](https://git-scm.com).
