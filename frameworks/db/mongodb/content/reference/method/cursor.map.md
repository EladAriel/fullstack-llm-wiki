---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.map.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.990635Z"
---
# cursor.map() (mongosh method)

**meta:** :description: Apply a function to each document in a cursor and collect results using `cursor.map()` in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** cursor.map(function)

   .. include:: /includes/fact-mongosh-shell-method.rst

   Applies a ``function`` to each document visited by the cursor and
   collects the return values from successive applications of the
   ``function`` into a ``Cursor`` object.

   The :method:`cursor.map()` method has the following parameter:

   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``function``
   
        - function
   
        - A function to apply to each document visited by the cursor.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst

## Behavior

:method:`cursor.map()` returns a ``Cursor`` object. Note that
``.map()`` only converts the type, it does not create a new cursor. You
can convert the ``Cursor`` object to an ``Array`` with ``.toArray()``.  

## Examples

These examples refer to the products collection:

.. code-block:: javascript

   db.products.insertMany([ 
      { _id: 1, name: 'widget', price: 10.89 },
      { _id: 2, name: 'thing', price: 11.24 },
      { _id: 3, name: 'moppet', price: 8 },
      { _id: 4, name: 'cosa', price: 24.19 }
   ])

### Return a Value From a Collection

Get the product names.

.. code-block:: javascript

   db.products.find().map( function(p) { return p.name; } ) ;

### Return Results as an ``Array``

Calculate a discounted sale price and return the results as an array. 

.. code-block:: javascript

   var salePrices = db.products.find().map( function(p) { return p.price * .9 } ).toArray() ;

Confirm that the output is an ``Array``

.. code-block:: javascript

   salePrices.constructor.name

**seealso:** :method:`cursor.forEach()` for similar functionality.