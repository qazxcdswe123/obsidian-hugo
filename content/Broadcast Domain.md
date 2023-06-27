A broadcast domain is a logical division of a computer network where all nodes can reach each other by [[broadcast]] at the data link layer ([[Network Layer|OSI Layer]] 2)

In a broadcast domain, devices can communicate with each other directly, without the need for an intermediate [[gateway]] router

## Break Down
Routers, layer 3 switches, and VLANs can be used to separate broadcast domains.
For example, in a network with multiple interconnected switches without VLANs, the broadcast domain includes all of those switches; when using VLANs, each [[VLAN]] is typically its own broadcast domain.

## Links
- [[Collision Domain]]