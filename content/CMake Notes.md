---
aliases: []
tags: []
date created: Dec 3rd, 2022
date modified: Dec 3rd, 2022
---
**Note:** Although upper, lower and mixed case commands are supported by CMake, lower case commands are preferred and will be used throughout the tutorial.

Any project's top most CMakeLists.txt must start by specifying a minimum CMake version using the [`cmake_minimum_required()`](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html#command:cmake_minimum_required "cmake_minimum_required") command. This establishes policy settings and ensures that the following CMake functions are run with a compatible version of CMake.

To start a project, we use the [`project()`](https://cmake.org/cmake/help/latest/command/project.html#command:project "project") command to set the project name. This call is required with every project and should be called soon after [`cmake_minimum_required()`](https://cmake.org/cmake/help/latest/command/cmake_minimum_required.html#command:cmake_minimum_required "cmake_minimum_required"). As we will see later, this command can also be used to specify other project level information such as the language or version number.

Finally, the [`add_executable()`](https://cmake.org/cmake/help/latest/command/add_executable.html#command:add_executable "add_executable") command tells CMake to create an executable using the specified source code files.

```sh
# Generate build files
cmake /path/to/CMakeLists.txt
# Compile/link
cmake --build .
```

## CMake Configuration
```
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
project(Tutorial VERSION 1.0)
configure_file(TutorialConfig.h.in TutorialConfig.h)
```

## Linking
```
add_executable(cmake_testapp main.cpp)
add_library(test_library STATIC calc.cpp)

include_directories(includes/math) include_directories(includes/general)

find_library(TEST_LIBRARY test_library lib) target_link_libraries(cmake_testapp LINK_PUBLIC &{TEST_LIBRARY}) # after add_executable
```

## Links
[Quick CMake tutorial | CLion Documentation](https://www.jetbrains.com/help/clion/quick-cmake-tutorial.html#profiles)