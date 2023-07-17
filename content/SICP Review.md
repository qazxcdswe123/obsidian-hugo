---
aliases: []
date created: Jan 2nd, 2023
date modified: Jul 17th, 2023
---

## SICP Review: Languages Die, Long Live Mindsets

Warning: free flowing writing below.

SICP is considered one of the most prestigious textbooks in the programming field and is often referred to as the bible of computer science. Instead of teaching you languages it teaches you programming (as an introductory textbook). I had very high expectations for it and spent half a month reading through the first 3 chapters. However, I have to say that it didn't meet my expectations, and considered much of its content 'trivial'.

So what is the book about? Well, it all comes down to two words: "Abstraction" and "Encapsulation".

For me, abstraction means extracting the "sameness" and putting similarity together, while the encapsulation part means to "package" what is needed to use together.

> [!NOTE] Thought: The Fundamental Abstraction  
> Programes are built on top of multiple abstractions, such as the Programming Languages, the Operating System, the Von Neumann Machine or even The World! I would argue that the world is the fundamental abstraction of all kinds and all other abstractions were built on top of that.

There are also JavaScript and Python versions of SICP and I will say that the JavaScript version may be a good choice given that it has a comparative version. Many people will argue that you should only read the Scheme version, but I will say the book is not about the language but the ideas behind it, so I guess it doesn't really matter.

> [!NOTE] The Scheme Experience  
> I have to say that the developer experience of Scheme is not great! I use Racket and it seems that some of the functions mentioned in the book are not contained in Racket. The Racket language server is great and it provides some auto-completions and can do code formatting, but it's still cumbersome to find the right position to close the parentheses (just like JavaScript lol).  
> The code reading experience is not bad once you have become accustomed to the style, but the code writing experience is still sometimes frustrating.  
> It seems that the Scheme standard is lossy? So sometimes you can't find the exact implementation and it is just like the undefined behavior in C and C++. Kind of annoying tbh.

### Random Notes
Chapter 1 introduces the "procedures" and how we can use them to build up the abstraction. A lot of math is involved here and it's a bit challenging. You need to really grasp the abstract idea and some of the math insights to get through them. I found a term saying that it is `executable math` which really suits the chapter.  

The parenthesis in scheme is annoying to write and at first annoying to read. But after you get used to it become really easy to read, still frustrating to write.  

The function passing in scheme is really powerful and mind-blowing. Even though is may be trivial in functional programming, but I haven't learnt it yet so...  

It's the most fun part of reading, maybe because I'm less experienced with this idea.

___

Chapter 2 introduces "data" called `list` and the `list` are basically linked list in C (LISP stands for `LISt Processing`). A lot of the abstraction and encapsulation can be learned from OOP, so it's really boring to read about this.  

Also noticed that other languages such as Rust and JavaScript learned (copied) a lot from LISP. Even the name is the same in Rust :D.

___

Chapter 3 basically uses what we have learned to build objects with state (remind me of react) and introduces steam. Stream is really powerful and I work like promise in JavaScript. Really like the idea.  

The message passing now can be achieved by `channel` and I would say the design of `channel` is much, much better.

### Why SICP Didn't Meet My Expectation
I found that a lot of the concepts were trivial and a lot of the abstraction can be learned from OOP. The only difference is that scheme is a very flexible and dynamic language, and the feeling is just unmatched.

If you are an experienced programmer, then I would assume that you already have the gist of many ideas the book is trying to convey. But the book is itself a textbook, and I would say the exercises can sometimes be hard. Even though no prior knowledge is needed to start, but it could certainly be devastating to fail to solve the problems. It is also fun to see that a lot of discussion on `schemewiki` is about how OP was wrong, and the errata were also wrong, the errata of the errata were also wrong. So it's a bit challenging if you are new to programming, especially if you are self learning.

Besides, the idea of concurrency can also be better learned from database theory.

What's more, sometimes I feel a sense of emptiness when reading the book, maybe because it teaches you abstraction, and it can be frustrating. Didn't have much fun reading this.

### Excerpts
> higher-order procedures permit us to manipulate these general methods to create further abstractions.  
> As programmers, we should be alert to opportunities to identify the underlying abstractions in our programs and to build upon them and generalize them to create more powerful abstractions. This is not to say that one should always write programs in the most abstract way possible; expert programmers know how to choose the level of abstraction appropriate to their task. But it is important to be able to think in terms of these abstractions, so that we can be ready to apply them in new contexts. The significance of higher-order procedures is that they enable us to represent these abstractions explicitly as elements in our programming language, so that they can be handled just like other computational elements.

> Encapsulating, or “hiding,” parts of the state of a large system within local variables

> Functional programming languages, which do not include any provision for assignment or mutable data.

> It is intriguing that a similar connection between time and communication also arises in the theory of Relativity, where the speed of light (the fastest signal that can be used to synchronize events) is a fundamental constant relating time and space. The complexities we encounter in dealing with time and state in our computational models may in fact mirror a fundamental complexity of the physical universe.

Special Thanks for claude to correct my english mistakes.
