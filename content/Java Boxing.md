## Boxing and Unboxing
- Boxing in Java refers to the process of converting a primitive data type into its corresponding wrapper class (e.g., `int` to `Integer`, `double` to `Double`, etc.). 
- Unboxing is the reverse process, converting a wrapper class object back into its corresponding primitive data type (e.g., `Integer` to `int`, `Double` to `double`, etc.)

```java
// boxing
List<Integer> li = new ArrayList<>();
for (int i = 1; i < 50; i += 2)
    li.add(i);

// unboxing
public static int sumEven(List<Integer> li) {
    int sum = 0;
    for (Integer i: li)
        if (i % 2 == 0)
            sum += i;
	return sum;
}
```