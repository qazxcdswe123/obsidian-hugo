---
aliases:
tags: 
date created: Apr 3rd, 2022
date modified: Mar 14th, 2023
---

## `GET`
Two commands supported by HTTP include **GET** and **POST**.  
GET allows a browser to ask for a page or file in a URL, and POST allows a browser to send additional data to the server that is hidden from the URL. Both of these are **requests** we can make to a server, which will provide a **response** in return.

[[HTTP Headers]]

## `POST`
- `application/x-www-form-urlencoded`: the keys and values are encoded in key-value tuples separated by `'&'`, with a `'='` between the key and the value. Non-alphanumeric characters in both keys and values are [URL encoded](https://en.wikipedia.org/wiki/URL_encoding): this is the reason why this type is not suitable to use with binary data (use `multipart/form-data` instead)
- `multipart/form-data`: each value is sent as a block of data ("body part"), with a user agent-defined delimiter ("boundary") separating each part. The keys are given in the `Content-Disposition` header of each part.
- `text/plain`  
[POST - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)

## `PATCH`
The **HTTP `PATCH` request method** applies partial modifications to a resource.

## `HEAD`
The `HEAD` method asks for a response identical to a `GET` request, but without the response body.

## Links
- [[WebSocket]]
- [HTTP request methods - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)