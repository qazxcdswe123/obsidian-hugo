## Web Extension
- [Web Extensions | Visual Studio Code Extension API](https://code.visualstudio.com/api/extension-guides/web-extensions)
- [[Web Worker]]

### Limitations
- Importing or requiring other modules is not supported. `importScripts` is not available as well. As a consequence, the code must be packaged to a single file.
- The [VS Code API](https://code.visualstudio.com/api/references/vscode-api) can be loaded via the pattern `require('vscode')`. This will work because there is a shim for `require`, but this shim cannot be used to load additional extension files or additional node modules. It only works with `require('vscode')`.
- Node.js globals and libraries such as `process`, `os`, `setImmediate`, `path`, `util`, `url` are not available at runtime. They can, however, be added with tools like webpack. The [webpack configuration](https://code.visualstudio.com/api/extension-guides/web-extensions#webpack-configuration) section explains how this is done.
- The opened workspace or folder is on a virtual file system. Access to workspace files needs to go through the VS Code [file system](https://code.visualstudio.com/api/references/vscode-api#FileSystem) API accessible at `vscode.workspace.fs`.
- [Extension context](https://code.visualstudio.com/api/references/vscode-api#ExtensionContext) locations (`ExtensionContext.extensionUri`) and storage locations (`ExtensionContext.storageUri`, `globalStorageUri`) are also on a virtual file system and need to go through `vscode.workspace.fs`.
- For accessing web resources, the [Fetch](https://developer.mozilla.org/docs/Web/API/Fetch_API) API must be used. Accessed resources need to support [Cross-Origin Resource Sharing](https://developer.mozilla.org/docs/Web/HTTP/CORS) (CORS)
- Creating child processes or running executables is not possible. However, web workers can be created through the [Worker](https://developer.mozilla.org/en-US/docs/Web/API/Worker) API. This is used for running language servers as described in the [Language Server Protocol in web extensions](https://code.visualstudio.com/api/extension-guides/web-extensions#language-server-protocol-in-web-extensions) section.
- As with regular extensions, the extension's `activate/deactivate` functions need to be exported via the pattern `exports.activate = ...`.
