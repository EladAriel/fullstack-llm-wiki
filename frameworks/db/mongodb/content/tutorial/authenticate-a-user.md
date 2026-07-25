---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/authenticate-a-user.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
