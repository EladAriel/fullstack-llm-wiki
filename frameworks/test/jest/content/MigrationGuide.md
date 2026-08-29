---
type: "Framework Learn Page"
framework: "Jest"
source_repo: "https://github.com/jestjs/jest"
source_branch: "main"
source_path: "docs/MigrationGuide.md"
source_commit: "be425a0b0e3bd60a74e4a7e350aa38c63a2d25ef"
source_commit_short: "be425a0"
source_commit_date: "2026-08-28T13:51:49+02:00"
generated_at: "2026-08-29T09:40:10.454071Z"
---
# Migrationguide

---
id: migration-guide
title: Migrating to Jest
---

If you'd like to try out Jest with an existing codebase, there are a number of ways to convert to Jest:

- If you are using Jasmine, or a Jasmine like API (for example [Mocha](https://mochajs.org)), Jest should be mostly compatible, which makes it less complicated to migrate to.
- If you are using AVA, Expect.js (by Automattic), Jasmine, Mocha, proxyquire, Should.js or Tape you can automatically migrate with Jest Codemods (see below).
- If you like [chai](http://chaijs.com/), you can upgrade to Jest and continue using chai. However, we recommend trying out Jest's assertions and their failure messages. Jest Codemods can migrate from chai (see below).

## jest-codemods

If you are using [AVA](https://github.com/avajs/ava), [Chai](https://github.com/chaijs/chai), [Expect.js (by Automattic)](https://github.com/Automattic/expect.js), [Jasmine](https://github.com/jasmine/jasmine), [Mocha](https://github.com/mochajs/mocha), [proxyquire](https://github.com/thlorenz/proxyquire), [Should.js](https://github.com/shouldjs/should.js), [Tape](https://github.com/substack/tape), or [Sinon](https://sinonjs.org/) you can use the third-party [jest-codemods](https://github.com/skovhus/jest-codemods) to do most of the dirty migration work. It runs a code transformation on your codebase using [jscodeshift](https://github.com/facebook/jscodeshift).

To transform your existing tests, navigate to the project containing the tests and run:

```bash
npx jest-codemods
```

More information can be found at [https://github.com/skovhus/jest-codemods](https://github.com/skovhus/jest-codemods).
