---
aliases: []
date created: Apr 4th, 2023
date modified: Jun 22nd, 2023
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

## CSMA/CD
1. **准备发送：** 适配器从网络层获得一个分组，加上首部和尾部，组成以太网帧，放入适配器的缓存中；
2. **检测信道：** 若检测到信道忙，则不停检测，直到信道空闲。若检测到信道空闲，并在 96 比特时间内仍保持空闲，则发送帧；
3. **在发送过程中不停检测：**
	- **发送成功：** 在争用期内未检测到碰撞，则帧肯定发送成功。发送后，回到（1）
	- **发送失败：** 在争用期内检测到碰撞，停止发送数据，发送干扰信号。执行二进制[[Exponential backoff|指数退避]]算法，等待 r 倍 512 比特后，返回步骤（2），继续检测信道。若重传 16 次仍不成功，则停止重传并向上报错误。
   

- 争用期长度为 2t，即端到端传播时延的两倍。检测到碰撞后不发送干扰信号。

## Links
- [Minimum ethernet frame is 64 bytes, Why the payload must be padded to at least 46 bytes - Network Engineering Stack Exchange](https://networkengineering.stackexchange.com/questions/34189/minimum-ethernet-frame-is-64-bytes-why-the-payload-must-be-padded-to-at-least-4)
- [Ethernet frame - Wikipedia](https://en.wikipedia.org/wiki/Ethernet_frame)
- [EtherType - Wikipedia](https://en.wikipedia.org/wiki/EtherType)