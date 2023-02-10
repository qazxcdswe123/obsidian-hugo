## Downcasting
```java
class Animal {}

class Dog3 extends Animal {
    static void method(Animal a) {
        if (a instanceof Dog3) {
            Dog3 d = (Dog3) a; //downcasting  
            System.out.println("ok downcasting performed");
        }
    }

    public static void main(String[] args) {
        Animal a = new Dog3();
        Dog3.method(a);
    }
}
```

## Keyword
### `Transient`
The `transient` keyword in Java is used to indicate that a field should not be part of the serialization (which means saved, like to a file) process.