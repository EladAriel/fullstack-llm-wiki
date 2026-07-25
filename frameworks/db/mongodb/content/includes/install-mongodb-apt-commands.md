---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/install-mongodb-apt-commands.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You can also install the MongoDB Shell that uses the system's OpenSSL. You must have already installed OpenSSL on your system before installing this version of the MongoDB Shell.

You can install all of the MongoDB Enterprise packages and the MongoDB Shell that uses the system's OpenSSL without removing the MongoDB Shell first. For example:

```sh
sudo apt install -y mongodb-enterprise mongodb-mongosh-shared-openssl11
```

The following example removes the MongoDB Shell and then installs the MongoDB Shell that uses the system's OpenSSL 1.1:

```sh
sudo apt remove -y mongodb-mongosh && sudo apt install -y
mongodb-mongosh-shared-openssl11
```

The following example removes the MongoDB Shell and then installs the MongoDB Shell that uses the system's OpenSSL 3:

```sh
sudo apt remove -y mongodb-mongosh && sudo apt install -y
mongodb-mongosh-shared-openssl3
```

You can also choose the MongoDB packages to install.

The following example installs MongoDB Enterprise and tools, and the MongoDB Shell that uses the system's OpenSSL 1.1:

```sh
sudo apt install -y mongodb-enterprise-database
mongodb-enterprise-tools mongodb-mongosh-shared-openssl11
```

The following example installs MongoDB Enterprise and tools, and the MongoDB Shell that uses the system's OpenSSL 3:

```sh
sudo apt install -y mongodb-enterprise-database
mongodb-enterprise-tools mongodb-mongosh-shared-openssl3
```
