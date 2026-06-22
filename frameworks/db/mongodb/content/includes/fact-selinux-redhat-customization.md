---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-selinux-redhat-customization.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Using a Custom MongoDB Directory Path +++++++++++++++++++++++++++++++++++++

#. Update the SELinux policy to allow the `mongod` service to use the new directory:

```bash
   sudo semanage fcontext -a -t <type> </some/MongoDB/directory.*>

Specify one of the following types as appropriate:

- ``mongod_var_lib_t`` for data directory

- ``mongod_log_t`` for log file directory

- ``mongod_var_run_t`` for pid file directory

.. note::

   Be sure to include the ``.*`` at the end of the directory.
```

#. Update the SELinux user policy for the new directory:

```bash
   sudo chcon -Rv -u system_u -t <type> </some/MongoDB/directory>

Specify one of the following types as appropriate:

- ``mongod_var_lib_t`` for data directory

- ``mongod_log_t`` for log directory

- ``mongod_var_run_t`` for pid file directory
```

#. Apply the updated SELinux policies to the directory:

```bash
   sudo restorecon -R -v </some/MongoDB/directory>
```

For example:

> **Tip:** Be sure to include the `.*` at the end of the directory for the
`semanage fcontext` operations.

- If using a non-default MongoDB data path of `/mongodb/data`:
```bash
  sudo semanage fcontext -a -t mongod_var_lib_t '/mongodb/data.*'
  sudo chcon -Rv -u system_u -t mongod_var_lib_t '/mongodb/data'
  sudo restorecon -R -v '/mongodb/data'
```

- If using a non-default MongoDB log directory of `/mongodb/log`
(e.g. if the log file path is `/mongodb/log/mongod.log`):

```bash
  sudo semanage fcontext -a -t mongod_log_t '/mongodb/log.*'
  sudo chcon -Rv -u system_u -t mongod_log_t '/mongodb/log'
  sudo restorecon -R -v '/mongodb/log' 
```

Using a Custom MongoDB Port +++++++++++++++++++++++++++

```bash
sudo semanage port -a -t mongod_port_t -p tcp <portnumber>
```
