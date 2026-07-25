---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-create-db-use-cases.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

3. Select your Redis use case. There are four pre-defined use cases:

    {{<image filename="images/rc/create-database-redis-use-cases.png" alt="The Redis Use case panel">}}

    - **Cache**: Stores short-term or volatile data. Can be used for session management, semantic cache, session store, and other uses where data is short-lived.
    - **Database**: Stores durable and consistent data. Can be used for document databases, feature storage, gaming leaderboards, durable caches, and other uses where your data needs to be highly available and persistent.
    - **Vector search**: Manages and manipulates vector data. Can be used for Generative AI, recommendation systems, visual search, and other uses where you can search and query your data.
    - **Custom**: If your Redis use case doesn't match any of the other use cases, you can choose this option to customize all of your settings.

    Select the use case that best matches your Redis use case. You can always change the settings later. 