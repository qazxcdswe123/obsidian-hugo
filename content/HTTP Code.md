---
aliases: []
date created: Apr 19th, 2022
date modified: Aug 27th, 2022
---
- [HTTP response status codes - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

- `200 OK`
- `301 Moved Permanently`
- `302 Found`
- `304 Not Modified`
- `307 Temporary Redirect`
- `401 Unauthorized`
- `403 Forbidden`
- `404 Not Found`
- `429 Too Many Requests`
	- The response may include a Retry-After header that indicates how long to wait before making a new request.
	- [[Exponential backoff]]
- `500 Internal Server Error`
	- Buggy code on a server might result in this status code, like segfaults we might have seen in C.
- `503 Service Unavailable`  