- Base and Derived Classes
`class derived-class: access-specifier base-class`

# Inheritance
-   **public inheritance** makes `public` members of the base class `public` in the derived class, and the `protected` members of the base class remain `protected` in the derived class.
-   **protected inheritance** makes the `public` and `protected` members of the base class `protected` in the derived class.
-   **private inheritance** makes the `public` and `protected` members of the base class `private` in the derived class.
```cpp
class Base {
    public:
        int x;
    protected:
        int y;
    private:
        int z;
};

class PublicDerived: public Base {
    // x is public
    // y is protected
    // z is not accessible from PublicDerived
};

class ProtectedDerived: protected Base {
    // x is protected
    // y is protected
    // z is not accessible from ProtectedDerived
};

class PrivateDerived: private Base {
    // x is private
    // y is private
    // z is not accessible from PrivateDerived
}
```