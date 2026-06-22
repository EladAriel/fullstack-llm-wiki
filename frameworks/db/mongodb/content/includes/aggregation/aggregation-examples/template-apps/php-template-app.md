---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/aggregation/aggregation-examples/template-apps/php-template-app.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Before you begin following this aggregation tutorial, you must set up a new PHP app. You can use this app to connect to a MongoDB deployment, insert sample data into MongoDB, and run the aggregation pipeline.

> **Tip:** To learn how to install the PHP library and connect to MongoDB,
see the `Get Started with the PHP Library
<https://www.mongodb.com/docs/php-library/current/get-started/>`__
tutorial.
To learn more about performing aggregations in the PHP library, see the
`Aggregation guide
<https://www.mongodb.com/docs/php-library/current/aggregation/>`__.

After you install the library, create a file called `agg_tutorial.php`. Paste the following code in this file to create an app template for the aggregation tutorials.

> **Important:** In the following code, read the code comments to find the sections of
the code that you must modify for the tutorial you are following.
If you attempt to run the code without making any changes, you will
encounter a connection error.

```php
<?php

require 'vendor/autoload.php';

// Modify imports for each tutorial as needed.
use MongoDB\Client;
use MongoDB\BSON\UTCDateTime;
use MongoDB\Builder\Pipeline;
use MongoDB\Builder\Stage;
use MongoDB\Builder\Type\Sort;
use MongoDB\Builder\Query;
use MongoDB\Builder\Expression;
use MongoDB\Builder\Accumulator;

use function MongoDB\object;

// Replace the placeholder with your connection string.
$uri = '<connection string>';
$client = new Client($uri);

// Get a reference to relevant collections.
// ... $someColl = $client->agg_tutorials_db->someColl;
// ... $anotherColl = $client->agg_tutorials_db->anotherColl;

// Delete any existing documents in collections if needed.
// ... $someColl->deleteMany([]);

// Insert sample data into the collection or collections.
// ... $someColl->insertMany(...);

// Add code to create pipeline stages within the Pipeline instance.
// ... $pipeline = new Pipeline(...);

// Run the aggregation.
// ... $cursor = $someColl->aggregate($pipeline);

// Print the aggregation results.
foreach ($cursor as $doc) {
    echo json_encode($doc, JSON_PRETTY_PRINT), PHP_EOL;
}
```

For every tutorial, you must replace the connection string placeholder with your deployment's connection string.

> **Tip:** To learn how to locate your deployment's connection string, see the
[Create a Connection String](https://www.mongodb.com/docs/php-library/current/get-started/#create-a-connection-string)_
step of the Get Started with the PHP Library tutorial.

For example, if your connection string is `"mongodb+srv://mongodb-example:27017"`, your connection string assignment resembles the following:

```php
$uri = 'mongodb+srv://mongodb-example:27017';
```
