---
aliases: []
tags: [] 
date created: Aug 15th, 2022
date modified: Aug 20th, 2022
---
> [Don’t confuse scop e with lifet ime. The scope of a declarat ion is a reg ion of the program text; it is a compi le-t ime pro per ty. The lifet ime of a var iable is the range of time dur ing exe cut ion when the var iable can be refer red to by other par ts of the program; it is a run-t ime pro per ty.](marginnote3app://note/096C2F2A-E997-4B88-8299-956AB56902E8)

Similar With: [[Python Namespace]], [[JavaScript Hoisting]]
# General
## Variables
Variables may be internal to a function, external but known only within a single source file, or visible to the entire program.

By default, external variables and functions have the property that all references to them by the same name, even from functions compiled separately, are references to the same thing. (The standard calls this property external linkage.)

## Static
The static declaration, applied to an external variable or function, limits the scope of that object to the rest of the source file being compiled.

## Lexical Scope
[javascript - What is lexical scope? - Stack Overflow](https://stackoverflow.com/questions/1047454/what-is-lexical-scope)
- AKA static scope

```javascript
void fun()
{
    int x = 5;

    void fun2()
    {
        printf("%d", x);
    }
}
```

- Contract: dynamic scope  

```javascript
void fun()
{
    printf("%d", x);
}

void dummy1()
{
    int x = 5;

    fun();
}

void dummy2()
{
    int x = 10;

    fun();
}
```

The first one is called static because it can be deduced at compile-time, and the second is called dynamic because the outer scope is dynamic and depends on the chain call of the functions.
# Language Specific
## C
### Extern Keyword
[How to correctly use the extern keyword in C - Stack Overflow](https://stackoverflow.com/questions/496448/how-to-correctly-use-the-extern-keyword-in-c)
> `extern` changes the linkage. With the keyword, the function / variable is assumed to be available somewhere else and the resolving is deferred to the linker.  
> There's a difference between `extern` on functions and on variables.  
> For **variables** it doesn't instantiate the variable itself, i.e. doesn't allocate any memory. This needs to be done somewhere else. Thus it's important if you want to import the variable from somewhere else.  
> For **functions**, this only tells the compiler that linkage is extern. As this is the default (you use the keyword `static` to indicate that a function is not bound using extern linkage) you don't need to use it explicitly.

Point to the same variable, instead of a different copy.
