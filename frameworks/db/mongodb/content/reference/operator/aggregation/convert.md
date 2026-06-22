---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/convert.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $convert (expression operator)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

.. versionchanged:: 8.3

```javascript
{
   $convert:
      {
         input: <expression>,
         to: <type expression> || {
            type: <type expression>,
            subtype: <int>
         },
         base: <expression>,       // new in 8.3
         format: <string>,
         onError: <expression>,
         onNull: <expression>
      }
}
```

`$convert` takes a document with the following fields:

In addition to :expression:`$convert`, MongoDB provides the following aggregation operators as shorthand when the default "onError" and "onNull" behavior is acceptable:

- :expression:`$toArray`
- :expression:`$toBool`
- :expression:`$toDate`
- :expression:`$toDecimal`
- :expression:`$toDouble`
- :expression:`$toInt`
- :expression:`$toLong`
- :expression:`$toObject`
- :expression:`$toObjectId`
- :expression:`$toString`
- :expression:`$toUUID`
### Type Identifiers

The `to.type` field accepts the following numeric and string identifiers:

### Binary Subtypes

The following table lists the valid values for the `to.subtype` field:

.. include:: /includes/binary-subtypes.rst

## Behavior

The following sections describe how to convert values to different types.

### Convert to BinData

.. include:: /includes/binData-numeric-input.rst

.. include:: /includes/convert-subtype.rst

Convert from numeric types to `binData`: ``````````````````````````````````````````

When converting a numeric type to `binData`:

- An `int` becomes a 4-byte `binData`.
- A `long` becomes an 8-byte `binData`.
- A `double` becomes an 8-byte `binData`.
The `byteOrder` of the numeric output defaults to "little", or the placement of the least significant byte first. In contrast, "big" places the most significant byte first.

Convert `long` to `binData`:

**Input:**

**Output**:

Convert `long` to `binData` with big-endian byte ordering:

**Input:**

**Output**:

Convert `double` to `binData`:

**Input:**

**Output**:

Convert `int` to `binData`:

**Input:**

**Output**:

Convert an array of numeric values to `binData`:

This example shows how `$convert` converts arrays containing different types of numeric values into `binData`.

**Input:**

**Output**:

Convert from string to BinData ``````````````````````````````

MongoDB also supports conversions between `binData` and strings.

The following examples demonstrate how to convert strings to binData.

> **Note:** .. include:: /includes/convert-subtype.rst

### Convert to Array

.. versionadded:: 8.3

The following table lists the input types that can be converted to an array:

.. include:: /includes/table-toArray-input-types.rst

The following table lists some conversion of string to array examples:

