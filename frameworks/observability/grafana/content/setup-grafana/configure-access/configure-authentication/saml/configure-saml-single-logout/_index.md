---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/setup-grafana/configure-access/configure-authentication/saml/configure-saml-single-logout/_index.md"
source_commit: "5e3a02f81d2aadf4bf24fe49ed97d872556f5bf9"
source_commit_short: "5e3a02f8"
source_commit_date: "2026-08-29T10:58:19+09:00"
generated_at: "2026-08-29T09:39:37.419244Z"
---
---
aliases:
  - ../../../configure-security/configure-authentication/setup-grafana/configure-security/configure-authentication/saml/configure-saml-single-logout/ # /docs/grafana/next/setup-grafana/configure-security/configure-authentication/setup-grafana/configure-security/configure-authentication/saml/configure-saml-single-logout/
  - ../../../configure-security/configure-authentication/saml/configure-saml-single-logout/ # /docs/grafana/next/setup-grafana/configure-security/configure-authentication/saml/configure-saml-single-logout/
description: Learn how to configure SAML authentication in Grafana's UI.
labels:
  products:
    - cloud
    - enterprise
menuTitle: Configure SAML single logout
title: Configure SAML single logout
weight: 560
---

# Configure SAML Single Logout

The single logout feature allows users to log out from all applications associated with the current IdP session established via SAML SSO. If the `single_logout` option is set to `true` and a user logs out, Grafana requests IdP to end the user session which in turn triggers logout from all other applications the user is logged into using the same IdP session (applications should support single logout). Conversely, if another application connected to the same IdP logs out using single logout, Grafana receives a logout request from IdP and ends the user session.

{{< admonition type="note" >}}
The improved SLO features, including proper handling of the IdP's SessionIndex, are currently behind the `improvedExternalSessionHandlingSAML` feature toggle. When this feature toggle is enabled, Grafana will correctly handle session-specific logouts. If the feature toggle is not enabled, logging out will end all of the user's sessions.
{{< /admonition >}}
