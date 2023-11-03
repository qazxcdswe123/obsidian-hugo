---
aliases:
  - AI
link:
  - "[[Gradient Descent]]"
date created: Sep 11th, 2023
date modified: Oct 30th, 2023
---

## Neural Network
1. Perceptron
	- [Perceptron - Wikipedia](https://en.wikipedia.org/wiki/Perceptron)
2. Feed Forward Networks
	- 
3. Multi-Layer Perceptron
4. Radial Based Networks
5. Convolutional Neural Networks
6. Recurrent Neural Networks
7. Long Short-Term Memory Networks

8. **Input layer:** this first layer is where data is received before being passed along to the next-layer nodes
9. **Hidden layer:** where weighted connections and non-linear activation functions generate the output  (this level could include multiple layers)
10. **Output layer:** where the finished data is expressed

## Acceleration
- Feature Scaling
	- z-score normalization
		- After z-score normalization, all features will have a mean of 0 and a standard deviation of 1.
		- Change input to $x^{(i)}_j = \dfrac{x^{(i)}_j - \mu_j}{\sigma_j}$, where $\mu_j = \frac{1}{m} \sum_{i=0}^{m-1} x^{(i)}_j$ and $\sigma^2_j = \frac{1}{m} \sum_{i=0}^{m-1} (x^{(i)}_j - \mu_j)^2$
- Vectorization
- Feature Engineering (Polynomial Feature, not have to be a linear line)

## Mean Teacher architecture
### Components:
- **Student Network**: This network is optimized by stochastic gradient descent. It is responsible for making predictions based on the input data.
- **Teacher Network**: This network is updated by the exponential moving average (EMA) of the Student network's parameters. It is used to generate pseudo-labels for unlabeled images.