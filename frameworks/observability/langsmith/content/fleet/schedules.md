---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/fleet/schedules.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.698433Z"
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
