---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/features/email.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.939338Z"
---
# Email

---
title: "Email"
---

Optionally, you can configure an SMTP server to send transactional emails. These are used for password resets, user invitations, and more.

* **PHOENIX\_SMTP\_HOSTNAME:** The SMTP hostname to use for sending password reset emails.

* **PHOENIX\_SMTP\_PORT:** The SMTP port. Defaults to `587`.

* **PHOENIX\_SMTP\_USERNAME:** The SMTP username.

* **PHOENIX\_SMTP\_PASSWORD:** The SMTP password.

* **PHOENIX\_SMTP\_MAIL\_FROM:** The `from` address in the emails. Defaults to `noreply@arize.com`.

* **PHOENIX\_SMTP\_VALIDATE\_CERTS:** Whether to validate the SMTP server's certificate. Defaults to `true`.

Example usage:

```javascript
export PHOENIX_SMTP_HOSTNAME="smtp.example.com"
export PHOENIX_SMTP_PORT=587
export PHOENIX_SMTP_USERNAME="phoenix-user"
export PHOENIX_SMTP_PASSWORD="yourpassword"
export PHOENIX_SMTP_MAIL_FROM="noreply@yourdomain.com"
export PHOENIX_SMTP_VALIDATE_CERTS=true
```

These settings are required for password reset flows when authentication is enabled in Phoenix.

## FAQ

<Accordion title="Which SMTP service should I use?">
* It is recommended to use a reputable SMTP service for transactional emails to ensure delivery and prevent abuse. If you do not have a preferred service from your cloud provider, consider providers like Resend, Mailgun, Sendgrid, or Postmark, which are easy to set up and offer generous free tiers.
</Accordion>


