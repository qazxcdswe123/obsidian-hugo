# Condition Code (Implicit Setting)
All 1-bit flags, not set directly

## Single bit registers
- `CF`: Carry Flag (for unsigned)
- `SF`: Sign Flag (for signed)
- `ZF`: Zero Flag
- `OF`: Overflow Flag (for signed)

## Condition Codes (Explicit Setting: Compare)
Used for compare two values
`cmpq SRC2, SRC1` : Reversed order
`cmpq b,a` like computing `a-b` without setting destination

- `CF` set if carry out from most significant bit (used for unsigned comparisons)
- `ZF` set if a == b
- `SF` set if (a-b) < 0 (as signed)(negative)
- `OF` set if two’s-complement (signed) overflow (a>0 && b<0 && (a-b)<0) || (a<0 && b>0 && (a-b)>0)

## Condition Codes (Explicit Setting: Test)
`testq Src2, Src1`
`testq b,a` like computing `a&b` without setting destination

Sets condition codes based on value of `Src1 & Src2`
Useful to have one of the operands be a mask

- `ZF` set when `a&b == 0`
- `SF` set when `a&b < 0`
