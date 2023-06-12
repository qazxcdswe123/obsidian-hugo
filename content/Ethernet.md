---
aliases: []
date created: Apr 4th, 2023
date modified: Jun 12th, 2023
---
- Minimum ethernet frame is 64 bytes
- ![](https://img.ynchen.me/2023/04/844aef44c005a8a2254faf503ef24945.webp)

## Frame 
An Ethernet frame is a unit of data that's packaged for transmission across an Ethernet network. It includes various pieces of information to facilitate the sending, receiving, and processing of the data.  
This data is encapsulated in a frame structure, which includes a preamble, start frame delimiter, MAC destination and source addresses, type/length, payload (data), and a frame check sequence (FCS).

以太网帧的结构如下：
- 前导码 (Preamble)：7 个字节，由 10101010...的交替比特构成，用于唤醒接收端的接收器并使其能够同步到帧的开始。
- 起始帧定界符 (SFD)：1 个字节，固定为 10101011，用于标识帧的开始，是一种帧定界符。
- 目的 MAC 地址 (Destination MAC)：6 个字节，指定接收者的 MAC 地址。
- 源 MAC 地址 (Source MAC)：6 个字节，指定发送者的 MAC 地址。
- 类型/长度 (Type/Length)：2 个字节，标识负载的类型或长度。
- 数据负载 (Data Payload)：46-1500 字节，这是实际的数据内容。
- 帧检验序列 (FCS)：4 个字节，用于检测在传输过程中是否发生错误。

## Links
- [Minimum ethernet frame is 64 bytes, Why the payload must be padded to at least 46 bytes - Network Engineering Stack Exchange](https://networkengineering.stackexchange.com/questions/34189/minimum-ethernet-frame-is-64-bytes-why-the-payload-must-be-padded-to-at-least-4)
- [Ethernet frame - Wikipedia](https://en.wikipedia.org/wiki/Ethernet_frame)
- [EtherType - Wikipedia](https://en.wikipedia.org/wiki/EtherType)