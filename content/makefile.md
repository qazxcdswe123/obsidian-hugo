---
link:
  - "[[CMake]]"
aliases: []
date created: Apr 22nd, 2022
date modified: Aug 9th, 2023
---

```
target ... : prerequisites ...
    command
```

prerequisites 中如果有一个以上的文件比 target 文件要新的话，command 所定义的命令就会被执行。

## 变量

```
:= append
= recursive find

objects = main.o kbd.o command.o display.o \
     insert.o search.o files.o utils.o

edit : $(objects)
    cc -o edit $(objects)
```

## 自动推导
.o 文件自动知道编译命令

```
objects = main.o kbd.o command.o display.o \
    insert.o search.o files.o utils.o

aout : $(objects)
    cc -o aout $(objects)

main.o : defs.h
kbd.o : defs.h command.h
command.o : defs.h command.h
display.o : defs.h buffer.h
insert.o : defs.h buffer.h
search.o : defs.h buffer.h
files.o : defs.h buffer.h command.h
utils.o : defs.h

.PHONY : clean
clean :
    -rm edit $(objects)
```

## Make Clean

```
.PHONY : clean
clean :
    -rm edit $(objects)
```

### `phony`
A phony target is one that is **not the name of a file; rather it is just a name for a recipe to be executed when you make an explicit request.**  
`-` 表示出错继续运行

## Variable
- `$@` is an [automatic variable](https://makefiletutorial.com/#automatic-variables) that contains the target name.
- `$^` The names of all the prerequisites, with spaces between them.

- `CC`: Program for compiling C programs; default `cc`
- `CXX`: Program for compiling C++ programs; default `g++`
- `CFLAGS`: Extra flags to give to the C compiler
- `CXXFLAGS`: Extra flags to give to the C++ compiler
- `CPPFLAGS`: Extra flags to give to the C preprocessor
- `LDFLAGS`: Extra flags to give to compilers when they are supposed to invoke the linker

## Static Pattern Rule

```
objects = foo.o bar.o all.o
all: $(objects)

# These files compile via implicit rules
# Syntax - targets ...: target-pattern: prereq-patterns ...
# In the case of the first target, foo.o, the target-pattern matches foo.o and sets the "stem" to be "foo".
# It then replaces the '%' in prereq-patterns with that stem
$(objects): %.o: %.c

all.c:
	echo "int main() { return 0; }" > all.c

%.c:
	touch $@

clean:
	rm -f *.c *.o all
```
