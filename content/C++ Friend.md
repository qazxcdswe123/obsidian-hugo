**A friend class in C++ can access the private and protected members of the class in which it is declared as a friend**.

To declare all member functions of a class (says `Class1`) friend functions of another class (says `Class2`), declared "`friend class Class1;`" in `Class2`.
Friends are not _symmetric_. That is, if `Class1` is a friend of `Class2`, it does not imply that `Class2` is a friend of `Class1`. Friends are also not _transitive_. That is, if `Class1` is a friend of `Class2`, and `Class2` is a friend of `Class3`, it does not imply that `Class1` is a friend of `Class3`.
Use friend with care. Incorrect use of friends may corrupt the concept of _information hiding and encapsulation_.