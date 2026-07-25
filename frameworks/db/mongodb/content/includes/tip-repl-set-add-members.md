---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tip-repl-set-add-members.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Before MongoDB 5.0, a newly added secondary still counts as a voting member even though it can neither serve reads nor become primary until its data is consistent. If you are running a MongoDB version earlier than 5.0 and add a secondary with its :rsconf:`~members[n].votes` and :rsconf:`~members[n].priority` settings greater than zero, this can lead to a case where a majority of the voting members are online but no primary can be elected. To avoid such situations, consider adding the new secondary initially with :rsconf:`priority :0 <members[n].priority>` and :rsconf:`votes :0 <members[n].votes>`. Then, run :method:`rs.status()` to ensure the member has transitioned into :replstate:`SECONDARY` state. Finally, use :method:`rs.reconfig()` to update its priority and votes.
