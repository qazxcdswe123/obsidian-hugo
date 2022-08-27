---
aliases: [npm, yarn, pnpm]
---
# Package Manager

## npm
`npm config set registry https://registry.npmmirror.com`

## pnpm
`pnpm setup`
`pnpm config set registry https://registry.npmmirror.com`

## parameters
- `-g`
the `-g` flag is a shorthand for the `global` configuration which sets the package install location to the folder where you installed NodeJS.
This is useful when you need to run the package from the command line instead of using `require()` and import it to your code.

- `-S`
The `S` option is the Save option in npm. It adds the npm package to your dependencies for your project. You can also add the dependency manually by editing the package.json file.

- `-D`
To remove a dev dependency, you need to attach the `-D` or `--save-dev` flag to the npm uninstall, and then specify the name of the package.