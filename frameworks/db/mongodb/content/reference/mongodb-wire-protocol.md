---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mongodb-wire-protocol.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/unicode-checkmark.rst

=====================

# MongoDB Wire Protocol

> **Note:** This MongoDB Wire Protocol Specification is licensed under a
`Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License
<https://creativecommons.org/licenses/by-nc-sa/3.0/us/>`__. You may
not use or adapt this material for any commercial purpose, such as
to create a commercial database or database-as-a-service offering.

## Introduction

The MongoDB Wire Protocol is a simple socket-based, request-response style protocol. Clients communicate with the database server through a regular TCP/IP socket.

## TCP/IP Socket

Clients should connect to the database with a regular TCP/IP socket.

### Port

The default port number for :binary:`~bin.mongod` and :binary:`~bin.mongos` instances is 27017. The port number for :binary:`~bin.mongod` and :binary:`~bin.mongos` is configurable and may vary.

### Byte Ordering

All integers in the MongoDB wire protocol use little-endian byte order: that is, least-significant byte first.

## Messages Types and Formats

MongoDB uses the `OP_MSG <wire-op-msg>` opcode for both client requests and database replies. There are several message formats used in older versions of MongoDB which have been deprecated in favor of `OP_MSG`.

> **Note:** This page uses a C-like `struct` to describe the message
structure.
The types used in this document, such as `int32` and `cstring`,
are the same as those defined in the `BSON specification
<http://bsonspec.org/#/specification>`_.

## Standard Message Header

In general, each message consists of a standard message header followed by request-specific data. The standard message header is structured as follows:

```c
struct MsgHeader {
    int32   messageLength; // total message size, including this
    int32   requestID;     // identifier for this message
    int32   responseTo;    // requestID from the original request
                           //   (used in responses from the database)
    int32   opCode;        // message type
}
```

## Opcodes

MongoDB uses these `opCode` values:

### `OP_COMPRESSED`

Any opcode can be compressed and wrapped in an `OP_COMPRESSED` header. The `OP_COMPRESSED` message contains the original compressed opcode message alongside the metadata necessary to process and decompress it.

The format of the `OP_COMPRESSED` message is:

```bash
struct {
    MsgHeader header;            // standard message header
    int32  originalOpcode;       // value of wrapped opcode
    int32  uncompressedSize;     // size of deflated compressedMessage, excluding MsgHeader
    uint8  compressorId;         // ID of compressor that compressed message
    char    *compressedMessage;  // opcode itself, excluding MsgHeader
}
```

Each compressor is assigned a predefined compressor ID as follows:

### `OP_MSG`

`OP_MSG` is an extensible message format used to encode both client requests and server replies on the wire.

`OP_MSG` has the following format:

```none
OP_MSG {
    MsgHeader header;           // standard message header
    uint32 flagBits;            // message flags
    Sections[] sections;        // data sections
    optional<uint32> checksum;  // optional CRC-32C checksum
}
```

Flag Bits `````````

The `flagBits` integer is a bitmask encoding flags that modify the format and behavior of `OP_MSG`.

The first 16 bits (0-15) are required and parsers **MUST** error if an unknown bit is set.

The last 16 bits (16-31) are optional, and parsers **MUST** ignore any unknown set bits. Proxies and other message forwarders **MUST** clear any unknown optional bits before forwarding messages.

Sections ````````

An `OP_MSG` message contains one or more sections. Each section starts with a `kind` byte indicating its type. Everything after the `kind` byte constitutes the section's payload.

The available kinds of sections follow.

Kind 0: Body ````````````

A body section is encoded as a **single** `BSON object <bson-types>`. The size in the BSON object also serves as the size of the section. This section kind is the standard command request and reply body.

All top-level fields **MUST** have a unique name.

Kind 1: Document Sequence `````````````````````````

Kind 2 ``````

This section is used for internal purposes.

Checksum ````````

Each message **MAY** end with a CRC-32C [#f1]_ checksum that covers all bytes in the message except for the checksum itself.

If you do not use TLS/SSL connections, :binary:`~bin.mongod` instances and :binary:`~bin.mongos` instances exchange messages with checksums.

If you use TLS/SSL connections, :binary:`~bin.mongod` instances and :binary:`~bin.mongos` instances skip the checksum.

Drivers and older binaries will ignore the checksum if presented with messages with checksum.

The presence of a checksum is indicated by the `checksumPresent` flag bit.

### Legacy Opcodes

Starting in MongoDB 5.1, these opcodes are removed in favor of `OP_MSG <wire-op-msg>`:

- `OP_DELETE`
- `OP_GET_MORE`
- `OP_INSERT`
- `OP_KILL_CURSORS`
- `OP_QUERY` [#op-query-footnote]_
- `OP_REPLY`
- `OP_UPDATE`
If you are running an older version of MongoDB and need detailed information on the previous opcodes, see `wire-legacy-opcodes`.

MongoDB 5.1 removes support for both `OP_QUERY` find operations and `OP_QUERY` commands. As an exception, `OP_QUERY` is still supported for running the :dbcommand:`hello` and `isMaster` commands as part of the connection handshake.

described by https://tools.ietf.org/html/rfc4960#page-140.

## Contents

- Legacy Opcodes </legacy-opcodes>
