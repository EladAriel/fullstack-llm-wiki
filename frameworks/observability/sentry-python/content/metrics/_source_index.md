---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/metrics/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.042700Z"
---
# Index

---
title: Set Up Metrics
sidebar_title: Application Metrics
description: "Metrics allow you to send, view and query counters, gauges and measurements sent from your applications within Sentry."
sidebar_order: 7
sidebar_section: features
new: true
---

<AgentSetupCallout skill="sentry-python-sdk" platformName="Python" />

Sentry metrics help you pinpoint and solve issues that impact user experience and app performance by measuring the data points that are important to you. You can track things like processing time, event size, user signups, and conversion rates, then correlate them back to tracing data in order to get deeper insights and solve issues faster.

Once in Sentry, these metrics can be viewed alongside relevant errors, and searched using their individual attributes.

## Requirements

<PlatformContent includePath="metrics/requirements" />

## Usage

<PlatformContent includePath="metrics/usage" />

## Options

<PlatformContent includePath="metrics/options" />

## Default Attributes

<PlatformContent includePath="metrics/default-attributes" />
