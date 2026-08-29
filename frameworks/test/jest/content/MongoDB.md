---
type: "Framework Learn Page"
framework: "Jest"
source_repo: "https://github.com/jestjs/jest"
source_branch: "main"
source_path: "docs/MongoDB.md"
source_commit: "be425a0b0e3bd60a74e4a7e350aa38c63a2d25ef"
source_commit_short: "be425a0"
source_commit_date: "2026-08-28T13:51:49+02:00"
generated_at: "2026-08-29T09:40:10.456155Z"
---
# Mongodb

---
id: mongodb
title: Using with MongoDB
---

With the [Global Setup/Teardown](Configuration.md#globalsetup-string) and [Async Test Environment](Configuration.md#testenvironment-string) APIs, Jest can work smoothly with [MongoDB](https://www.mongodb.com/).

## Use jest-mongodb Preset

[Jest MongoDB](https://github.com/shelfio/jest-mongodb) provides all required configuration to run your tests using MongoDB.

1.  First install `@shelf/jest-mongodb`

```bash npm2yarn
npm install --save-dev @shelf/jest-mongodb
```

2.  Specify preset in your Jest configuration:

```json
{
  "preset": "@shelf/jest-mongodb"
}
```

3.  Write your test

```js
const {MongoClient} = require('mongodb');

describe('insert', () => {
  let connection;
  let db;

  beforeAll(async () => {
    connection = await MongoClient.connect(globalThis.__MONGO_URI__, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    db = await connection.db(globalThis.__MONGO_DB_NAME__);
  });

  afterAll(async () => {
    await connection.close();
  });

  it('should insert a doc into collection', async () => {
    const users = db.collection('users');

    const mockUser = {_id: 'some-user-id', name: 'John'};
    await users.insertOne(mockUser);

    const insertedUser = await users.findOne({_id: 'some-user-id'});
    expect(insertedUser).toEqual(mockUser);
  });
});
```

There's no need to load any dependencies.

See [documentation](https://github.com/shelfio/jest-mongodb) for details (configuring MongoDB version, etc).
