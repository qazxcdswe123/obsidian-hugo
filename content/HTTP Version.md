---
aliases: []
link: []
date created: Sep 16th, 2023
date modified: Oct 8th, 2023
---

## HTTP Version History
- HTTP/1.1
- HTTP/2
- HTTP/3

---

## HTTP 1
- RFC 1945
	- 1994
	- 60-page specification

---

## HTTP 1.1
- RFC 2616
	- 1996
	- 176 pages, with a lot of optional parts.
- Supports virtual hosting (a server with a single IP Address hosting multiple domains)
- [[HTTP Persistent Connection|keep-alive]]
	- Persistent Connections: decoupled the one-to-one relationship between TCP and HTTP
	- Multiplexing: send in bulk, read in queue, have head-of-line issue.
 - hard to update its protocol since every middle box has its own implementation

--

![image.png](https://img.ynchen.me/2023/10/53116d4cd31e191454d02d9c0d3e1129.webp)

--

![image.png](https://img.ynchen.me/2023/10/5e3017a6c68dce2534281252b517676a.webp)

--

```
GET / HTTP/1.1

Host: www.freebsd.org
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.7) Gecko/20050414 Firefox/1.0.3
Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 300
Connection: keep-alive
If-Modified-Since: Mon, 09 May 2005 21:01:30 GMT
If-None-Match: "26f731-8287-427fcfaa"
```

```
HTTP/1.1 200 OK

Date: Fri, 13 May 2005 05:51:12 GMT
Server: Apache/1.3.x LaHonda (Unix)
Last-Modified: Fri, 13 May 2005 05:25:02 GMT
ETag: "26f725-8286-42843a2e"
Accept-Ranges: bytes
Content-Length: 33414
Keep-Alive: timeout=15, max=100
Connection: Keep-Alive
Content-Type: text/html
```

---

## HTTP 2
- RFC 7540
	- May 15th 2015
- Binary Protocol
- Single TCP Connection
	- multiplexd
	- stream
- Header compression
- Do not require it to deliver in order
	- Prioritization
	- Dependency Tree
- Server Push

--

```
 +-----------------------------------------------+
 |                 Length (24)                   |
 +---------------+---------------+---------------+
 |   Type (8)    |   Flags (8)   |
 +-+-------------+---------------+-------------------------------+
 |R|                 Stream Identifier (31)                      |
 +=+=============================================================+
 |                   Frame Payload (0...)                      ...
 +---------------------------------------------------------------+
```

--

![image.png](https://img.ynchen.me/2023/10/ee89a2f3a820b20b11c6667724d54bd2.webp)

--

![image.png](https://img.ynchen.me/2023/10/a546327422aed8fcc872026b943ea6a0.webp)

--

```
curl --http2 https://www.example.com -I -v

HTTP/1.1 200 Connection established

* using HTTP/2
* h2 [:method: HEAD]
* h2 [:scheme: https]
* h2 [:authority: www.example.com]
* h2 [:path: /]
* h2 [user-agent: curl/8.1.2]
* h2 [accept: */*]
* Using Stream ID: 1 (easy handle 0x127012800)
> HEAD / HTTP/2
> Host: www.example.com
> User-Agent: curl/8.1.2
> Accept: */*

HTTP/2 200 
accept-ranges: bytes
age: 136909
cache-control: max-age=604800
content-type: text/html; charset=UTF-8
date: Sun, 08 Oct 2023 02:28:20 GMT
etag: "3147526947"
expires: Sun, 15 Oct 2023 02:28:20 GMT
last-modified: Thu, 17 Oct 2019 07:18:26 GMT
server: ECS (laa/7BA2)
x-cache: HIT
content-length: 1256
```

---

## HTTP 3
- RFC 9114
	- 2022
- [[QUIC]]
	- Encryption by default using [[TLS]]
	- middlebox agnostic
	- stream
	- no handshake required
		 - 0-RTT
	- mobile friendly
		- connection ID (wifi to mobile switch), aka connection migration

--

 ![image.png](https://img.ynchen.me/2023/10/0a878d68f19be53d731ab91ef29c6c18.webp)

--

![image.png](https://img.ynchen.me/2023/10/04cb80d831f5429a5facfa62b3150948.webp)

--

![image.png](https://img.ynchen.me/2023/10/5b30bc234ecff7b855c632fe6b687ffa.webp)


---

## Comparisons

--

### Similarities
- Both protocols offer server push support
- Both protocols have header compression, and QPACK and HPACK are similar in design.
- Both protocols offer multiplexing over a single connection using streams

--

### Differences
The differences are in the details and primarily there thanks to HTTP/3's use of QUIC:
- HTTP/3 has better and more likely to work early data support thanks to QUIC's 0-RTT handshakes, while TCP Fast Open and TLS usually sends less data and often faces problems.
- HTTP/3 has much faster handshakes thanks to QUIC vs TCP + TLS.
- HTTP/3 does not exist in an insecure or unencrypted version. HTTP/2 can be implemented and used without HTTPS - even if this is rare on the Internet.
- HTTP/2 can be negotiated directly in a TLS handshake with the ALPN extension, while HTTP/3 is over QUIC so it needs an `Alt-Svc:` header response first to inform the client about this fact.
- The base HTTP/3 specification doesn't define prioritization itself. The HTTP/2 approach to prioritization has been deemed too complicated and is deprecated by the latest revision of the HTTP/2 specification [RFC 9113](https://www.rfc-editor.org/rfc/rfc9113.html). A simpler alternative, the Extensible Prioritization Scheme for HTTP ([RFC 9218](https://www.rfc-editor.org/rfc/rfc9218.html)), has been published separately, which can be used in both HTTP/2 and HTTP/3.


## Links
- [Why HTTP/3 is eating the world | APNIC Blog](https://blog.apnic.net/2023/09/25/why-http-3-is-eating-the-world/)
- [[QUIC]]
- [English - HTTP/3 explained](https://http3-explained.haxx.se/en)
- [http2 explained - The HTTP/2 book](https://daniel.haxx.se/http2/)
