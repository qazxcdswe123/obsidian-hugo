---
aliases: []
date created: Feb 28th, 2023
date modified: Jun 4th, 2023
---
Idea: Informative = Unlikely

## Information
$$I = \log_{2} \frac{1}{P(x)} = - \log_{2}P(X)$$

- Why take logarithm?
1. **Quantifying Multiplicative Changes:** Probabilities multiply (for independent events), but our sense of "information" is more additive. For example, if you flip two coins, the total number of outcomes is 4, which is the multiplication of the outcomes of each coin (2 outcomes for the first coin times 2 outcomes for the second coin). However, the 'information' you get from flipping two coins feels more like 'twice the information from one coin'. Logarithms convert this multiplication of probabilities into addition, which aligns better with our intuitive sense of 'information'.
2. **Measure of Surprise or Rarity:** The logarithm function is decreasing for (0,1], which means the more probable an event is, the less 'information' or 'surprise' it provides when it occurs, and vice versa. This aligns with our intuition: events that occur rarely give us more 'new information' when they do occur than events that occur frequently.

## Entropy
$$H = \Sigma^{M}_{i=1}P(X_{i}) \log_{2} \frac{1}{P(X_{i)}} =\Sigma^{M}_{i=1}P(X_i)I_i$$

$$ I = mH$$
Entropy is highest when uncertainty or randomness is highest. So it is highest when all probability are the same.

## SNR (Signal-to-Noise Ratio)
$$SNR_{dB} = 10 \cdot \lg \left( \frac{P_{signal}}{P_{noise}} \right) 
$$

- $P_{signal}$ is the power of the signal,
- $P_{noise}$ is the power of the noise,

### Threshold Effect
as long as the SNR is above this threshold, the receiver can effectively suppress noise and the error rate remains low. However, once the SNR falls below this threshold, the noise begins to significantly affect the demodulated signal, causing a rapid increase in the error rate.

## Baud
$$R_{b}= R_{B} \cdot \log_{2} M$$

$M$ is the radix of the data.

## Shannon–Hartley theorem
![cd8e56f09c4da5480c1ddfd15855f2cc803938f4](https://wikimedia.org/api/rest_v1/media/math/render/svg/cd8e56f09c4da5480c1ddfd15855f2cc803938f4)