Convert binData to Array `````````````````````````

This example shows how `$convert` converts `binData` of different formats into arrays containing values of their respective types:

**Input**:

**Output**:

### Convert to Object

.. versionadded:: 8.3

The following table lists the input types that can be converted to an object:

.. include:: /includes/table-toObject-input-types.rst

The following table lists some conversion to object examples:

### Convert to Boolean

The following table lists the input types that can be converted to a boolean:

.. include:: /includes/aggregation/convert-to-bool-table.rst

The following table lists some conversion to boolean examples:

### Convert to Integer

The following table lists the input types that can be converted to an integer:

The following table lists some conversion to integer examples:

### Convert to Decimal

The following table lists the input types that can be converted to a decimal:

The following table lists some conversion to decimal examples:

### Convert to Double

The following table lists the input types that can be converted to a double:

The following table lists some conversion to double examples:

### Subnormal Numbers

.. include:: /includes/fact-float-parse-behavior-8.3.rst

### Convert to Long

The following table lists the input types that can be converted to a long:

The following table lists some conversion to long examples:

### Convert to Date

The following table lists the input types that can be converted to a date:

The following table lists some conversion to date examples:

### Convert to ObjectId

The following table lists the input types that can be converted to an ObjectId:

The following table lists some conversion to date examples:

### Convert to String

.. include:: /includes/convert-string-types.rst

> **Note:** When you specify `base` and the `input` is a numeric type,
:expression:`$convert` returns the string representation of the
integer value in that base. Base conversion for strings is only
supported for integer values, otherwise :expression:`$convert`
returns a conversion error unless you specify `onError`.

The following table lists some conversion to string examples:

## Examples

### Base Conversion Example

Create a collection `examples` with a placeholder document:

```javascript
db.examples.insertOne({ _id: 1 })
```

The following example converts between numbers and strings using different bases:

```javascript
db.examples.aggregate([
  {
    $project: {
      _id: 0,
      bin:        { $convert: { input: 10,    to: "string", base: 2  } },
      hex:        { $convert: { input: 10,    to: "string", base: 16 } },
      intFromBin: { $convert: { input: "1010", to: "int",   base: 2  } },
      intFromHex: { $convert: { input: "A",    to: "int",   base: 16 } }
    }
  }
])
```

This operation returns the following document:

```javascript
{
  bin: "1010",
  hex: "A",
  intFromBin: 10,
  intFromHex: 10
}
```

### Type Conversion Example

Create a collection `orders` with the following documents:

```javascript
db.orders.insertMany( [
   { _id: 1, item: "apple", qty: 5, price: 10 },
   { _id: 2, item: "pie", qty: 10, price: Decimal128("20.0") },
   { _id: 3, item: "ice cream", qty: 2, price: "4.99" },
   { _id: 4, item: "almonds" },
   { _id: 5, item: "bananas", qty: 5000000000, price: Decimal128("1.25") }
] )
```

The following aggregation operation on the `orders` collection converts the `price` to a decimal:

```javascript
// Define stage to add convertedPrice and convertedQty fields with
//    the converted price and qty values.
// If price or qty values are missing, the conversion returns a
//    value of decimal value or int value of 0.
// If price or qty values cannot be converted, the conversion returns
//    a string

priceQtyConversionStage = { 
   $addFields: { 
      convertedPrice: { $convert:
         {
            input: "$price",
            to: "decimal",
            onError: "Error",
            onNull: Decimal128("0")
         } },
      convertedQty: { $convert:
         { 
            input: "$qty",
            to: "int", 
            onError:{ $concat:
               [
                  "Could not convert ",
                  { $toString:"$qty" },
                  " to type integer."
               ]
            },
         onNull: Int32("0") 
      } },
   }
};

totalPriceCalculationStage = { 
   $project: { totalPrice: {
     $switch: {
        branches: [
          { case:
             { $eq: [ { $type: "$convertedPrice" }, "string" ] },
             then: "NaN"
          },
          { case:
             { $eq: [ { $type: "$convertedQty" }, "string" ] },
             then: "NaN"
          },
        ],
        default: { $multiply: [ "$convertedPrice", "$convertedQty" ] }
     }
} } };

db.orders.aggregate( [
   priceQtyConversionStage,
   totalPriceCalculationStage
])
```

The operation returns the following documents:

```javascript
{ _id: 1, totalPrice: Decimal128("50") },
{ _id: 2, totalPrice: Decimal128("200.0") },
{ _id: 3, totalPrice: Decimal128("9.98") },
{ _id: 4, totalPrice: Decimal128("0") },
{ _id: 5, totalPrice: 'NaN' }
```

> **Note:** These examples use :binary:`mongosh`. The default types are
different in the legacy :binary:`mongo` shell.

## Learn More

- Convert a value to an array with :expression:`$toArray`
- Convert a string to an object with :expression:`$toObject`
- Convert a value to a boolean with :expression:`$toBool`
- Convert a value to an integer with :expression:`$toInt`
- Convert a value to a decimal with :expression:`$toDecimal`
- Convert a value to a double with :expression:`$toDouble`
- Convert a value to a long with :expression:`$toLong`
- Convert a value to a date with :expression:`$toDate`
- Convert a value to an ObjectId with :expression:`$toObjectId`
- Convert a value to a string with :expression:`$toString`
- Convert a date string to a date object with :expression:`$dateFromString`
- Convert a date object to a string with :expression:`$dateToString`
