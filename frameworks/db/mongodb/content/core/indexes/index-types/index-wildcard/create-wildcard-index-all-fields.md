---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/indexes/index-types/index-wildcard/create-wildcard-index-all-fields.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# Create a Wildcard Index on All Fields

You can create a wildcard index that supports queries on all possible document fields. Wildcard indexes support queries on arbitrary or unknown field names.

To create a wildcard index on all fields (excluding `_id`), use the wildcard specifier (`$**`) as the index key:

```javascript
db.<collection>.createIndex( { "$**": <sortOrder> } )
```

## About this Task

.. include:: /includes/indexes/wildcard-use-case-warning.rst

## Before You Begin

Create an `artwork` collection that contains the following documents:

```javascript
db.artwork.insertMany( [
   {
      "name": "The Scream",
      "artist": "Edvard Munch",
      "style": "modern",
      "themes": [ "humanity", "horror" ]
   },
   {
      "name": "Acrobats",
      "artist": {
         "name": "Raoul Dufy",
         "nationality": "French",
         "yearBorn": 1877
      },
      "originalTitle": "Les acrobates",
      "dimensions": [ 65, 49 ] 
   },
   {
      "name": "The Thinker",
      "type": "sculpture",
      "materials": [ "bronze" ],
      "year": 1904
   }
] )
```

Each document contains details about the artwork. The field names vary between documents depending on the information available about the piece.

## Procedure

The following operation creates a wildcard index on all document fields in the `artwork collection (excluding id`):

```javascript
db.artwork.createIndex( { "$**" : 1 } )
```

## Results

This index supports single-field queries on any field in the collection. If a document contains an embedded document or array, the wildcard index traverses the document or array and stores the value for all fields in the document or array.

For example, the index supports the following queries:

- Query:
```javascript
  db.artwork.find( { "style": "modern" } )

Output:

.. code-block:: javascript
  :copyable: false

  [
     {
        _id: ObjectId("6352c401b1fac2ee2e957f09"),
        name: 'The Scream',
        artist: 'Edvard Munch',
        style: 'modern',
        themes: [ 'humanity', 'horror' ]
     }
  ]
```

- Query:
```javascript
  db.artwork.find( { "artist.nationality": "French" } )

Output:

.. code-block:: javascript
  :copyable: false

  [
     {
        _id: ObjectId("6352c525b1fac2ee2e957f0d"),
        name: 'Acrobats',
        artist: { name: 'Raoul Dufy', nationality: 'French', yearBorn: 1877 },
        originalTitle: 'Les acrobates',
        dimensions: [ 65, 49 ]
     }
  ]
```

- Query:
```javascript
  db.artwork.find( { "materials": "bronze" } )

Output:

.. code-block:: javascript
  :copyable: false

  [
     {
        _id: ObjectId("6352c387b1fac2ee2e957f08"),
        name: 'The Thinker',
        type: 'sculpture',
        materials: [ 'bronze' ],
        year: 1904
     }
  ]
```

## Learn More

To learn how to create a wildcard index that projects specific fields to cover, see the following pages:

- `wc-compound-index-wcProject`
- `create-wildcard-index-multiple-fields`
To learn more about behaviors for wildcard indexes, see:

- `wildcard-index-embedded-object-behavior`
- `wildcard-index-restrictions`
