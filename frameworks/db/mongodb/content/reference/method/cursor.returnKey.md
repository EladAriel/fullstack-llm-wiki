---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.returnKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# cursor.returnKey() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

If the query does not use an index to perform the read operation, the cursor returns empty documents.

## Example

The `restaurants` collection contains documents with the following schema:

```javascript
db.restaurants.insertOne( 
   {
      _id: ObjectId("564f3a35b385149fc7e3fab9"),
      address: {
         building: "2780",
         coord: [
            -73.98241999999999,
            40.579505
         ],
         street: "Stillwell Avenue",
         zipcode: "11224"
      },
      borough: "Brooklyn",
      cuisine: "American ",
      grades: [
         {
            date: ISODate("2014-06-10T00:00:00Z"),
            grade: "A",
            score: 5
         },
         {
            date: ISODate("2013-06-05T00:00:00Z"),
            grade: "A",
            score: 7
         }
      ],
      name: "Riviera Caterer",
      restaurant_id: "40356018"
   }
)
```

The collection has two indexes in addition to the default `_id` index:

```javascript
{
   "v" : 1,
   "key" : {
      "_id" : 1
   },
   "name" : "_id_",
   "ns" : "guidebook.restaurant"
},
{
   "v" : 1,
   "key" : {
      "cuisine" : 1
   },
   "name" : "cuisine_1",
   "ns" : "guidebook.restaurant"
},
{
   "v" : 1,
   "key" : {
      "_fts" : "text",
      "_ftsx" : 1
   },
   "name" : "name_text",
   "ns" : "guidebook.restaurant",
   "weights" : {
      "name" : 1
   },
   "default_language" : "english",
   "language_override" : "language",
   "textIndexVersion" : 3
}
```

The following code uses the :method:`cursor.returnKey()` method to return only the indexed fields used for executing the query:

```javascript
var csr = db.restaurant.find( { "cuisine" : "Japanese" } )
csr.returnKey()
```

This returns the following:

```javascript
{ "cuisine" : "Japanese" }
{ "cuisine" : "Japanese" }
{ "cuisine" : "Japanese" }
{ "cuisine" : "Japanese" }
...
```
