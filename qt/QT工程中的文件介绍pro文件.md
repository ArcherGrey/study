#QT工程中的文件介绍----*.pro文件

> .pro文件

相信学习过QT的同志们，应该自己写了一个最简单的Hello程序。同时也就开始使用了一个命令：qmake –project 。这个命令是用来生成QT的工程文件（.pro）的，这个文件是用来设置编译或者链接的变量，以便用qmake生成相对应的Makefile文件。这个文件的基本内容就是：

    TEMPLATE = app
    
    TARGET =
    
    DEPENDPATH += .
    
    INCLUDEPATH += .
    
     
    
    # Input
    
    SOURCES += main.cpp
    
 

下面我们就通过这个文件一步一步认识.pro这个文件：

TEMPLATE：这个变量是用来定义你的工程将被编译成什么模式。怎么说呢，TEMPLATE=app 表示这个project将被编译成一个应用程序（application）。如果没有这个设置，系统将默认编译为application。当然TEMPLATE还有其他的值：lib(生成库的Makefile) ,subdirs(生成有多级目录管理的Makefile)，vcapp，vclib，vcsubdirs（对应Windows 下面VC）。

TARGET：生成最后目标的名字。
如果要指定生成目标的路径，这加一个DESTDIR（这个用来指定路径）。

DEPENDPATH：工程的依赖路径。

INCLUDEPATH：这个用来指定工程要用到的头文件路径。
 一般是自定义的或者没有放入系统头文件路径的头文件。

SOURCES：工程需要的源文件。

----------


介绍到这里也许你对Pro文件就有一个大概的认识了，但是这还不够，这仅仅只是开始。

比如如何架子资源啊，如何加载语言啊，如何加载ui啊，如何找到图标啊等。

 

当然除了上面的QT变量外，还有另外的变量,这里只介绍常用的：

HEADERS：工程所需要的头文件。

FORMS：工程要用到的ui文件。（ui文件时用QT设计器生成的）。

LIBS：加载动态库。`LIBS +=./mitab/libmitab.so`

TRASHLATIONS：加载要用到的语言翻译*.ts文件。

RESOURCES：加载要用到的资源*.qrc文件。

win32:RC_FILE：加载要用到rc文件（这个只能用在Windows环境）。可以用来配置图标。

CONFIG：告诉qmake应用程序的配置信息。这个变量可以用来指定是生成debug模式还是release模式，也可以都生成。也可以用来打开编译器警告或者关闭。还可以用来配置要Qt加载库。



如果要加载qt的库和你想要多线程：`CONFIG +=qt thread`

如果你要在windows下面运行console：`CONFIG +=console`

QT：用来加载指定的库名，如：xml等，当时前提是要在CONFIG中配置qt值。

          QT += xml network

 

UI_DIR：UIC将ui转化为头文件所存放的目录。

RCC_DIR：RCC将qrc文件转化为头文件所存放的目录。

MOC_DIR：MOC命令将含Q_OBJECT的头文件转换为标准的头文件存放的目录。

OBJECTS_DIR：生成的目标文件存放的目录。

最后，因为QT是跨平台的，所以我们在不同的平台上用同一个pro文件，这要加入有关平台的信息。在windows是win32，Linux平台是unix。