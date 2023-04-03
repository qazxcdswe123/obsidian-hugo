---
aliases: []
date created: Mar 14th, 2023
date modified: Mar 14th, 2023
---
# ESBuild

## Bugs
```
app.js:1 Plugin failure: obsidian-sample-plugin TypeError: require_streams(...) is not a function
    at node_modules/iconv-lite/lib/index.js (VM229 plugin:obsidian-sample-plugin:4204:26)
    at __require (VM229 plugin:obsidian-sample-plugin:13:50)
    at node_modules/raw-body/index.js (VM229 plugin:obsidian-sample-plugin:4260:17)
    at __require (VM229 plugin:obsidian-sample-plugin:13:50)
    at node_modules/body-parser/lib/read.js (VM229 plugin:obsidian-sample-plugin:4615:19)
    at __require (VM229 plugin:obsidian-sample-plugin:13:50)
    at node_modules/body-parser/lib/types/json.js (VM229 plugin:obsidian-sample-plugin:13596:16)
    at __require (VM229 plugin:obsidian-sample-plugin:13:50)
    at loadParser (VM229 plugin:obsidian-sample-plugin:15893:20)
    at Function.get [as json] (VM229 plugin:obsidian-sample-plugin:15883:16)
```

Edit `esbuild.config.mjs` and add `platform: "node"`
