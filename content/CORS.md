---
aliases: [Cross-Origin Resource Sharing]
tags: []
date created: Mar 13th, 2023
date modified: Mar 13th, 2023
---
## What
**Cross-Origin Resource Sharing** ([CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)) is an [HTTP](https://developer.mozilla.org/en-US/docs/Glossary/HTTP)-header based mechanism that allows a server to indicate any [origins](https://developer.mozilla.org/en-US/docs/Glossary/Origin) (domain, scheme, or port) other than its own from which a browser should permit loading resources.
CORS also relies on a mechanism by which browsers make a "preflight" request to the server hosting the cross-origin resource, in order to check that the server will permit the actual request. In that preflight, the browser sends headers that indicate the HTTP method and headers that will be used in the actual request.

![image.png](https://img.ynchen.me/2023/03/ae9065b63b7179eda0dcdad5608cad58.webp)

### Preflight
A CORS preflight request is a [CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS) request that checks to see if the CORS protocol is understood and a server is aware using specific methods and headers.

## Links
- [Cross-origin resource sharing - Wikipedia](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
- [cors - npm](https://www.npmjs.com/package/cors)
- [Preflight request - MDN Web Docs Glossary: Definitions of Web-related terms | MDN](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request)