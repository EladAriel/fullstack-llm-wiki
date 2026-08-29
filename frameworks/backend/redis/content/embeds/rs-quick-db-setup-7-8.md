---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rs-quick-db-setup-7-8.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.096648Z"
---
# Rs Quick Db Setup 7 8

1. On the **Databases** screen, select **Quick database**.

    {{<image filename="images/rs/screenshots/databases/db-screen.png" alt="Select Quick database on the Databases screen." >}}

1. Enter 12000 for the **Port**.

    If port 12000 is not available, enter any available port number between 10000 to 19999 or leave it blank to let the cluster assign a port number for you. You will use this port number to connect to the database.

    {{<image filename="images/rs/screenshots/databases/quick-db-7-8-2.png" alt="Create a quick database." >}}

1. Select **Create** to create your database.

When you see **Database active** appear on the database configuration screen, the database is activated and ready for you to use.

{{<image filename="images/rs/icons/db-active-icon.png" width="150px" alt="Database active icon." >}}


You now have a Redis database!