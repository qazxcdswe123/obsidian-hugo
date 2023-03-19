## Bug
```
Error: Error while loading rule '@typescript-eslint/dot-notation': You have used a rule which requires parserServices to be generated. You must therefore provide a value for the "parserOptions.project" property for @typescript-eslint/parser.
```

Add `"parserOptions": { "project": ["tsconfig.json"] }` to `.eslintrc.cjs`