1. 
```python
import numpy as np
import matplotlib.pyplot as plt


# 利用均匀分布（随机数numpy random.rand）首先生成两点分布样本，进而生成二项分布（不能直接调用numpy random.binomial函数）的样本，画出二项分布样本的直方图。


def generate_samples(n, p, size=1):
    """
    Parameters
    ----------
    n: number of trials : int
    p: probability of success : float
    size: number of samples : int
    """
    data = np.random.rand(n, size)
    data[data < p] = 0
    data[data >= p] = 1
    # change the type of samples from np.float64 to int
    data = data.astype(int)
    return data.sum(axis=0)


# Use generated samples to plot the histogram of binomial distribution
def plot_binomial_bar(data):
    """
    Parameters
    ----------
    data: samples of binomial distribution
    """
    x_axis = np.arange(data.min(), data.max() + 1)
    y_axis = np.zeros(x_axis.shape)
    y_index = 0
    for i in x_axis:
        y_axis[y_index] = (data == i).sum()
        y_index += 1
    plt.bar(x_axis, y_axis)
    plt.title(label='Binomial Distribution Samples')
    plt.xlabel(xlabel='Measurements')
    plt.ylabel(ylabel='Occurrence')
    plt.show()


if __name__ == '__main__':
    samples = generate_samples(20, 0.5, size=160)
    print(samples)
    plot_binomial_bar(samples)


```

```python
import numpy
import matplotlib.pyplot as plt

"""
2.利用均匀分布（随机数numpy random.rand）或标准正态分布分布律（scipy.stat norm.cdf），
采用2种不同的算法产生正态分布（不能直接调用numpy random.normal函数）的样本，画出正态分布样本的直方图，对2种算法的复杂度进行对比分析。
"""


def generate_normal_distribution_samples1(mean, standard_deviation, size=1):
    """
    Parameters
    ----------
    mean: mean of normal distribution : float
    standard_deviation: standard deviation of normal distribution : float
    size: number of samples : int
    ----------
    Algorithm Used: Box-Muller algorithm
    """
    u = numpy.random.rand(size)
    v = numpy.random.rand(size)
    z = numpy.sqrt(-2 * numpy.log(u)) * numpy.cos(2 * numpy.pi * v)
    return mean + standard_deviation * z


def generate_normal_distribution_samples2(mean, standard_deviation, size=1):
    """
    Parameters
    ----------
    mean: mean of normal distribution : float
    standard_deviation: standard deviation of normal distribution : float
    size: number of samples : int
    ----------
    Algorithm Used: Inverse Transform Sampling
    """
    import scipy.stats as stats
    u = numpy.random.rand(size)
    return mean + standard_deviation * numpy.sqrt(2) * stats.norm.ppf(u)


if __name__ == '__main__':
    # samples = numpy.random.normal(0, 1, size=1000)
    # plt.hist(samples, 50)
    # plt.show()
    sample1 = generate_normal_distribution_samples1(0, 1, size=1000)
    plt.hist(sample1, 50)
    plt.title(label='Normal Distribution Samples1')
    plt.xlabel(xlabel='Measurements')
    plt.ylabel(ylabel='Occurrence')
    plt.show()

    sample2 = generate_normal_distribution_samples2(0, 1, size=1000)
    plt.hist(sample2, 50)
    plt.title(label='Normal Distribution Samples2')
    plt.xlabel(xlabel='Measurements')
    plt.ylabel(ylabel='Occurrence')
    plt.show()
```

```python
import binomial_distribution
import normal_distribution
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

"""
3.	利用均匀分布和两点分布的样本来验证中心极限定理，
画出“相应分布和的分布”对应样本的直方图以及相应的真实正态分布概率密度曲线，进行对比分析。
x 轴是测量值，y 轴是出现次数。
"""

def central_limit_theorem():
    """
    Use uniform distribution and binomial distribution to verify central limit theorem
    """
    binomial_samples = binomial_distribution.generate_samples(20, 0.5, size=1000)
    normal_samples = normal_distribution.generate_normal_distribution_samples2(0, 1, size=1000)

    # generate samples from central limit theorem
    plt.hist(binomial_samples, bins=50)
    plt.title(label='Central Limit Theorem Samples')
    plt.xlabel(xlabel='Measurements')
    plt.ylabel(ylabel='Occurrence')
    plt.show()

    plt.hist(normal_samples, 50)
    plt.title(label='Normal Distribution Samples')
    plt.xlabel(xlabel='Measurements')
    plt.ylabel(ylabel='Occurrence')
    plt.show()

    x_axis = np.arange(-5, 5, 0.01)
    y_axis = stats.norm.pdf(x_axis, 0, 1)
    plt.plot(x_axis, y_axis)
    plt.title(label='Normal Distribution Probability Density Function')
    plt.xlabel(xlabel='Measurements')
    plt.ylabel(ylabel='Probability')
    plt.show()
    
    
central_limit_theorem()
```

```python
"""
(4)	分别生成均匀分布、两点分布以及正态分布的样本，验证大数定律。
画图展示随着样本容量的增加，随机变量的算术平均依概率收敛到数学期望。
x axis: Number of coin tosses (from 0 to 10000)
y axis: head ratio (0.5 in the middle) 
"""

import numpy as np
import matplotlib.pyplot as plt
import binomial_distribution
import normal_distribution



def verify_law_of_large_numbers():
    binomial_samples = binomial_distribution.generate_samples(1, 0.5, size=10000)
    normal_samples = normal_distribution.generate_normal_distribution_samples1(0, 1, size=10000)

    binomial_distribution_ratio = []
    normal_distribution_ratio = []
    for i in range(1, 10000):
        binomial_distribution_ratio.append(np.mean(binomial_samples[:i]))
        normal_distribution_ratio.append(np.mean(normal_samples[:i]))
        
    plt.plot(binomial_distribution_ratio)
    plt.title(label='Binomial Distribution Law of Large Numbers')
    plt.xlabel(xlabel='Number of coin tosses')
    plt.xlim(1, 10000)
    plt.ylabel(ylabel='Head ratio')
    plt.ylim(0.4, 0.6)
    plt.show()
    
    plt.plot(normal_distribution_ratio)
    plt.title(label='Normal Distribution Law of Large Numbers')
    plt.xlabel(xlabel='Number of coin tosses')
    plt.xlim(1, 10000)
    plt.ylabel(ylabel='Head ratio')
    plt.ylim(-0.1, 0.1)
    plt.show()


verify_law_of_large_numbers()
```