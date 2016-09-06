# OpenGL--hello 窗口 
基本配置完成后，来通过一个简单的窗口来了解OpenGL的初始化和基本设置。

----------

> 导入所需头文件

    // GLEW
    #define GLEW_STATIC
    #include <GL/glew.h>
    // GLFW
    #include <GLFW/glfw3.h>
    
第二行定义宏是因为要使用GLEW静态的链接库。

----------

> 初始化和基本设置


添加在main函数中

    	glfwInit(); // 初始化GLFW
    	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR,3); // 告诉GLFW使用的OpenGL主版本号是3
    	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR,3); // 次版本号是3，也就是使用OpenGL 3.3
    	glfwWindowHint(GLFW_OPENGL_PROFILE,GLFW_OPENGL_CORE_PROFILE); // 告诉GLFW使用核心模式(Core-proflie)
    	glfwWindowHint(GLFW_RESIZEABLE,GL_FALSE); // 不允许调整窗口大小
    


如果是 mac os x 系统需要加上一条：

    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT,GL_TRUE);

----------
> 创建窗口

    添加在上面代码的后面
    
    // 前两个参数是窗口的宽和高，第三个是标题
    GLFWwindow* window = glfwCreateWindow(800,600,"Hello",nullptr,nullptr); 
    
    // 如果创建失败
    if(window == nullptr)
    {
    	std::cout<<"Fail"<<std::endl;
    	glfwTerminate();
    	return -1;
    }
    
    // 根据窗口设置上下文
    glfwMakeContextCurrent(window);

----------
> 初始化GLEW

GLEW是用来管理OpenGL函数指针的，所以在使用任何OpenGL函数之前需要初始化GLEW。

    添加在上面的代码后面
    // 将这个设置为真，GLEW就会知道去使用现在的方法去获取函数指针和其他扩展。如果设置为假的话，在使用OpenGL核心模式就会有些问题
    glewExperimental = GL_TRUE;
    
    // 初始化GLEW
    if(glewInit()!=GLEW_OK)
    {
    	std::cout<<"Fail"<<std::endl;
    	return -1;
    }

----------

> 设置显示区域（viewport）

也就是OpenGL渲染窗口的大小

    添加在上面的代码之后
    
    int width, height ;
    glfwGetFramebufferSize(window, &width ,&height );
    
    // 前两个参数代表窗口左下角的位置，第三个和第四个控制渲染窗口的宽和高（像素）
    glViewport(0,0,width,height);


----------
> 游戏循环(Game Loop)

我们不希望只绘制一个图像之后应用程序就立即退出并且关闭窗口，我们希望程序在我们发出明确的关闭指令之前不断的绘制图像并且可以接受用户的输入。所以我们需要在程序中添加一个while循环：

    添加在上面的代码之后
    
    // Game Loop
    while(!glfwWindowShouldClose(window))
    {
    	glfwPollEvents();
    	glfwSwapBuffers(window);
    }



- `glfwWindowShouldClose` 函数在我们每次循环的开始前检查一次GLFW是否被要求退出，如果是的话该函数返回true然后游戏循环便结束了，之后为我们就可以关闭应用程序了。
- `glfwPollEvents` 函数检查有没有触发什么事件（比如键盘输入、鼠标移动等），然后调用对应的回调函数（可以通过回调方法手动设置）。我们一般在游戏循环的开始调用事件处理函数。
- `glfwSwapBuffers` 函数会交换颜色缓冲（它是一个储存着GLFW窗口每一个像素颜色的大缓冲），它在这一迭代中被用来绘制，并且将会作为输出显示在屏幕上。



> 双缓冲(Double Buffer)
> 
应用程序使用单缓冲绘图时可能会存在图像闪烁的问题。 这是因为生成的图像不是一下子被绘制出来的，而是按照从左到右，由上而下逐像素地绘制而成的。最终图像不是在瞬间显示给用户，而是通过一步一步生成的，这会导致渲染的结果很不真实。为了规避这些问题，我们应用双缓冲渲染窗口应用程序。前缓冲保存着最终输出的图像，它会在屏幕上显示；而所有的的渲染指令都会在后缓冲上绘制。当所有的渲染指令执行完毕后，我们交换(Swap)前缓冲和后缓冲，这样图像就立即呈显出来，之前提到的不真实感就消除了。

----------
> 最后

结束的时候需要释放所有分配的资源。

    添加在上面的代码之后
    
    // 释放GLFW分配的内存
    glfwTerminate();
    return 0;

结果如下图：

![](http://i.imgur.com/rs1K0dc.jpg)


----------
## 额外的
> 输入

我们希望能够在GLFW中实现一些键盘控制，可以使用GLFW的回调函数来完成。

回调函数实际上是一个函数指针，在设置好了之后，GLFW会在合适的时候调用，按键回调是回调函数中的一种，在设置了按键回调之后，GLFW就会在有键盘交互的时候调用它。

按键回调的函数原型如下：

    void key_callback(GLFWwindow* window, int key, int scancode, int action, int mode);

第一个参数是回调函数作用的窗口，第二个参数是表示按下的按键，action表示是按下还是释放，最后一个参数表示是否有 `Ctrl` , `Shift` , `Alt` , `Super`等按钮的操作。

一个简单的例子：

    void key_callback(GLFWwindow* window, int key, int scancode, int action, int mode)
    {
    	// 当用户按下ESC键,我们设置window窗口的WindowShouldClose属性为true
    	// 关闭应用程序
    	if(key == GLFW_KEY_ESCAPE && action == GLFW_PRESS)
    		glfwSetWindowShouldClose(window, GL_TRUE);
    }   

最后一件事就是通过GLFW注册我们的函数至合适的回调，代码是这样的:

    glfwSetKeyCallback(window, key_callback);  

除了按键回调函数之外，我们还能我们自己的函数注册其它的回调。例如，我们可以注册一个回调函数来处理窗口尺寸变化、处理一些错误信息等。我们可以在创建窗口之后，开始游戏循环之前注册各种回调函数。


----------
> 渲染

我们要把所有的渲染(Rendering)操作放到游戏循环中，因为我们想让这些渲染指令在每次游戏循环迭代的时候都能被执行。代码将会是这样的：

	// 程序循环
	while(!glfwWindowShouldClose(window))
	{
	    // 检查事件
	    glfwPollEvents();

    	// 渲染指令
    	...

    	// 交换缓冲
    	glfwSwapBuffers(window);
	}