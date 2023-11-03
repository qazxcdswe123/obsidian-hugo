---
aliases: []
date created: Dec 3rd, 2022
date modified: Dec 25th, 2022
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
cmake_minimum_required(VERSION 3.14.0 FATAL_ERROR)
```

## Target
```
add_executable(myExecutable main.cpp) 
add_library(libA sourceA.cpp) 
add_library(libB sourceB.cpp sourceB_impl.cpp) 
add_library(libC sourceC.cpp) 
target_link_libraries(myExecutable libA) 
target_link_libraries(libA libB) target_link_libraries(libB libC)
```

This is a classic way of creating targets. Here we have an executable called `myExecutable` and three libraries `libA`, `libB` and `libC`. For now we know, that in order to build `myExecutable` we have to link with `libA`, for building `libA` we have to link with `libB` and for building `libB` we have to link with `libC`. The last one has no dependencies.

Modern CMake introduced also new keywords, that specify visibility of the given target property: `PRIVATE`, `PUBLIC`, `INTERFACE`. If none is provided, then `PUBLIC` is assumed. Their meanings are as follows:
- `PRIVATE` property is only for the internal usage by the property owner,
- `PUBLIC` property is for both internal usage by the property owner and for other targets that use it (link with it),
- `INTERFACE` property is only for usage by other libraries.

> Targets that don’t produce any binaries (e.g. header-only libraries) can have only `INTERFACE` properties and can only use `INTERFACE` linking. This is quite understandable, because there is no “internal” part in such targets, so `PRIVATE` keyword doesn’t mean anything.

what is the visibility of the newly obtained set of properties (by `libA`)? Answer is simple: it’s the same as the specifier used in `target_link_libraries()` for that target. So if `libA` links as `PRIVATE` with `libB`, then all `PUBLIC` and `INTERFACE` properties of `libB` become `PRIVATE` properties of `libA`. Similarly, if it links as `PUBLIC`, then all `PUBLIC` and `INTERFACE` properties of `libB` become `PUBLIC` in `libA`. The same goes for `INTERFACE` linking.

### Library
1. Make it a library `add_library(MathFunctions mysqrt.cxx)`
2. (Optional): `add_subdirectory(MathFunctions)` (need a `CMakeLists.txt` in the sub-directory)
3. Link library to the target `target_link_libraries(Tutorial PUBLIC MathFunctions)`
4. Specify the library's header file location `target_include_directories(Tutorial PUBLIC "${PROJECT_BINARY_DIR}" "${PROJECT_SOURCE_DIR}/MathFunctions")`

#### Optional Library
1. Add an option to the top-level `CMakeLists.txt` file `option(USE_MYMATH "Use tutorial provided math implementation" ON)`.
2. Use `if()` to leverage options

```
if(USE_MYMATH)
  add_subdirectory(MathFunctions)
  list(APPEND EXTRA_LIBS MathFunctions)
  list(APPEND EXTRA_INCLUDES "${PROJECT_SOURCE_DIR}/MathFunctions")
endif()
```

1. Change the library name `target_link_libraries(Tutorial PUBLIC ${EXTRA_LIBS})`.

### Linking
```
add_executable(cmake_testapp main.cpp)
add_library(test_library STATIC calc.cpp)

include_directories(includes/math) 
include_directories(includes/general)

find_library(TEST_LIBRARY test_library lib) target_link_libraries(cmake_testapp LINK_PUBLIC &{TEST_LIBRARY}) # after add_executable
```

- We used [`target_include_directories()`](https://cmake.org/cmake/help/latest/command/target_include_directories.html#command:target_include_directories "target_include_directories") to specify where the executable target should look for include files.
	- The `INTERFACE`, `PUBLIC` and `PRIVATE` keywords are required to specify the [scope](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#target-usage-requirements) of the following arguments. `PRIVATE` and `PUBLIC` items will populate the [`INCLUDE_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/INCLUDE_DIRECTORIES.html#prop_tgt:INCLUDE_DIRECTORIES "INCLUDE_DIRECTORIES") property of `<target>`. `PUBLIC` and `INTERFACE` items will populate the [`INTERFACE_INCLUDE_DIRECTORIES`](https://cmake.org/cmake/help/latest/prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.html#prop_tgt:INTERFACE_INCLUDE_DIRECTORIES "INTERFACE_INCLUDE_DIRECTORIES") property of `<target>`. The following arguments specify include directories.

## Variable
- [`PROJECT_BINARY_DIR`](https://cmake.org/cmake/help/latest/variable/PROJECT_BINARY_DIR.html) : Full path to build directory for project.

## Links
- [Quick CMake tutorial | CLion Documentation](https://www.jetbrains.com/help/clion/quick-cmake-tutorial.html#profiles)  
- [CMake: Public VS Private VS Interface - Lei Mao's Log Book](https://leimao.github.io/blog/CMake-Public-Private-Interface/)