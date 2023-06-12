## What
An error correction system that can detect and correct errors when data is stored or transmitted.
Hamming code uses a block parity mechanism, dividing the data into blocks and adding parity to each block.

## How
1. Calculate the number of redundant bits
2. Insert the parity bits at positions that are powers of 2 (1, 2, 4, 8).
3. Set the parity bit to 1 if the total number of ones in the positions it checks is odd, and set it to 0 if the total number of ones is even

Example data: 1011010
1. Calculate the number of parity bits: Using the formula 2^p ≥ d + p + 1, we find that we need 4 parity bits for 7 data bits (2^4 ≥ 7 + 4 + 1).
2. Place the parity bits: Insert the parity bits at positions 1, 2, 4, and 8: _ P1 P2 1 P4 0 1 1 0 1 0
3. Calculate the parity bits:
	- P1 covers positions 1, 3, 5, 7, 9 (1, 1, 0, 1): 3 ones, so P1 = 0 (even parity)
	- P2 covers positions 2, 3, 6, 7, 10 (0, 1, 1, 0): 2 ones, so P2 = 0 (even parity)
	- P4 covers positions 4, 5, 6, 7 (1, 0, 1, 1): 3 ones, so P4 = 0 (even parity)
	- P8 doesn't cover any positions in this case, since it exceeds the total length

## Why
$$2^{p} \geq d + p + 1$$
- $p$: number of parity bits
- $d$: number of data bits

## Links
- ECC [[Memory]]