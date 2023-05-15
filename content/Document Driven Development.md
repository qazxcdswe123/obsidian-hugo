---
aliases: []
date created: Mar 24th, 2023
date modified: Mar 24th, 2023
---
### Documentation-Driven Development
The philosophy behind Documentation-Driven Development is a simple: **from the perspective of a user, if a feature is not documented, then it doesn't exist, and if a feature is documented incorrectly, then it's broken.**

- Document the feature _first_. Figure out how you're going to describe the feature to users; if it's not documented, it doesn't exist. Documentation is the best way to define a feature in a user's eyes.
- Whenever possible, documentation should be reviewed by users (community or Spark Elite) before any development begins.
- Once documentation has been written, development should commence, and test-driven development is preferred.
- Unit tests should be written that test the features as described by the documentation. If the functionality ever comes out of alignment with the documentation, tests should fail.
- When a feature is being modified, it should be modified documentation-first.
- When documentation is modified, so should be the tests.
- Documentation and software should both be versioned, and versions should match, so someone working with old versions of software should be able to find the proper documentation.

So, the preferred order of operations for new features:
- Write documentation
- Get feedback on documentation
- Test-driven development (where tests align with documentation)
- Push features to staging
- Functional [[testing]] on staging, as necessary
- Deliver feature
- Publish documentation
- Increment versions
