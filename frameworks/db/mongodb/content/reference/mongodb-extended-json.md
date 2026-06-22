---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mongodb-extended-json.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# MongoDB Extended JSON (v2)

> **Important:** The following page discusses MongoDB Extended JSON v2. For
discussion on the Legacy MongoDB Extended JSON v1, see
`/reference/mongodb-extended-json-v1`.
For supported data types in :binary:`~bin.mongosh`, see
:mongosh:`mongosh Data Types </reference/data-types/>`.

`JSON` can only directly represent a subset of the types supported by `BSON`. To preserve type information, MongoDB adds the following extensions to the JSON format.

- Canonical Mode
A string format that emphasizes type preservation at the expense of readability and interoperability. That is, conversion from canonical to BSON will generally preserve type information except in certain specific cases.

- Relaxed Mode
A string format that emphasizes readability and interoperability at the expense of type preservation. That is, conversion from relaxed format to BSON can lose type information.

Both formats conform to the [JSON RFC](http://www.json.org) and can be parsed by the various MongoDB drivers and tools.

## MongoDB Extended JSON v2 Usage

### Drivers

The following drivers support Extended JSON v2.0:

### Extended JSON Methods

MongoDB provides the following methods for Extended JSON:

For usage examples, see `ex-obj-conversions` below.

For additional details, see the documentation for:

- `MongoDB NodeJS Driver
<https://mongodb.github.io/node-mongodb-native/4.0/>`__

- [BSON Parser](https://github.com/mongodb-js/bson-ext)_
- [BSON-EXT Parser](https://github.com/mongodb-js/bson-ext)_
### MongoDB Database Tools

.. include:: /includes/extracts/4.2-changes-extended-json-v2.rst

## BSON Data Types and Associated Representations

The following presents some common BSON data types and the associated representations in Canonical and Relaxed.

The complete list is [here](https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md)_.

---------------------------------------------------

Where the array elements are as follows:

- `<elements>`
- Array elements use Extended JSON.
- To specify an empty array, omit the content `[ ]`.
---------------------------------------------------

Where the values are as follows:

- `"<payload>"`
- Base64 encoded (with padding as "=") payload string.
- `"<t>"`
- A one- or two-character hex string that corresponds to a BSON binary
subtype. See the extended bson documentation http://bsonspec.org/spec.html for subtypes available.

---------------------------------------------------

For dates between years 1970 and 9999, inclusive:

For dates before year 1970 or after year 9999:

Where the values are as follows:

- `"<millis>"`
- A 64-bit signed integer as string. The value represents milliseconds
relative to the epoch.

- `"<ISO-8601 Date/Time Format>"`
- A date in `ISO-8601 Internet Date/Time Format
<https://tools.ietf.org/html/rfc3339#section-5.6>`__ as string.

- The date/time has a maximum time precision of milliseconds:
- Fractional seconds have exactly 3 decimal places if the fractional
part is non-zero.

- Otherwise, fractional seconds SHOULD be omitted if zero.
---------------------------------------------------

Where the values are as follows:

- `"<number>"`
- A `high-precision decimal
<https://github.com/mongodb/specifications/blob/master/source/bson-decimal128/decimal128.rst>`_ as a string.

---------------------------------------------------

Where the document contents are as follows:

- `<content>`
- Name:value pairs that use Extended JSON.
- To specify an empty document, omit the content `{ }`.
---------------------------------------------------

For finite numbers:

For infinite numbers or NAN:

Where the values are as follows:

- `"<decimal string>"`
- A 64-bit signed floating point as a string.
- `<non-integer number>`
- A non-integer number. Integer numbers are parsed as an integer
instead of a double.

---------------------------------------------------

Where the values are as follows:

- `"<number>"`
- A 64-bit signed integer as string.
- `<integer>`
- A 64-bit signed integer.
---------------------------------------------------

Where the values are as follows:

- `"<number>"`
- A 32-bit signed integer as a string.
- `<integer>`
- A 32-bit signed integer.
---------------------------------------------------

The MaxKey BSON data type compares higher than all other types. See `faq-dev-compare-order-for-BSON-types` for more information on comparison order for BSON types.

---------------------------------------------------

The MinKey BSON data type compares lower than all other types. See `faq-dev-compare-order-for-BSON-types` for more information on comparison order for BSON types.

---------------------------------------------------

Where the values are as follows:

- `"<ObjectId bytes>"`
- A 24-character, big-endian hexadecimal string that represents the
ObjectId bytes.

---------------------------------------------------

Where the values are as follows:

- `"<regexPattern>"`
- A string that corresponds to the regular expression pattern. The
string can contain valid JSON characters and unescaped double quote (`"`) characters, but may not contain unescaped forward slash (`/`) characters.

- `"<options>"`
- A string that specifies BSON regular expression options. You must specify
the options in alphabetical order. For information on the supported options, see :query:`$options`.

---------------------------------------------------

Where the values are as follows:

- `<t>`
- A positive integer for the seconds since epoch.
- `<i>`
- A positive integer for the increment.
## Examples

.. include:: /includes/sample-data-usage.rst

The following examples illustrate Extended JSON usage.

### Type Representations

### Extended JSON Object Conversions

The following short examples retrieve a document object and then convert the object to different forms using Extended JSON object conversion methods.

EJSON.serialize ```````````````

Serialize the data stored in a MongoDB document object. :binary:`mongosh` parses a JavaScript object and returns values using `"$"` prefixed `types <type-representations>`:

EJSON.deserialize `````````````````

Deserialize a serialized object. :binary:`mongosh` parses a JavaScript object and returns values using the default :binary:`mongosh` `type <type-representations>` form:

EJSON.stringify ```````````````

Convert an object to a string. :binary:`mongosh` outputs the elements of the converted object as strings:

EJSON.parse ```````````

Parse a string to create an object. :binary:`mongosh` returns the converted strings as documents:
