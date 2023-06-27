---
aliases: [Internet Protocol, IPv4, IPv6]
date created: Feb 20th, 2023
date modified: Jun 8th, 2023
---
- [[CIDR]]  

| Property       | Behavior                                           |
| -------------- | -------------------------------------------------- |
| Datagram       | Individually routed packets. Hop-by-hop routing.   |
| Unreliable     | Packets might be dropped.                          |
| Best effort    | ..but only if necessary.                           |
| Connectionless | No per-flow state. Packets might be mis-sequenced. |

## IPv4
![image.png](https://img.ynchen.me/2023/02/413307f8e7ba8516a44c75cf35d93972.webp)

## IPv6
128-bit addresses represented in hexadecimal notation, separated into eight sub-blocks of 16 bits each.

### Compression
1. **Zero Compression**: If an IPv6 address contains continuous zeros, they are replaced with a double colon "::". `ef82:0000:0000:0000:0000:1a12:1234:1b12` -> `ef82::1a12:1234:1b12`
2. **Leading Zero Compression**: `1234:0fd2:5621:0001:0089:0000:0000:4500` -> `1234:fd2:5621:1:89:0:0:4500`