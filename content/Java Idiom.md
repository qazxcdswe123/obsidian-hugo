## `equals()` And `hashCode()` Contracts
- If two objects are equal according to the `equals()` method, then their hash codes must be equal as well.
- If two objects have the same hash code, they may or may not be equal according to the `equals()` method.

## `equals`
```java
@Override
public boolean equals(Object o) {
	if (this == o) return true;
	if (!(o instanceof Dog)) return false;
	Dog dog = (Dog) o;
	return getAge() == dog.getAge() && getName().equals(dog.getName()) && getBreed().equals(dog.getBreed());
    }
```

## `hashCode`
```java
@Override
public int hashCode() {
	final int prime = 31;
	int result = 1;
	result = (prime * result) + columnIndex;
	result = (prime * result) + rowIndex;
	return result;
}
```

## Links
- [Java Practices->Defensive copying](http://www.javapractices.com/topic/TopicAction.do?Id=15)
- [Java Practices->Copy constructors](http://www.javapractices.com/topic/TopicAction.do?Id=12)
- [Java Practices->Factory methods](http://www.javapractices.com/topic/TopicAction.do?Id=21)