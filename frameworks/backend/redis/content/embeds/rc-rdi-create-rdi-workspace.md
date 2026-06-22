---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-rdi-create-rdi-workspace.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

To create a Data Integration workspace for an existing [Pro subscription]({{< relref "/operate/rc/databases/create-database/create-pro-database-new" >}}):

1. From the Redis Cloud console, select **Data Integration** from the left-hand menu. If you don't have any workspaces yet, select **Create workspace** to go to the **Create workspace** page.

    {{<image filename="images/rc/rdi/rdi-create-workspace-button.png" alt="The create workspace button." width=200px >}}

    If you already have a workspace deployed, you'll see your current workspaces. Select **New workspace** to go to the **Create workspace** page.

    {{<image filename="images/rc/rdi/rdi-new-workspace-button.png" alt="The new workspace button." width=150px >}}

    You can also go to the **Data Integration** tab from your subscription or database page and select **Create workspace** to go to the **Create workspace** page for your subscription.

    {{<image filename="images/rc/rdi/rdi-create-workspace-button.png" alt="The create workspace button." width=200px >}}

2. Select your Pro subscription from the list if it's not already selected.

    {{<image filename="images/rc/rdi/rdi-create-workspace-select-subscription.png" alt="The select pro subscription drop down." width=80% >}}

3. A **Data Integration subnet (CIDR)** is automatically generated for you. If, for any reason, a CIDR is not generated, enter a valid CIDR that does not conflict with your applications or other databases.

    {{<image filename="images/rc/rdi/rdi-create-workspace-cidr.png" alt="The select pro subscription drop down." width=80% >}}

4. Select **Create workspace** to create your workspace.

    {{<image filename="images/rc/rdi/rdi-create-workspace-button.png" alt="The create workspace button." width=200px >}}

Your workspace will be created in the background. You can select **Create pipeline** to [create your pipeline]({{<relref "/operate/rc/rdi/define">}}) while the workspace is provisioning, or you can select **Create pipeline later** to go back to the Redis Cloud console.