- [[Communication System]]
- [[ARP]]

# 4 Layer Internet Model
- Application Layer
	- Bi-directional reliable byte stream between two applications, using application-specific semantics (e.g. http, bit-torrent).
- Transport Layer
	- [[TCP]] and [[UDP]]
	- Guarantees correct, in-order delivery of data end-to-end. Controls congestion.
- Network Layer
	- No need to concern how [[Packet|packets]] are sent via link layer
	- Delivers datagrams end-to-end. Best-effort delivery -no guarantees. Must use the Internet Protocol ([[IP]]).
- Link Layer
	- Delivers data over a single link between an end host and router, or between routers

[[Packet]]

# 7 Layer OSI Model