# Network Model

## 4 Layer Internet Model
- Application Layer
	- Bi-directional reliable byte stream between two applications, using application-specific semantics (e.g. http, bit-torrent).
- Transport Layer
	- [[TCP]] and [[UDP]]
	- Guarantees correct, in-order delivery of data end-to-end. [[Congestion Control]]
- Network Layer
	- No need to concern how [[Packet|packets]] are sent via link layer
	- Delivers datagrams end-to-end. Best-effort delivery -no guarantees. Must use the Internet Protocol ([[IP]]).
- Link Layer
	- Delivers data over a single link between an end host and router, or between routers  

### 7 Layer OSI Model
 ![image.png](https://img.ynchen.me/2023/02/f7969e87e3d75926237be138fb447066.webp)

## 7 Layer OSI Model
1. Physical Layer
2. Data Link Layer  
3. Network Layer
4. Transport Layer
5. Session Layer
6. Presentation Layer
7. Application Layer  
![image.png](https://img.ynchen.me/2023/02/b0cb7ea848e7e26ea5e44b6f44893468.webp)
