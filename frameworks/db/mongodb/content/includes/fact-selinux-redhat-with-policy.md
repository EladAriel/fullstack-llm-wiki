---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-selinux-redhat-with-policy.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, a new SELinux policy is available for MongoDB installations that:

- Use an `.rpm` installer.
- Use default configuration settings.
- Run on RHEL7 or later.
> **Note:** If your MongoDB deployment uses custom settings for any of the
following:
- `MongoDB connection ports <default-mongodb-port>`
- :setting:`~storage.dbPath`
- :setting:`systemLog.path`
- :setting:`~processManagement.pidFilePath`
You cannot use the MongoDB supplied SELinux policy. An alternative
is to create a custom SELinux policy, however an
improperly written custom policy may be less secure or may stop your
:binary:`mongod` instance from working.

Install the SELinux Policy ++++++++++++++++++++++++++

#. Ensure you have the following packages installed:

- `git`
- `make`
- `checkpolicy`
- `policycoreutils`
- `selinux-policy-devel`
```bash
   sudo yum install git make checkpolicy policycoreutils selinux-policy-devel
```

#. Download the policy repository.

```bash
   git clone https://github.com/mongodb/mongodb-selinux
```

#. Build the policy.

```bash
   cd mongodb-selinux
   make
```

#. Apply the policy.

```bash
   sudo make install
```

> **Important:** .. include:: /includes/downgrade-for-SELinux-policy.rst

SELinux Policy Considerations +++++++++++++++++++++++++++++

- The SELinux policy is designed to work with the configuration that
results from a standard MongoDB `.rpm` package installation. See [standard installation assumptions](https://github.com/mongodb/mongodb-selinux/blob/master/README.md#standard-installation)_ for more details.

- The SELinux policy is designed for :binary:`~bin.mongod` servers. It
does not apply to other MongoDB daemons or tools such as:

- :binary:`~bin.mongos`
- :binary:`~bin.mongosh`
- `mongocryptd`
- The `reference policy
<https://github.com/SELinuxProject/refpolicy/blob/master/policy/modules/services/mongodb.if>`__ supplied by the SELinux Project includes a `mongodb_admin` macro. This macro is not included in the MongoDB SELinux policy. An administrator in the `unconfined_t` domain can manage :binary:`mongod`.

- To uninstall the policy, go to the directory where you downloaded the
policy repository and run:

```bash
  sudo make uninstall
```
