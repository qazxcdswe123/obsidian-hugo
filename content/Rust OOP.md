### [Polymorphism](https://doc.rust-lang.org/stable/book/ch17-01-what-is-oo.html#polymorphism)

To many people, polymorphism is synonymous with inheritance. But it’s actually a more general concept that refers to code that can work with data of multiple types. For inheritance, those types are generally subclasses.

[[Rust]] instead uses generics to abstract over different possible types and trait bounds to impose constraints on what those types must provide. This is sometimes called _bounded parametric polymorphism_.