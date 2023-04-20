---
aliases: []
date created: Feb 17th, 2023
date modified: Apr 8th, 2023
---

# PCIE
- [PCI Express - Wikipedia](https://en.wikipedia.org/wiki/PCI_Express)
- **Peripheral Component Interconnect Express**
- Style: [Serial communication](https://en.wikipedia.org/wiki/Serial_communication)

> Every desktop PC [**motherboard**](https://www.tomshardware.com/reviews/motherboard-definition,5749.html) (opens in new tab)has a number of PCIe slots you can use to add [**GPUs**](https://www.tomshardware.com/reviews/gpu-graphics-card-definition,5742.html)(opens in new tab) (aka video cards aka graphics cards), [**RAID cards**](https://www.tomshardware.com/reviews/raid-controller-card-definition,5756.html)(opens in new tab)**,** Wi-Fi cards or [**SSD**](https://www.tomshardware.com/reviews/ssd-solid-state-drive-definition,5763.html)(opens in new tab) (solid-state drive) add-on cards.

## NVME

> The initialism _NVM_ stands for _[non-volatile memory](https://en.wikipedia.org/wiki/Non-volatile_memory "Non-volatile memory")_, which is often NAND [flash memory](https://en.wikipedia.org/wiki/Flash_memory "Flash memory") that comes in several physical form factors, including [solid-state drives](https://en.wikipedia.org/wiki/Solid-state_drive "Solid-state drive") (SSDs), PCIe add-in cards, and [M.2](https://en.wikipedia.org/wiki/M.2 "M.2") cards, the successor to [mSATA](https://en.wikipedia.org/wiki/MSATA "MSATA") cards. NVM Express, as a logical-device interface, has been designed to capitalize on the low [latency](https://en.wikipedia.org/wiki/Hard_disk_drive_performance_characteristics#Access_time "Hard disk drive performance characteristics") and internal parallelism of solid-state storage devices.

- [[Linux Storage]]

## SSD Trim
[What is Trim? | Crucial.com](https://www.crucial.com/articles/about-ssd/what-is-trim)

## RAID
- Raid 0
	- doubled speed, no redundancy
	- splits data into blocks and writes them across multiple drives in the array, offering fast read and write speeds
	- does **not provide fault tolerance or redundancy**, and problems on any of the disks in the array can result in complete data loss

# CPU

## Hyper Threading
- [[Thread]]
- [[Multi Threading]]
Hyper-threading is a [[process]] by which a CPU divides up its physical cores into virtual cores that are treated as if they are actually physical cores by the [[operating system]]. These virtual cores are also called threads.
The CPU exposes two execution contexts per physical core. This means that one physical core now works like two “logical cores” that can handle different software threads.
TLDR: use unused resources ([[Optimization|pipeline]], [[register]]).