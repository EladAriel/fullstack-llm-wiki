---
type: "Framework Learn Page"
framework: "Grafana"
source_repo: "https://github.com/grafana/grafana.git"
source_branch: "main"
source_path: "docs/sources/as-code/infrastructure-as-code/ansible/_index.md"
source_commit: "d18e58d33aa8741f08fbab4aa73bdaf1f04e3be5"
source_commit_short: "d18e58d3"
source_commit_date: "2026-07-25T13:50:43+02:00"
generated_at: "2026-07-25T19:08:09.053407Z"
---
---
keywords:
  - Infrastructure as Code
  - Quickstart
  - Grafana Cloud
  - Ansible
menuTitle: Ansible
title: Grafana Ansible collection
weight: 110
canonical: https://grafana.com/docs/grafana/latest/as-code/infrastructure-as-code/ansible/
aliases:
  - ../../infrastructure-as-code/ansible/ansible-grafana-agent-linux
  - ../../infrastructure-as-code/ansible/ansible-multiple-agents
labels:
  products:
    - cloud
---

# Grafana Ansible collection

The [Grafana Ansible collection](https://docs.ansible.com/ansible/latest/collections/grafana/grafana/) provides configuration management resources for Grafana. You can use it to manage:

- Grafana Cloud stacks
- Dashboards
- Data sources
- Folders
- Alerting contact points
- Notification policies
- API keys

If your resources aren't currently available in the Grafana Ansible collection, you can manage them on Grafana Cloud programmatically by writing Ansible playbooks that use the [Ansible's built-in URI module](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/uri_module.html) to call the [HTTP APIs](/docs/grafana/latest/developers/http_api/) to manage resources for the Grafana Cloud portal, as well as those within a stack.

## Learn more

Refer to [Create and manage a Grafana Cloud stack using Ansible](ansible-cloud-stack/) to learn how to create a Grafana Cloud stack and add a data source and dashboard using [Ansible](https://www.ansible.com/).

To learn more about managing Grafana with Infrastructure as code:

- [Grafana Ansible collection documentation](https://docs.ansible.com/ansible/latest/collections/grafana/grafana/)
- [Ansible playbook best practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Grafana API documentation](/docs/grafana/latest/developers/http_api/)
- [Grafana Cloud API documentation](https://grafana.com/docs/grafana-cloud/developer-resources/api-reference/)
- [Infrastructure as Code with Terraform](/docs/grafana/latest/as-code/infrastructure-as-code/terraform/)

## Grafana Agent (deprecated)

{{< docs/shared lookup="agent-deprecation.md" source="alloy" version="next" >}}

The Ansible collection also houses [Grafana Agent role](https://github.com/grafana/grafana-ansible-collection/tree/main/roles/grafana_agent), which is now deprecated.
