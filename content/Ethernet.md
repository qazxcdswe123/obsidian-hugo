---
aliases: []
date created: Apr 4th, 2023
date modified: Jun 26th, 2023
---
- Minimum ethernet frame is 64 bytes
- Measured in byte ![Measured in byte](https://img.ynchen.me/2023/04/844aef44c005a8a2254faf503ef24945.webp)

## Frame 
- Size: 64 - 1518 bytes
	- Minimum: an 18-byte header and a 46-byte payload.
	- Maximum: a 1,500-byte payload.

1. Preamble: Informs the receiving system that a frame is starting and enables synchronization.
2. Start Frame Delimiter (SFD): Signifies that the Destination MAC Address field begins with the next byte.
3. Destination [[MAC Address]]: The MAC address of the destination device.
4. Source [[MAC Address]]: The MAC address of the source device.
5. EtherType (in Ethernet II): In Ethernet II, this field identifies the protocol carried in the payload of the frame (e.g., IPv4, IPv6, or [[ARP]]).
	- A value of 0x0800 indicates that the payload is an [[IP]] [[packet]] 
	- A value of 0x0806 indicates that the payload is an [[ARP]] packet.
6. Data and Pad: Contains the payload data. Padding data is added to meet the minimum length requirement for this field (46 bytes).
7. Frame Check Sequence (FCS): Contains a 32-bit Cyclic Redundancy Check ([[CRC]]) which allows detection of corrupted data

## CSMA/CD
1. **准备发送：** 适配器从网络层获得一个分组，加上首部和尾部，组成以太网帧，放入适配器的缓存中；
2. **检测信道：** 若检测到信道忙，则不停检测，直到信道空闲。若检测到信道空闲，并在 96 比特时间内仍保持空闲，则发送帧；
3. **在发送过程中不停检测：**
	- **发送成功：** 在争用期内未检测到碰撞，则帧肯定发送成功。发送后，回到（1）
	- **发送失败：** 在争用期内检测到碰撞，停止发送数据，发送干扰信号。执行二进制 [[Exponential backoff|指数退避]] 算法，等待 r 倍 512 比特后，返回步骤（2），继续检测信道。若重传 16 次仍不成功，则停止重传并向上报错误。
   

- 争用期长度为 2t，即端到端传播时延的两倍。检测到碰撞后不发送干扰信号。

## Links
- [Minimum ethernet frame is 64 bytes, Why the payload must be padded to at least 46 bytes - Network Engineering Stack Exchange](https://networkengineering.stackexchange.com/questions/34189/minimum-ethernet-frame-is-64-bytes-why-the-payload-must-be-padded-to-at-least-4)
- [Ethernet frame - Wikipedia](https://en.wikipedia.org/wiki/Ethernet_frame)
- [EtherType - Wikipedia](https://en.wikipedia.org/wiki/EtherType)