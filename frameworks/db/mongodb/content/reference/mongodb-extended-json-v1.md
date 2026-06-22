---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mongodb-extended-json-v1.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# MongoDB Extended JSON (v1)

> **Important:** The following page discusses MongoDB Extended JSON v1 (Legacy
extended JSON). For discussion on MongoDB Extended JSON v2, see
`/reference/mongodb-extended-json`.
For supported data types in :binary:`~bin.mongo`, see
:mongosh:`mongosh Data Types </reference/data-types/>`.

`JSON` can only represent a subset of the types supported by `BSON`. To preserve type information, MongoDB adds the following extensions to the JSON format:

- Strict mode. Strict mode representations of BSON types conform to
the [JSON RFC](http://www.json.org). Any JSON parser can parse these strict mode representations as key/value pairs; however, only the MongoDB internal JSON parser recognizes the type information conveyed by the format.

- `mongo` Shell mode. The MongoDB internal JSON parser and the
:binary:`~bin.mongo` shell can parse this mode.

The representation used for the various data types depends on the context in which the JSON is parsed.

## MongoDB Extended JSON v1 and MongoDB Drivers

The following drivers support Extended JSON v1.0 (Legacy):

- C#
- Ruby
> **Note:** The C# Driver 3.0 and later does not have support for strict mode but supports
shell mode.

For the other drivers, refer to `/reference/mongodb-extended-json`.

## Parsers and Supported Format

### Input in Strict Mode

The following can parse representations in strict mode with recognition of the type information.

- :binary:`~bin.mongoimport` version 4.0 and earlier
- `--query` option of various MongoDB tools
- :products:`MongoDB Compass </compass>`
Other JSON parsers, including :binary:`~bin.mongo` shell, can parse strict mode representations as key/value pairs, but without recognition of the type information.

### Input in `mongo` Shell Mode

The following can parse representations in `mongo` shell mode with recognition of the type information.

- :binary:`~bin.mongoimport` version 4.0 and earlier
- `--query` option of various MongoDB tools
- :binary:`~bin.mongo` shell
### Output in Strict Mode

Before version 4.2, :binary:`~bin.mongoexport` outputs data in strict mode of MongoDB Extended JSON v1.

### Output in `mongo` Shell Mode

Before version 4.2, :binary:`~bin.bsondump` outputs in `mongo` shell mode.

## BSON Data Types and Associated Representations

The following presents the BSON data types and the associated representations in strict mode and `mongo` shell mode.

### Binary

Where the values are as follows:

- `<bindata>` is the base64 representation of a binary string.
- `<t>` is a representation of a single byte indicating the data type. In
Strict mode it is a hexadecimal string, and in Shell mode it is an integer. See the extended bson documentation. http://bsonspec.org/spec.html

### Date

### Timestamp

Where the values are as follows:

- `<t>` is the JSON representation of a 32-bit unsigned integer for
seconds since epoch.

- `<i>` is a 32-bit unsigned integer for the increment.
### Regular Expression

Where the values are as follows:

- `<sRegex>` is a string of valid JSON characters.
- `<jRegex>` is a string that may contain valid JSON characters and
unescaped double quote (`"`) characters, but may not contain unescaped forward slash (`/`) characters.

- `<sOptions>` is a string containing the regex options represented
by the letters of the alphabet.

- `<jOptions>` is a string that may contain only the characters 'g',
'i', 'm' and 's' (added in v1.9). Because the `JavaScript` and `mongo Shell` representations support a limited range of options, any nonconforming options will be dropped when converting to this representation.

### OID

Where the values are as follows:

- `<id>` is a 24-character hexadecimal string.
### DB Reference

Where the values are as follows:

- `<name>` is a string of valid JSON characters.
- `<id>` is any valid extended JSON type.
### Undefined Type

### MinKey

### MaxKey

### NumberLong

### NumberDecimal
