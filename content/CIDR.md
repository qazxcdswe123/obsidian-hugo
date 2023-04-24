---
aliases: []
date created: Feb 21st, 2023
date modified: Apr 20th, 2023
---

## CIDR
- Classless Inter-Domain Routing
- A **Longest Prefix Match**

**Class A:** Allows 2^24 host addresses on the network. The starting host address is 0.0.0.0 and the ending address is 127.0.0.0. These networks use the 255.0.0.0 subnet mask, or /8 CIDR notation.

**Class B:** Allows 2^16 host addresses on the network. The starting host address is 128.0.0.0 and the ending address is 191.255.0.0. These networks use the 255.255.0.0 subnet mask, or /16 CIDR notation.

**Class C:** Allows 2^8 host addresses on the network. The starting host address is 192.0.0.0 and the ending address is 223.255.255.0. These networks use the 255.255.255.0 subnet mask, or /24 CIDR notation.

- [CIDR Conversion Table | HPE Edgeline Docs](https://techlibrary.hpe.com/docs/otlink-wo/CIDR-Conversion-Table.html)
- [[Netmask]]

## Classed IP

### Class A
- Public IP Range: 1.0.0.0 to 127.0.0.0
	- First octet value range from 1 to 127
- Private IP Range: 10.0.0.0 to 10.255.255.255 (See [Private IP Addresses](https://www.meridianoutpost.com/resources/articles/IP-classes.php#private) below for more information)
- Subnet Mask: 255.0.0.0 (8 bits)
- Number of Networks: 126
- Number of Hosts per Network: 16,777,214

### Class B
- Public IP Range: 128.0.0.0 to 191.255.0.0
	- First octet value range from 128 to 191
- Private IP Range: 172.16.0.0 to 172.31.255.255 (See [Private IP Addresses](https://www.meridianoutpost.com/resources/articles/IP-classes.php#private) below for more information)
- Subnet Mask: 255.255.0.0 (16 bits)
- Number of Networks: 16,382
- Number of Hosts per Network: 65,534

### Class C
- Public IP Range: 192.0.0.0 to 223.255.255.0
	- First octet value range from 192 to 223
- Private IP Range: 192.168.0.0 to 192.168.255.255 (See [Private IP Addresses](https://www.meridianoutpost.com/resources/articles/IP-classes.php#private) below for more information)
- Special IP Range: 127.0.0.1 to 127.255.255.255 (See [Special IP Addresses](https://www.meridianoutpost.com/resources/articles/IP-classes.php#special) below for more information)
- Subnet Mask: 255.255.255.0 (24 bits)
- Number of Networks: 2,097,150
- Number of Hosts per Network: 254

## Class D
- Range: 224.0.0.0 to 239.255.255.255
	- First octet value range from 224 to 239
- Number of Networks: N/A
- Number of Hosts per Network: Multicasting

### Class E
- Range: 240.0.0.0 to 255.255.255.255
	- First octet value range from 240 to 255
- Number of Networks: N/A
- Number of Hosts per Network: Research/Reserved/Experimental

### Private IP Addresses
- Class A Private Range: 10.0.0.0 to 10.255.255.255
- Class B Private APIPA Range: 169.254.0.0 to 169.254.255.255
	- _Automatic Private IP Addressing_ (APIPA) is a feature with _Microsoft Windows_-based computers to automatically assign itself an IP address within this range if a _Dynamic Host Configuration Protocol_ (DHCP) server is not available on the network. A DHCP server is a network device that is responsible for assigning IP addresses to devices on the network.  
	- At your home, your Internet modem or router likely provides this functionality. In your work place, a _Microsoft Windows Server_, a network firewall, or some other specialized network device likely provides this functionality for the computer at your work environment.
- Class B Private Range: 172.16.0.0 to 172.31.255.255
- Class C Private Range: 192.168.0.0 to 192.168.255.255

[Ethernet Numbers](https://www.iana.org/assignments/ethernet-numbers/ethernet-numbers.xhtml)