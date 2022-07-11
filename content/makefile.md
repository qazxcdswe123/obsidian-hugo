[[C++ OOP 面向对象]]
[Src](https://seisman.github.io/how-to-write-makefile/introduction.html)
## 关于程序的编译和链接
无论是C还是C++，首先要把源文件编译成中间代码文件，在Windows下也就是 `.obj` 文件，UNIX下是 `.o` 文件，即Object File，这个动作叫做编译（compile）。然后再把大量的Object File合成执行文件，这个动作叫作链接（link）。
链接时，主要是链接函数和全局变量。所以，我们可以使用这些中间目标文件（ `.o` 文件或 `.obj` 文件）来链接我们的应用程序。链接器并不管函数所在的源文件，只管函数的中间目标文件（Object File），在大多数时候，由于源文件太多，编译生成的中间目标文件太多，而在链接时需要明显地指出中间目标文件名，这对于编译很不方便。所以，我们要给中间目标文件打个包，在Windows下这种包叫“库文件”（Library File），也就是 `.lib` 文件，在UNIX下，是Archive File，也就是 `.a` 文件。

# 语法
## 规则
我们的规则是：
1.  如果这个工程没有编译过，那么我们的所有c文件都要编译并被链接。
2.  如果这个工程的某几个c文件被修改，那么我们只编译被修改的c文件，并链接目标程序。
3.  如果这个工程的头文件被改变了，那么我们需要编译引用了这几个头文件的c文件，并链接目标程序。

```
target ... : prerequisites ...
    command
    ...
    ...
```
prerequisites中如果有一个以上的文件比target文件要新的话，command所定义的命令就会被执行。
```
# bad practise

edit : main.o kbd.o command.o display.o \
        insert.o search.o files.o utils.o
    cc -o edit main.o kbd.o command.o display.o \
        insert.o search.o files.o utils.o

main.o : main.c defs.h
    cc -c main.c
kbd.o : kbd.c defs.h command.h
    cc -c kbd.c
command.o : command.c defs.h command.h
    cc -c command.c
display.o : display.c defs.h buffer.h
    cc -c display.c
insert.o : insert.c defs.h buffer.h
    cc -c insert.c
search.o : search.c defs.h buffer.h
    cc -c search.c
files.o : files.c defs.h buffer.h command.h
    cc -c files.c
utils.o : utils.c defs.h
    cc -c utils.c
clean :
    rm edit main.o kbd.o command.o display.o \
        insert.o search.o files.o utils.o
```
## 变量
```
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
## make clean
```
.PHONY : clean
clean :
    -rm edit $(objects)
```
A phony target is one that is not really the name of a file; rather it is just a name for a recipe to be executed when you make an explicit request.
`-` 表示出错继续运行
