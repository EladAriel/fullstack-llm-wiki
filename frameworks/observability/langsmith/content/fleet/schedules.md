---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/fleet/schedules.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1df"
source_commit_date: "2026-07-25T00:27:23+00:00"
generated_at: "2026-07-25T19:08:33.438507Z"
---
# Schedules

---
title: Schedules
description: Configure schedules to run your Fleet agents on a recurring basis.
---

Schedules run your agent on a recurring time-based schedule. Use schedules when your agent needs to do work proactively, not just in response to a message or event.

Common use cases include:

- **Daily briefings**: Summarize emails, calendar events, or Slack activity each morning.
- **Memory synthesis**: Periodically review and consolidate the agent's memory files to keep context clean and relevant.
- **Proactive outreach**: Draft weekly status updates, follow-up reminders, or recurring reports.
- **Data monitoring**: Check dashboards, metrics, or feeds on a set cadence and surface anything noteworthy.

<Tip>
To start an agent based on an event (such as a Slack message or email), use [channels](/langsmith/fleet/channels) instead.
</Tip>

## Add a schedule

To add a schedule:

1. In the **Schedules** section, click **+ Add**.
1. Select when the schedule should run.

    <Note>
    Schedules are in UTC. Convert your desired execution time to UTC when configuring the schedule.
    </Note>

1. (Optional) Add a **Prompt**. With a custom prompt, you can tell the agent what to do on each scheduled run. For example:

    - "Summarize my unread emails from the last 24 hours and post a digest to #team-updates in Slack."                               
    - "Review your memory files and consolidate any redundant or outdated entries." 

1. Click **Create schedule**.
1. Click **Save changes**.
