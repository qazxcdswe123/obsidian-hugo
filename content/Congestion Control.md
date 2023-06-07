---
aliases: []
date created: Jun 5th, 2023
date modified: Jun 5th, 2023
---

## Slow Start
1. The sender starts by sending a small number of packets (usually one) and waits for an acknowledgment (ACK) from the receiver.
2. When the ACK is received, the sender doubles the number of packets it sends and waits for ACKs for all of them.
3. This process continues until the sender detects congestion or the receiver's window has been reached.
4. At this point, slow start has served its purpose and allows data to be transmitted at maximum capacity without congesting the network.

TCP 中的拥塞控制算法，防止发送超过网络能处理的数据量。  
主要思想是：逐渐提高数据传输速率，而不是一开始就很高。
1. 一开始时：建立 TCP 连接，发送方的拥塞窗口大小（cwnd）会被设置为一个很小的值，通常是 1 或 2 个数据包的大小。
2. 每当发送方收到一个对之前发送的数据包的确认（ACK）时，它就会将拥塞窗口大小加倍。（所以其实不慢的）
3. 当拥塞窗口大小达到一个阈值（ssthresh）时，发送方就会停止慢开始算法，转而使用拥塞避免算法。这个阈值通常就是网络能够承受的最大负载。
4. 如果在传输过程中发生了数据包丢失，那么发送方会将阈值减半，并将拥塞窗口大小重置为 1，然后重新开始慢开始算法。

## 拥塞避免算法
用于控制数据包的发送速率，以防止网络拥塞。这种算法在拥塞窗口大小达到阈值（ssthresh）后开始工作，此时慢开始算法已经停止。

1. 当拥塞窗口大小（cwnd）达到阈值（ssthresh）时，拥塞避免算法开始工作。此时，发送方不再将拥塞窗口大小加倍，而是每次收到一个确认（ACK）时，只增加一个最大段大小（MSS）。
2. 这意味着在没有网络拥塞的情况下，拥塞窗口的大小会线性增长，而不是像慢开始算法那样指数增长。这有助于防止网络过载。
3. 如果在传输过程中发生了数据包丢失，那么发送方会将阈值（ssthresh）设置为当前拥塞窗口大小的一半，并将拥塞窗口大小重置为 1，然后重新开始慢开始算法。

## 快重传算法
用于更快地恢复丢失的数据包

思想：当接收方连续收到三个重复的确认（ACK）时，就认为一个数据包已经丢失，然后发送方会立即重新发送这个数据包，而不是等待超时 Timer。

1. 当接收方收到一个乱序的数据包时，它会立即发送一个重复确认（ACK），确认号（acknowledgment number）是它期望接收的下一个数据包的序列号。
2. 如果发送方连续收到三个重复确认（ACK），它就会认为一个数据包已经丢失。这是因为，如果接收方已经收到了后续的数据包，那么它就会重复确认它期望接收的下一个数据包，这通常是丢失的数据包。
3. 当发送方收到三个重复确认（ACK）时，它会立即重新发送丢失的数据包，而不是等待 Timer。

## 快恢复算法
与快重传算法一起工作，当发送方通过快重传算法检测到数据包丢失并重新发送数据包后，快恢复算法就开始工作。

1. 当发送方收到三个重复确认（ACK）并重新发送丢失的数据包后，它会进入快恢复阶段。在这个阶段，发送方会将阈值（ssthresh）设置为当前拥塞窗口大小的一半，然后将拥塞窗口大小（cwnd）设置为新的阈值加上三个最大段大小（MSS）。
2. 在快恢复阶段，每收到一个重复确认（ACK），发送方都会将拥塞窗口大小增加一个最大段大小（MSS）。这意味着在快恢复阶段，拥塞窗口的大小会线性增长。
3. 当发送方收到一个新的确认（ACK），表示丢失的数据包已经被成功接收，那么发送方就会退出快恢复阶段，将拥塞窗口大小设置为阈值（ssthresh），然后开始拥塞避免算法。

## Traffic Shaping

### Leaky Bucket Algorithm
Data always pass in the smae rate

### Token Bucket Algorithm
When a packet (data) needs to be sent, it grabs a token. If there are no tokens, it has to wait. This allows for bursty data, as you could save up tokens when traffic is low and spend them when a burst of data arrives.
Like PV [[Semaphore]]