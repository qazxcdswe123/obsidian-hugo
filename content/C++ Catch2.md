---
aliases: []
tags: []
date created: Sep 16th, 2022
date modified: Sep 16th, 2022
---
[GitHub - catchorg/Catch2: A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14, C++17 and later (C++11 support is in v2.x branch, and C++03 on the Catch1.x branch)](https://github.com/catchorg/Catch2)

## Tutorial
Like most test frameworks, Catch2 supports a class-based fixture mechanism, where individual tests are methods on class and setup/teardown can be done in constructor/destructor of the type.

However, their use in Catch2 is rare, because idiomatic Catch2 tests instead use _sections_ to share setup and teardown code between test code. This is best explained through an example ([code](https://github.com/catchorg/Catch2/blob/devel/examples/100-Fix-Section.cpp)):

```c++
TEST_CASE( "vectors can be sized and resized", "[vector]" ) {
    std::vector<int> v( 5 );

    REQUIRE( v.size() == 5 );
    REQUIRE( v.capacity() >= 5 );

    SECTION( "resizing bigger changes size and capacity" ) {
        v.resize( 10 );

        REQUIRE( v.size() == 10 );
        REQUIRE( v.capacity() >= 10 );
    }
    SECTION( "resizing smaller changes size but not capacity" ) {
        v.resize( 0 );

        REQUIRE( v.size() == 0 );
        REQUIRE( v.capacity() >= 5 );
    }
    SECTION( "reserving bigger changes capacity but not size" ) {
        v.reserve( 10 );

        REQUIRE( v.size() == 5 );
        REQUIRE( v.capacity() >= 10 );
    }
    SECTION( "reserving smaller does not change size or capacity" ) {
        v.reserve( 0 );

        REQUIRE( v.size() == 5 );
        REQUIRE( v.capacity() >= 5 );
    }
}
```

For each `SECTION` the `TEST_CASE` is executed from the start. This means that each section is entered with a freshly constructed vector `v`, that we know has size 5 and capacity at least 5, because the two assertions are also checked before the section is entered. Each run through a test case will execute one, and only one, leaf section.