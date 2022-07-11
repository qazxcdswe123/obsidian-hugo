[[Floating Point Representation]]
[Exponent bias - Wikipedia](https://en.wikipedia.org/wiki/Exponent_bias)
the value stored is offset from the actual value by the **exponent bias**, also called a **biased exponent**
Biasing is done because exponents have to be signed values in order to be able to represent both tiny and huge values, but [two's complement](https://en.wikipedia.org/wiki/Two%27s_complement "Two's complement"), the usual representation for signed values, would make comparison harder.