---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/subscriptions/delete-subscription.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Delete a subscription
alwaysopen: false
categories:
- docs
- operate
- rc
description: null
linktitle: Delete subscription
weight: 50
---

{{<note>}}
Once a subscription is deleted, it cannot be recovered. We recommend [backing up your data]({{< relref "/operate/rc/databases/back-up-data.md" >}}) before removing databases or subscriptions.
{{</note>}}

To delete a subscription:

1.  [Delete all databases]({{< relref "/operate/rc/databases/delete-database.md" >}}) from the subscription.

    The number of databases for the subscription is shown in the subscription list. You cannot delete a subscription until there are zero databases in the subscription.

    {{<image filename="images/rc/subscription-list-pro-no-databases.png" width="50%" alt="The number of databases is shown in the bottom, left of the subscription in the subscription list." >}}

2.  View the subscription details.  

    If you have more than one subscription, select the target subscription from the subscription list.

3.  Select the **Overview** tab.

    {{<image filename="images/rc/subscription-details-overview-flexible.png" width="75%" alt="The Overview tab displays the details of your subscription." >}}

4.  Select the **Delete subscription** button.

    {{<image filename="images/rc/button-subscription-delete.png" alt="Use the Delete subscription button to delete your subscription plan." >}}

    {{<image filename="images/rc/subscription-delete-confirm-dialog.png" alt="Select the Yes, cancel button to confirm the subscription cancellation." >}}


5.  Select the **Delete subscription** button to confirm your choice.
