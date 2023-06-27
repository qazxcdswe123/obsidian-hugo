---
aliases: []
date created: Jun 22nd, 2023
date modified: Jun 22nd, 2023
---
A **media access control address** (**MAC address**) is a [unique identifier](https://en.wikipedia.org/wiki/Unique_identifier "Unique identifier") assigned to a [network interface controller](https://en.wikipedia.org/wiki/Network_interface_controller "Network interface controller") (NIC) for use as a [network address](https://en.wikipedia.org/wiki/Network_address "Network address") in communications within a [network segment](https://en.wikipedia.org/wiki/Network_segment "Network segment").

## Universal and Local (U/L bit)
- **Universally administered addresses (UAA)** is uniquely assigned to a device by its manufacturer.
- **Locally administered address (LAA)** is assigned to a device by software or a network administrator, overriding the burned-in address for physical devices.

Locally administered addresses are distinguished from universally administered addresses by setting (assigning the value of 1 to) the second-least-significant **bit** of the first octet of the address.
- If the bit is 0, the address is universally administered.
- If it is 1, the address is locally administered.

## Unicast and Multicast (I/G bit)
The least significant bit of an address's first octet is referred to as the _I/G_, or _Individual/Group_, bit.
- When this bit is 0, the [frame](https://en.wikipedia.org/wiki/Frame_(networking) "Frame (networking)") is meant to reach only one receiving NIC ([[Unicast]]).
- When this bit is 1, it's a [[Multicast]] address.


## Links
- [MAC address - Wikipedia](https://en.wikipedia.org/wiki/MAC_address)
- [[Ethernet]]