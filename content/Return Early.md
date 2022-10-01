## Return Early
[Return Early Pattern. A rule that will make your code more… | by Leonel Menaia | The Startup | Medium](https://medium.com/swlh/return-early-pattern-3d18a41bba8)
[Structured programming - Wikipedia](https://en.wikipedia.org/wiki/Structured_programming#Early_exit)
- Example

```java
public String returnStuff(SomeObject argument1, SomeObject argument2){
      if (!argument1.isValid()) {
            throw new Exception();
      }

      if (!argument2.isValid()) {
            throw new Exception();
      }

      SomeObject otherVal1 = doSomeStuff(argument1, argument2);

      if (!otherVal1.isValid()) {
            throw new Exception();
      }

      SomeObject otherVal2 = doAnotherStuff(otherVal1);

      if (!otherVal2.isValid()) {
            throw new Exception();
      }

      return "Stuff";
}
```

![](https://img.ynchen.me/2022/08/a066269d4fc0e3462869815112de99e4.png)
- Fail fast
- Single Entry, Single Exit (SESE)

### Disadvantage
- Unable to clean resources