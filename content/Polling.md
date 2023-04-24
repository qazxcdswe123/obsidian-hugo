---
aliases: []
date created: Mar 17th, 2023
date modified: Apr 20th, 2023
---

## Short Polling
Short polling is based on a timer and updates data at fixed intervals of time, it involves the client repeatedly sending requests to the server to check for new data

## Long Polling
1. A request is sent to the server.
2. The server doesn’t close the connection until it has a message to send.
3. When a message appears – the server responds to the request with it.
4. The browser makes a new request immediately.
Long polling works great in situations when messages are rare.

- Used in [[JavaScript]]
- See also: webhook, [Websocket](https://javascript.info/websocket) and [Server Sent Events](https://javascript.info/server-sent-events).
