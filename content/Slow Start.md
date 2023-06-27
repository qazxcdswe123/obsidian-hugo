---
aliases: [慢开始算法]
date created: Jun 23rd, 2023
date modified: Jun 23rd, 2023
---
1. The sender starts by sending a small number of packets (usually one) and waits for an acknowledgment (ACK) from the receiver.
2. When the ACK is received, the sender **doubles** the number of packets it sends and waits for ACKs for all of them.
3. This process continues until the sender detects congestion or the receiver's window has been reached.
4. At this point, slow start has served its purpose and allows data to be transmitted at maximum capacity without congesting the network.

[[TCP]] 中的拥塞控制算法，防止发送超过网络能处理的数据量。  
主要思想是：逐渐提高数据传输速率，而不是一开始就很高。
1. 一开始时：建立 TCP 连接，发送方的拥塞窗口大小（cwnd）会被设置为一个很小的值，通常是 1 或 2 个数据包的大小。
2. 每当发送方收到一个对之前发送的数据包的确认（ACK）时，它就会将拥塞窗口大小加倍。（所以其实不慢的）
3. 当拥塞窗口大小达到一个阈值（ssthresh）时，发送方就会停止慢开始算法，转而使用拥塞避免算法。这个阈值通常就是网络能够承受的最大负载。
4. 如果在传输过程中发生了数据包丢失，那么发送方会将阈值减半，并将拥塞窗口大小重置为 1，然后重新开始慢开始算法。