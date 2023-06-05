---
aliases: []
date created: Nov 27th, 2022
date modified: Jun 4th, 2023
---

## Communication
- [[Fourier Transform]]
- [汇总：能量/功率信号、频谱、能量谱、功率谱 - 知乎](https://zhuanlan.zhihu.com/p/339291397)

1. **Spectrum (频谱):** This refers to the range of frequencies that a signal contains. In signal processing, the spectrum of a signal or sound provides a representation of which frequencies are present in the signal. In other words, it's a breakdown of a signal into its frequency components.
2. **Wavelength (波长):** This is the spatial period of a wave, the distance over which the wave's shape repeats. It is usually determined by considering the distance between consecutive points of the same phase, such as crests, troughs, or zero crossings, in a waveform. The standard unit for wavelength is the meter (m).

$$v = f \cdot \lambda$$
- $v$: speed
- $f$: freq
- $\lambda$: wavelength

### Energy Signal (能量信号)

### Power Signal (功率信号)

## Computer Science
- [[Interrupt]]
- [[Trap]]
- [[Exception]]
- [[Linux]]


如果我们需要查询所有选择了张三所选修全部课程的学生的姓名，我们可以通过以下关系代数表达式来实现。这个问题可以被解决为两部分，一是找出张三所选修的所有课程，二是找出选修了所有这些课程的学生。最后用自然连接将学生编号与学生姓名关联起来。

这是关系代数的表示：

$$\pi_{SN}(S) \bowtie (\pi_{S\#}(SC) - \pi_{S\#}((\pi_{C\#}(SC) - \pi_{C\#}(\sigma_{S\# = \text{'张三的学号'}}(SC))) \times \pi_{S\#}(SC)))$$

在这个表达式中，我们首先通过选择操作符 (σ) 找到张三所选修的所有课程，然后从所有课程中减去这些课程，得到张三没有选修的课程。然后我们找出选修了这些课程的所有学生，并从所有学生中减去这些学生，得到只选修了张三所选修的课程的学生。最后，我们用投影操作符 (π) 来选取这些学生的姓名。