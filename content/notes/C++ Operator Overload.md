- `++`
-   The prefix function increments the `count`, and returns this object by reference.
-   The postfix function saves the old value (by constructing a new instance with this object via the copy constructor), increments the `count`, and return the saved object by value.
```c++
Counter & Counter::operator++() {
   ++count;
   return *this;
}
 
// postfix++, return old value by value
const Counter Counter::operator++(int dummy) {
   Counter old(*this); // copy constructor
   ++count;
   return old;
}
```
[Why dummy](https://stackoverflow.com/questions/36816973/purpose-of-dummy-parameter-in-postfix-operator-overload-c)

- `<<`
`friend ostream& operator<<(ostream &out, const Fraction &rhs);`
`ostream& operator<<(ostream &out, const Fraction &rhs)`

- `=`
```c++
// Override the default assignment operator to handle dynamic memory
const MyDynamicArray& MyDynamicArray::operator= (const MyDynamicArray & rhs) {
   if (this != &rhs) {  // no self assignment
      if (size_ != rhs.size_) {
         // reallocate memory for the array
         delete [] ptr;
         size_ = rhs.size_;
         ptr = new double[size_];
      }
      // Copy elements
      for (int i = 0; i < size_; ++i) {
         ptr[i] = rhs.ptr[i];
      }
   }
   return *this;
}
```

```c++
String &String::operator=(const String &other)
{
    if (this != &other)
    {
        if (size != other.len)
        {
            delete[] data;
            len = other.len;
            data = new char[len + 1];
        }
        strcpy(data, other.data);
    }
    return *this;
}
```
