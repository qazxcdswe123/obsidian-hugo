---
aliases: []
tags: []
date created: Apr 22nd, 2022
date modified: Dec 3rd, 2022
---
[[CMake Notes]]
[Src](https://seisman.github.io/how-to-write-makefile/introduction.html)

## 关于程序的编译和链接
无论是 C 还是 C++，首先要把源文件编译成中间代码文件，在 Windows 下也就是 `.obj` 文件，UNIX 下是 `.o` 文件，即 Object File，这个动作叫做编译（compile）。然后再把大量的 Object File 合成执行文件，这个动作叫作链接（link）。  
链接时，主要是链接函数和全局变量。所以，我们可以使用这些中间目标文件（ `.o` 文件或 `.obj` 文件）来链接我们的应用程序。链接器并不管函数所在的源文件，只管函数的中间目标文件（Object File），在大多数时候，由于源文件太多，编译生成的中间目标文件太多，而在链接时需要明显地指出中间目标文件名，这对于编译很不方便。所以，我们要给中间目标文件打个包，在 Windows 下这种包叫“库文件”（Library File），也就是 `.lib` 文件，在 UNIX 下，是 Archive File，也就是 `.a` 文件。

## 规则
我们的规则是：
1. 如果这个工程没有编译过，那么我们的所有 c 文件都要编译并被链接。
2. 如果这个工程的某几个 c 文件被修改，那么我们只编译被修改的 c 文件，并链接目标程序。
3. 如果这个工程的头文件被改变了，那么我们需要编译引用了这几个头文件的 c 文件，并链接目标程序。

```
target ... : prerequisites ...
    command
    ...
    ...
```

prerequisites 中如果有一个以上的文件比 target 文件要新的话，command 所定义的命令就会被执行。

```
# bad practise

edit : main.o kbd.o command.o display.o 
    cc -o edit main.o kbd.o command.o display.o 

main.o : main.c defs.h
    cc -c main.c
kbd.o : kbd.c defs.h command.h
    cc -c kbd.c
command.o : command.c defs.h command.h
    cc -c command.c
display.o : display.c defs.h buffer.h
    cc -c display.c
clean :
    rm edit main.o kbd.o command.o display.o 
```

## 变量
``

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

A phony target is one that is not really the name of a file; rather it is just a name for a recipe to be executed when you make an explicit request.  
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

## Recursive Use of Make