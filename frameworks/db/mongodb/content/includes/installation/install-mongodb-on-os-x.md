---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/installation/install-mongodb-on-os-x.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# Install MongoDB Community Edition on macOS

## Overview

Use this tutorial to install MongoDB {+version+} |edition| Edition on macOS using the third-party [Homebrew](https://brew.sh)_ package manager.

Starting with MongoDB 4.4.1, installing MongoDB through Homebrew also installs the :dbtools:`MongoDB Database Tools </>`. See `brew-installs-dbtools` for more information.

### MongoDB Version

.. include:: /includes/fact-install-past-mongodb.rst

## Considerations

### Platform Support

.. include:: /includes/fact-platform-support-macos.rst

### Production Notes

.. include:: /includes/fact-see-production-notes.rst

## Install MongoDB Community Edition

### Prerequisites

Ensure your system meets each of the following prerequisites. You only need to perform each prerequisite step once on your system. If you have already performed the prerequisite steps as part of an earlier MongoDB installation using Homebrew, you can skip to the `installation procedure <install>`.

Install Xcode Command-Line Tools ````````````````````````````````

Homebrew requires the Xcode command-line tools from Apple's Xcode.

- Install the Xcode command-line tools by running the following
command in your macOS Terminal:

```bash
  xcode-select --install
```

Install Homebrew ````````````````

macOS does not include the Homebrew `brew` package by default.

- Install `brew` using the official
[Homebrew installation instructions](https://brew.sh/#install).

### Installing MongoDB {+version+} |edition| Edition

Follow these steps to install MongoDB |edition| Edition using Homebrew's `brew` package manager. Be sure that you have followed the `installation prerequisites <osx-prereq>` above before proceeding.

#. Tap the [MongoDB Homebrew Tap](https://github.com/mongodb/homebrew-brew) to download the official Homebrew formula for MongoDB and the Database Tools, by running the following command in your macOS Terminal:

```bash
   brew tap mongodb/brew

If you have already done this for a previous installation of MongoDB,
you can skip this step.
```

#. To update Homebrew and all existing formulae:

```bash
   brew update
```

#. To install MongoDB, run the following command in your macOS Terminal application:

```bash
   brew install mongodb-community@{+version+}
```

> **Tip:** Alternatively, you can specify a previous version of MongoDB if
desired. You can also maintain multiple versions of MongoDB side by
side in this manner.

> **Tip:** If you have previously installed an older version of the formula,
you may encounter a ChecksumMismatchError. To resolve, see
`troubleshooting-checksumerror`.

The installation includes the following binaries:

- The :binary:`~bin.mongod` server
- The :binary:`~bin.mongos` sharded cluster query router
- The MongoDB Shell, :binary:`~bin.mongosh`
In addition, the installation creates the following files and directories at the location specified below, depending on your Apple hardware:

See [Apple's documentation](https://support.apple.com/en-us/HT211814)_ for the current list of Apple hardware using the Apple Silicon processor. You can also run the following command to check where `brew` has installed these files and directories:

```bash
brew --prefix
```

Starting with MongoDB 4.4.1, the installation also includes the :dbtools:`MongoDB Database Tools </>`. See `brew-installs-dbtools` for more information.

## Run MongoDB Community Edition

Follow these steps to run MongoDB |edition| Edition. These instructions assume that you are using the default settings.

You can run MongoDB as a macOS service using `brew`, or you can run MongoDB manually as a background process.

> **Note:** .. include:: /includes/installation/ulimit-macos-brew-note.rst
See `Ulimit Settings <ulimit-settings>` for more information.

- To run MongoDB (i.e. the :binary:`~bin.mongod` process) **as a
macOS service**, run:

```bash
  brew services start mongodb-community@{+version+}

To stop a :binary:`~bin.mongod` running as a macOS service, use the
following command as needed:

.. code-block:: bash

  brew services stop mongodb-community@{+version+}
```

- To run :binary:`~bin.mongod` **manually as a background process**
using a config file:

- If your deployment does not use :ref:`TLS connections
<configure-mongod-mongos-for-tls-ssl>`, use the `--fork` option:

- For macOS running on Intel processors, run:
```bash
      mongod --config /usr/local/etc/mongod.conf --fork

 - For macOS running on `Apple Silicon processors
   <https://support.apple.com/en-us/HT211814>`__, run:

   .. code-block:: bash

      mongod --config /opt/homebrew/etc/mongod.conf --fork

 - If your deployment uses :ref:`TLS connections
   <configure-mongod-mongos-for-tls-ssl>`, use `GNU Screen
   <https://www.gnu.org/software/screen/>`_.

   - For macOS running on Intel processors:

     .. procedure::
        :style: normal 

        .. step:: Start your screen.

           .. code-block:: bash

              screen -S <name-of-screen>

        .. step:: Start ``mongod``.

           .. code-block:: bash

              mongod --config /usr/local/etc/mongod.conf 

        .. step:: Detach from screen.

           Detach from your screen by typing ``Ctrl+a``, then
           clicking ``d``.

        .. step:: View all active screens.

           .. code-block:: bash

              screen -ls

   - For macOS running on `Apple Silicon processors
     <https://support.apple.com/en-us/HT211814>`__:

     .. procedure::
        :style: normal 

        .. step:: Start your screen.

           .. code-block:: bash

              screen -S <name-of-screen>

        .. step:: Start ``mongod``.

              .. code-block:: bash

                 mongod --config /opt/homebrew/etc/mongod.conf

        .. step:: Detach from screen.

           Detach from your screen by typing ``Ctrl+a``, then
           clicking ``d``.

        .. step:: View all active screens.

           .. code-block:: bash

              screen -ls
```

- To run `mongod` **manually as a background process** specifying
:option:`--dbpath <mongod --dbpath>` and :option:`--logpath <mongod --logpath>` on the command line, run:

```bash
  mongod --dbpath /path/to/dbdir --logpath /path/to/mongodb.log --fork

To stop a :binary:`~bin.mongod` running as a background process,
connect to the :binary:`~bin.mongod` using :mongosh:`mongosh </>`,
and issue the :dbcommand:`shutdown` command as needed.
```

Both methods use the :file:`mongod.conf` file created during the install. You can add your own MongoDB `configuration options </reference/configuration-options>` to this file as well.

> **Note:** .. include:: /includes/extracts/macos-prevent-launch-mongod.rst

To verify that MongoDB is running, perform one of the following:

- If you started MongoDB **as a macOS service**:
```bash
  brew services list

You should see the service ``mongodb-community`` listed as
``started``.
```

- If you started MongoDB **manually as a background process**:
```bash
  ps aux | grep -v grep | grep mongod

You should see your ``mongod`` process in the output.
```

You can also view the log file to see the current status of your `mongod` process: `/usr/local/var/log/mongodb/mongo.log`.

### Connect and Use MongoDB

To begin using MongoDB, connect :binary:`~bin.mongosh` to the running instance. From a new terminal, issue the following:

```bash
mongosh
```

For information on CRUD (Create,Read,Update,Delete) operations, see:

- `/tutorial/insert-documents`
- `/tutorial/query-documents`
- `/tutorial/update-documents`
- `/tutorial/remove-documents`
## Using the MongoDB Database Tools

Starting in MongoDB 4.4.1, installing MongoDB through `brew` also installs the MongoDB Database Tools.

The :dbtools:`MongoDB Database Tools </>` are a collection of command-line utilities for working with a MongoDB deployment, including data backup and import/export tools like :binary:`mongoimport` and :binary:`mongodump` as well as monitoring tools like :binary:`mongotop`.

Once you have installed the MongoDB Server in the steps above, the Database Tools are available directly from the command line in your macOS Terminal application. For example you could run :binary:`mongotop` against your running MongoDB instance by invoking it in your macOS Terminal like so:

```bash
mongotop
```

It should start up, connect to your running :binary:`mongod`, and start reporting usage statistics.

See the :dbtools:`MongoDB Database Tools Documentation</>` for usage information for each of the Database Tools.

## Additional Information

### Localhost Binding by Default

.. include:: /includes/fact-installation-bind-ip-default-in-config.rst

### Troubleshooting ChecksumMismatchError

If you have previously installed an older version of the formula, you may encounter a `ChecksumMismatchError` resembling the following:

```bash
Error: An exception occurred within a child process:

  ChecksumMismatchError: SHA256 mismatch

Expected: c7214ee7bda3cf9566e8776a8978706d9827c1b09017e17b66a5a4e0c0731e1f

  Actual: 6aa2e0c348e8abeec7931dced1f85d4bb161ef209c6af317fe530ea11bbac8f0

 Archive: /Users/kay/Library/Caches/Homebrew/downloads/a6696157a9852f392ec6323b4bb697b86312f0c345d390111bd51bb1cbd7e219--mongodb-macos-x86_64-4.2.0.tgz

To retry an incomplete download, remove the file above.
```

To fix:

#. Remove the downloaded :file:`.tgz` archive.

#. Retap the formula.

```bash
   brew untap mongodb/brew && brew tap mongodb/brew
```

#. Retry the install.

```bash
   brew install mongodb-community@{+version+}
```
