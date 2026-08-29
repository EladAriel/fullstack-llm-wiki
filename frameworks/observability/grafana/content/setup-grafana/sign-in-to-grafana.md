---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/setup-grafana/sign-in-to-grafana.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.396200Z"
---
---
description: Learn how to sign in to Grafana
labels:
  products:
    - enterprise
    - oss
title: Sign in to Grafana
weight: 400
---

# Sign in to Grafana

This topic describes how to sign in to Grafana.

## Before you begin

- [Install Grafana](../installation/)

## Steps

To sign in to Grafana for the first time, follow these steps:

1. Open your web browser and go to root URL specified in [Grafana configuration file](../configure-grafana/).

   Unless you have configured Grafana differently, it is set to use `http://localhost:3000` by default.

1. On the signin page, enter `admin` for username and password.
1. Click **Sign in**.

   If successful, you will see a prompt to change the password.

1. Click **OK** on the prompt and change your password.

> **Note:** We strongly recommend that you change the default administrator password.
