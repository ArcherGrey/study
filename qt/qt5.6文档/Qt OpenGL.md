# Qt OpenGL
> 警告： 这个模块不应该使用任何自定义的代码。请使用 `Qt GUI` 中相应的 `OpenGL` 类
> 
>  `OpenGL` 是一个用来绘制3D图形的标准API。 `OpenGL` 只处理3D绘制和很少或者不能支持GUI程序问题。一个 `OpenGL` 应用的用户接口必须要通过其他工具包来创建，例如 Cocoa 在 OS 平台，MFC 在Windows平台，或者Qt跨平台。
> 
> 注意： `OpenGL` 是硅谷图形公司的注册商标，在美国或者其他国家。
> 
> Qt的 `OpenGL` 模块使得在qt应用中使用 `OpenGL`十分容易。它提供了一个 `OpenGL` 控件类使得使用起来和其他qt控件一样方便，除了打开一个 `OpenGL` 显示缓存，你可以使用 `OpenGL` 自己的API来提供内容。
> 
> 通过下面的语句来导入模块类：
> 
>     #include <QtOpenGL>
> 
> 为了链接模块，需要在qmake的 `.pro` 文件中添加：
> 
>     QT += opengl
> 
> qt的 `OpenGL` 模块是跨平台的Qt/C++包含平台依赖GLX，WGL或者AGL C的接口的实现。虽然所提供的基本功能和Mark Kilgard的GLUT库非常相似，应用程序使用Qt OpenGL模块对于非OpenGL特定的GUI功能可以充分的发挥所有qt接口的优势。