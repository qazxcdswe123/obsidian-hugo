## `transient`
When a field is declared transient, it will not be serialized even if the class to which it belongs is serialized.

## `Serializable`
Convert the **state** of an object into a byte stream

```java
public final void writeObject(Object obj) throws IOException

public final Object readObject() throws IOException, ClassNotFoundException
```