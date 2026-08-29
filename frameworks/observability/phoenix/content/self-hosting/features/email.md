---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/features/email.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.916082Z"
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


