---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/authenticate-a-user.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================================

# Authenticate a User with Self-Managed Deployments

To authenticate as a user, you must provide a username, password, and the :option:`authentication database <mongosh --authenticationDatabase>` associated with that user.

> **Important:** It is not possible to switch between users in the same
:binary:`~bin.mongosh` session. Authenticating as a different user
means the session has the privileges of **both** authenticated
users. To switch between users exit and relaunch
:binary:`~bin.mongosh`.

Using :binary:`~bin.mongosh`, you can:

For examples using a MongoDB driver, see the :driver:`driver documentation </>`.
