---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/quick-db-setup.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

1. On the **Databases** screen, select **Quick database**.

    {{<image filename="images/rs/screenshots/databases/db-screen.png" alt="Select Quick database on the Databases screen." >}}

1. Enter 12000 for the **Port**.

    If port 12000 is not available, enter any available port number between 10000 to 19999 or leave it blank to let the cluster assign a port number for you. You will use this port number to connect to the database.

    {{<image filename="images/rs/screenshots/databases/quick-db.png" alt="Create a quick database." >}}

1. Select **Create** to create your database.

When you see **Database active** appear on the database configuration screen, the database is activated and ready for you to use.

{{<image filename="images/rs/icons/db-active-icon.png" width="150px" alt="Database active icon." >}}


You now have a Redis database!