---
type: "Framework Learn Page"
framework: "jest"
source_repo: "https://github.com/jestjs/jest"
source_branch: "main"
source_path: "docs/DynamoDB.md"
source_commit: "1865dd8659f5131715c780fa92f40623fce2f9c9"
source_commit_short: "1865dd86"
source_commit_date: "2026-06-21T13:50:36+02:00"
generated_at: "2026-06-21T11:51:37Z"
---

---
id: dynamodb
title: Using with DynamoDB
---

With the [Global Setup/Teardown](Configuration.md#globalsetup-string) and [Async Test Environment](Configuration.md#testenvironment-string) APIs, Jest can work smoothly with [DynamoDB](https://aws.amazon.com/dynamodb/).

## Use jest-dynamodb Preset

[Jest DynamoDB](https://github.com/shelfio/jest-dynamodb) provides all required configuration to run your tests using DynamoDB.

1.  First, install `@shelf/jest-dynamodb`

```bash npm2yarn
npm install --save-dev @shelf/jest-dynamodb
```

2.  Specify preset in your Jest configuration:

```json
{
  "preset": "@shelf/jest-dynamodb"
}
```

3.  Create `jest-dynamodb-config.js` and define DynamoDB tables

See [Create Table API](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB.html#createTable-property)

```js
module.exports = {
  tables: [
    {
      TableName: `files`,
      KeySchema: [{AttributeName: 'id', KeyType: 'HASH'}],
      AttributeDefinitions: [{AttributeName: 'id', AttributeType: 'S'}],
      ProvisionedThroughput: {ReadCapacityUnits: 1, WriteCapacityUnits: 1},
    },
    // etc
  ],
};
```

4.  Configure DynamoDB client

```js
const {DocumentClient} = require('aws-sdk/clients/dynamodb');

const isTest = process.env.JEST_WORKER_ID;
const config = {
  convertEmptyValues: true,
  ...(isTest && {
    endpoint: 'localhost:8000',
    sslEnabled: false,
    region: 'local-env',
  }),
};

const ddb = new DocumentClient(config);
```

5.  Write tests

```js
it('should insert item into table', async () => {
  await ddb
    .put({TableName: 'files', Item: {id: '1', hello: 'world'}})
    .promise();

  const {Item} = await ddb.get({TableName: 'files', Key: {id: '1'}}).promise();

  expect(Item).toEqual({
    id: '1',
    hello: 'world',
  });
});
```

There's no need to load any dependencies.

See [documentation](https://github.com/shelfio/jest-dynamodb) for details.
