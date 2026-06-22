---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/expansion-directives.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================================

# External Configuration Values for Self-Managed MongoDB

MongoDB supports using expansion directives in configuration files to load externally sourced values. Expansion directives can load values for specific `configuration file options <configuration-options>` or load the entire configuration file. Expansion directives help obscure confidential information like security certificates and passwords.

```yaml
storage: 
  dbPath: "/var/lib/mongo"
systemLog:
  destination: file
  path: "/var/log/mongodb/mongod.log"
net:
  bindIp:
    __exec: "python /home/user/getIPAddresses.py"
    type: "string"
    trim: "whitespace"
    digest: 85fed8997aac3f558e779625f2e51b4d142dff11184308dc6aca06cff26ee9ad
    digest_key: 68656c6c30303030307365637265746d796f6c64667269656e64
  tls:
    mode: requireTLS
    certificateKeyFile: "/etc/tls/mongod.pem"
    certificateKeyFilePassword:
      __rest: "https://myrestserver.example.net/api/config/myCertKeyFilePassword"
      type: "string"
      digest: b08519162ba332985ac18204851949611ef73835ec99067b85723e10113f5c26
      digest_key: 6d795365637265744b65795374756666
```

- .. include:: /includes/extracts/4.2-changes-expansion-configuration-file-permission-rest.rst
- .. include:: /includes/extracts/4.2-changes-expansion-configuration-file-permission-exec.rst
To use expansion directives, you must specify the :option:`--configExpand <mongod --configExpand>` command-line option with the complete list of expansion directives used:

```bash
mongod --config "/path/to/config/mongod.conf" --configExpand "rest,exec"
```

If you omit the :option:`--configExpand <mongod --configExpand>` option or if you do not specify the complete list of expansion directives used in the configuration file, the |mongods| returns an error and terminates. You can only specify the :option:`--configExpand <mongod --configExpand>` option on the command line.

## Use the `__rest` Expansion Directive

The :configexpansion:`__rest` expansion directive loads configuration file values from a `REST endpoint. _rest` supports loading specific values  in the configuration file or loading the entire configuration file.

> **Important:** The value returned by the specified `REST` endpoint
**cannot** include any additional expansion directives. The
|mongods| does **not** perform additional
processing on the returned data and will terminate with an
error code if the returned data includes additional
expansion directives.

## Use the `__exec` Expansion Directive

The :configexpansion:`__exec expansion directive loads configuration file values from a shell or terminal command. _exec` supports loading specific values in the configuration file or loading the entire configuration file.

> **Important:** The data returned by executing the specified  `__exec`
string **cannot** include any additional expansion
directives. The |mongods| does **not**
perform additional processing on the returned data and
will terminate with an error code if the returned data
includes additional expansion directives.

## Expansion Directives Reference

## Output the Configuration File with Resolved Expansion Directive Values

You can test the final output of a configuration file that specifies one or more expansion directives by starting the |mongods| with the :option:`--outputConfig <mongod --outputConfig>` option. A |mongods| started with :option:`--outputConfig <mongod --outputConfig>` outputs the resolved YAML configuration document to `stdout` and halts. If any expansion directive specified in the configuration file returns additional expansion directives, the |mongods| throws an error and terminates.

> **Warning:** The :option:`--outputConfig <mongod --outputConfig>` option returns
the resolved values for any field using an expansion directive. This
includes any private or sensitive information previously obscured by
using an external source for the configuration option.

For example, the following configuration file `mongod.conf contains a :configexpansion:_rest` expansion directive:

```yaml
storage:
  dbPath: "/var/lib/mongo"
systemLog:
  destination: file
  path: "/var/log/mongodb/mongod.log"
net:
  port:
    __rest: "https://mongoconf.example.net:8080/record/1"
    type: string
```

The string recorded at the specified URL is `20128`

.. include:: /includes/extracts/4.2-changes-expansion-configuration-file-permission-rest.rst

Start the :binary:`mongod <bin.mongod>` with the :option:`--configExpand "rest" <mongod --configExpand>` and :option:`--outputConfig <mongod --outputConfig>` options:

```yaml
mongod -f mongod.conf --configExpand rest --outputConfig
```

The :binary:`mongod <bin.mongod>` outputs the following to `stdout` before terminating:

```yaml
config: mongod.conf
storage:
  dbPath: "/var/lib/mongo"
systemLog:
  destination: file
  path: "/var/log/mongodb/mongod.log"
net:
  port: 20128
outputConfig: true
```
