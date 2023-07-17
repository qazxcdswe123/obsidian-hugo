---
aliases: [环]
date created: Dec 5th, 2022
date modified: Dec 27th, 2022
---

# Ring

## [[Discrete Math Algebra]]
- 加法：Abel，单位元 0，负元 -x  
- 乘法：结合律，单位元 (If Any) 1，逆元 $x^{-1}$，
- 加法乘法间满足分配律

- 满足交换律为 **交换环**，
- 存在单位元为 **含幺环**  
- 无零因子环：$\forall a,b \in R$, $ab = 0 \to a = 0$ or $b = 0$  
- 整环：既是交换环，含幺环，又是无零因子环
- 域：是整环，至少两个元素，除 0 外都有逆

## Properties
1. $a0 = 0a = 0$
2. $a(-b) = (-a)b = -ab$
3. $(-a)(-b) = ab$

重点：有分配率

# Integral Domain

## Definition
> 给定一个环 R，对任意元素 a ∈ R，如果存在元素 b ∈ R 使得 b != 0 且 a ∗ b = 0，则称 a 为一个 **零因子 (zero divisor)**。  
> 如果交换环 R 中没有除 0 以外的零因子，即 ∀a, b ∈ R，如果 ab = 0 有 a = 0 或 b = 0，则称 R 为整环。

# Subring
- Same as [[Subgroups]]

## Definition
> 给定环 R，R′ 是 R 的子集，如果 R′ 在环 R 的加法和乘法上也形成环，则称 R′ 是 R 的子环，记为 R′ ⊂ R。

[[Isomorphism]]

## Ideal
> 给定环 R，I 是 R 的 **子环**，如果对任意的 r ∈ R 有 rI ⊂ I 和 Ir ⊂ I，则称 I 是 R 的理想。

Normal [[Subgroups]] in ring.
1. 所有的环 R 都有两个平凡理想:{0} 和 R。

### Principal Ideal 主理想
[[Cyclic Groups]]
1. 对任意环 R，只包含一个元素 0 的主理想 ⟨0⟩ 称为零理想。
2. 对任意带单位元的环 R，称 ⟨1⟩ 为单位理想，显然 R = ⟨1⟩。
3. 对任意整数 n，集合 nZ 是整数环 Z 的理想，也是主理想， nZ = ⟨n⟩。

# 商环
