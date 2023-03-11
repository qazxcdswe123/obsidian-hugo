# Why care
The cryptic function we see was used to calculate the reverse of square root, namely $\frac{1}{\sqrt{c^{2}}}$, but why care?
It turns out that if we want to implement physics or lighting in your game engine, it helps when the vector you're calculated with are normalized to have length 1. The length of the vector can be calculated using Pythagorean theorem $\sqrt{x^2+y^2+z^2}$ (in 3D of course), and thus each component will be $x \times \frac{1}{\sqrt{x^{2} + y^{2} + z^2}}$, you might see where this is going :).
However, even though calculating exponent in computer is easy, doing division is hard and expensive. In a performance critical scenario such as gaming, this "evil" function can lead to a better performance (**in that particular era**).

>Aside: Normal vectors are unit vectors aligned perpendicularly to a surface, defining its direction. They are commonly used for lighting, collisions, and other operations involving surfaces. Most of the time we only care about the direction of the light or physics and bringing in magnitude may even bring in some weird bugs, so normalized vector is all we need. It also helps to separate the _direction_ from the _magnitude_ of your vector. For example, you can keep the speed of a character constant, even when they travel in weird diagonal directions.

![image.png](https://img.ynchen.me/2023/03/52baa166b548ea36b02578f634751387.webp)

# But How
Mostly involves [[Binary]] calculation, Newton's method, a little math tricks and [[Floating Point Representation]], an additional blog concerning IEEE 754 can be found [[Introduction to Floating Point Number|here]].
A detailed visual proof can be found [Here](https://www.youtube.com/watch?v=p8u_k2LIZyo).

# What Now
The first time I saw this algorithm, I was thrilled and immediately compare it with `y = 1 / sqrt(x)`. And it disappointed me, by a lot. This magic function is now 10x slower!!!
Modern compiler, "No one knows optimization better than me".

It is still a good starting point to learn IEEE 754 though.

> Aside: In a recent Lex Fridman podcast with Carmack, he actually says that he didn't invent this algorithm, this piece of code was found in the codebase but somehow everyone credits this function to him. He is now an AI researcher in Meta.


# References
[Vector math — Godot Engine (stable) documentation in English](https://docs.godotengine.org/en/stable/tutorials/math/vector_math.html)
[Fast Inverse Square Root — A Quake III Algorithm - YouTube](https://www.youtube.com/watch?v=p8u_k2LIZyo)
[Why would you normalize a vector ? : r/gamedev](https://www.reddit.com/r/gamedev/comments/52fayj/why_would_you_normalize_a_vector/)