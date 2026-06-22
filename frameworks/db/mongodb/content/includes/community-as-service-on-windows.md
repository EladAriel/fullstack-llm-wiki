---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/community-as-service-on-windows.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Start MongoDB Community Edition as a Windows Service

You can install and configure MongoDB as a :guilabel:`Windows Service` during the install, and the MongoDB service starts upon successful installation.

You can also manually manage the service from the command line. To start the MongoDB service from the command line, open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows- commands/cmd)_ (`cmd.exe`) as an :guilabel:`Administrator`, and run the following command:

.. include:: /includes/steps/create-manually-windows-service-for-mongodb.rst

### Stop MongoDB Community Edition as a Windows Service

To stop/pause the MongoDB service, you can use the Services console:

#. From the Services console, locate the MongoDB service.

#. Right-click on the MongoDB service and click :guilabel:`Stop` (or :guilabel:`Pause`).

You can also manage the service from the command line. To stop the MongoDB service from the command line, open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows- commands/cmd)_ (`cmd.exe`) as an :guilabel:`Administrator`, and run the following command:

```bat
net stop MongoDB
```

### Remove MongoDB Community Edition as a Windows Service

To remove the MongoDB service, first use the Services console to stop the service. Then open a [Windows command prompt/interpreter](https://docs.microsoft.com/en-us/windows-server/administration/windows- commands/cmd)_ (`cmd.exe`) as an :guilabel:`Administrator`, and run the following command:

```bat
sc.exe delete MongoDB
```
