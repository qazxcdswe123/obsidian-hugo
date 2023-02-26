# Javadoc
1. The first paragraph is a description of the method documented.
2. Following the description are a varying number of descriptive tags, signifying:
    1. The parameters of the method (`@param`)
    2. What the method returns (`@return`)
    3. Any exceptions the method may throw (`@throws`)
    4. Other less-common tags such as `@see` (a "see also" tag)

```java
// import statements

/**
 * @author      Firstname Lastname <address @ example.com>
 * @version     1.6                 (current version number of program)
 * @since       1.2          (the version of the package this class was first added to)
 */

/**
 * Short one line description.                           (1)
 * <p>
 * Longer description. If there were any, it would be    (2)
 * here.
 * <p>
 * And even more explanations to follow in consecutive
 * paragraphs separated by HTML paragraph breaks.
 *
 * @param  variable Description text text text.          (3)
 * @return Description text text text.
 */
public int methodName (...) {
    // method body with a return statement
}
```