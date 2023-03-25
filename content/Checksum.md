---
aliases: []
tags: []
date created: Feb 26th, 2023
date modified: Mar 25th, 2023
---
- [[Hashing]]

## CRC
- [Cyclic redundancy check - Wikipedia](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)  
- [What Is Cyclic Redundancy Check (CRC), and It’s Role in Checking Error? | Simplilearn](https://www.simplilearn.com/tutorials/networking-tutorial/what-is-cyclic-redundancy-check)

### Sender Side (CRC Generator and Modulo Division):
1. The first step is to add the no. of zeroes to the data to be sent, calculated using k-1 (k - is the bits obtained through the polynomial equation.)
2. Applying the Modulo Binary Division to the data bit by applying the XOR and obtaining the remainder from the division
3. The last step is to append the remainder to the end of the data bit and share it with the receiver.

> Modulo binary division is a method of binary division that uses the modulo operation to find the remainder of a division. In this method, instead of subtracting the divisor from the dividend, we use the XOR operation to find the remainder.

### Receiver Side (Checking for Errors in the Received data):
To check the error, perform the Modulo division again and check whether the remainder is 0 or not, 
1. If the remainder is 0, the data bit received is correct, without any errors.
2. If the remainder is not 0, the data received is corrupted during transmission.