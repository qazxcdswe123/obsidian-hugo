---
link: []
aliases: [keep-alive]
date created: Mar 17th, 2023
date modified: Oct 9th, 2023
---
Use a single [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol "Transmission Control Protocol") connection to send and receive multiple [HTTP requests](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol")/responses, as opposed to opening a new connection for every single request/response pair. 

The newer [HTTP/2](https://en.wikipedia.org/wiki/HTTP/2 "HTTP/2") protocol uses the same idea and takes it further to allow multiple concurrent requests/responses to be multiplexed over a single connection.

## Links
- [HTTP persistent connection - Wikipedia](https://en.wikipedia.org/wiki/HTTP_persistent_connection)