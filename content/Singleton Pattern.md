---
aliases: []
date created: Jun 7th, 2023
date modified: Jun 7th, 2023
---

## What
A design pattern that restricts a class to instantiate only a single object, or instance. This is useful when exactly one object is needed to coordinate actions across the system.

## How

### Python
```python
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self
```

### Java
1. Private static variable of the same class that is the only instance of the class.
2. Private constructor to restrict instantiation of the class from other classes.
3. Public static method that returns the instance of the class, this is the global access point for the outer world to get the instance of the singleton class.

```java
public class Singleton {
   // Step 1: private static variable of the SAME class that is the only instance of the class.
   private static Singleton singleInstance = null;

   // Step 2: private constructor to restrict instantiation of the class from other classes.
   private Singleton() {
      // optional: add control logic here
   }

   // Step 3: public static method that returns the instance of the class, this is the global access point for outer world to get the instance of the singleton class.
   public static Singleton getInstance() {
      if (singleInstance == null)
         singleInstance = new Singleton();

      return singleInstance;
   }
}
```

## Why
Avoid inconsistent behavior if different parts of the program accessed different instances.  
Ensure that there's only one instance of the settings class that all parts of the program can access.

## Links
- Singleton design pattern is also used in other design patterns like [Abstract Factory](https://www.digitalocean.com/community/tutorials/abstract-factory-design-pattern-in-java), [Builder](https://www.digitalocean.com/community/tutorials/builder-design-pattern-in-java), [Prototype](https://www.digitalocean.com/community/tutorials/prototype-design-pattern-in-java), [Facade](https://www.digitalocean.com/community/tutorials/facade-design-pattern-in-java), etc.