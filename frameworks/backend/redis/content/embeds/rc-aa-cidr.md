---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/rc-aa-cidr.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.095517Z"
---
# Rc Aa Cidr

Every CIDR should be unique to properly route network traffic between each Active-Active database instance and your consumer VPCs. The CIDR block regions should _not_ overlap between the Redis server and your app consumer VPCs. In addition, CIDR blocks should not overlap between cluster instances. 

When all **Deployment CIDR** regions display a green checkmark, you're ready to continue.  

{{<image filename="images/rc/icon-cidr-address-ok.png" width="30px" alt="Green checkmarks indicate valid CIDR address values." >}}

Red exclamation marks indicate error conditions; the tooltip provides additional details.

{{<image filename="images/rc/icon-cidr-address-error.png" width="30px" alt="Red exclamation points indicate CIDR address problems." >}} 