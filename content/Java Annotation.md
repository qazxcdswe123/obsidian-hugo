```java
@Author(
   name = "Benjamin Franklin",
   date = "3/27/2003"
)
class MyClass { ... }

myString = (@NonNull String) str;
void monitorTemperature() throws @Critical TemperatureException { ... }
class UnmodifiableList<T> implements @Readonly List<@Readonly T> { ... }
```

The predefined annotation types defined in `java.lang` are `@Deprecated`, `@Override`, and `@SuppressWarnings`.