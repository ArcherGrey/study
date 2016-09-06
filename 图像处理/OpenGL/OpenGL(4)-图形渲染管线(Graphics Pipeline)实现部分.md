# 图形渲染管线(Graphics Pipeline)实现

> 顶点输入

绘制图像之前，需要输入顶点数据。OpenGL中所有的坐标都是3D坐标（x,y,z）。只有坐标在（-1,1）范围内才会处理，也就是所有在所谓的标准化设备坐标(Normalized Device Coordinates)范围内的坐标才会最终呈现在屏幕上（在这个范围以外的坐标都不会显示）。

如果要渲染一个三角形，要指定三个顶点，每个顶点都有一个3D位置。我们会将它们以标准化设备坐标的形式（OpenGL的可见区域）定义为一个GLfloat数组。

	GLfloat vertices[] = {
    -0.5f, -0.5f, 0.0f,
     0.5f, -0.5f, 0.0f,
     0.0f,  0.5f, 0.0f
	};

渲染的是一个2D三角形，所以z坐标都是0，这样的话所有的顶点都会有一样的深度(即z坐标相同)，从而使它看上去像是2D的。（因为只有一个图形所以z即使设置不一样看起来也是2D的）



> 标准化设备坐标(Normalized Device Coordinates, NDC)
> 
一旦你的顶点坐标已经在顶点着色器中处理过，它们就应该是标准化设备坐标了，标准化设备坐标是一个x、y和z值在-1.0到1.0的一小段空间。任何落在范围外的坐标都会被丢弃/裁剪，不会显示在你的屏幕上。与通常的屏幕坐标不同，y轴正方向为向上，(0, 0)坐标是这个图像的中心，而不是左上角。最终你希望所有(变换过的)坐标都在这个坐标空间中，否则它们就不可见了。
你的标准化设备坐标接着会变换为屏幕空间坐标(Screen-space Coordinates)，这是使用你通过glViewport函数提供的数据，进行视口变换(Viewport Transform)完成的。所得的屏幕空间坐标又会被变换为片段输入到片段着色器中。

----------
> 顶点缓存对象（VBO）

定义这样的顶点数据以后，我们会把它作为输入发送给图形渲染管线的第一个处理阶段：顶点着色器。它会在GPU上创建内存用于储存我们的顶点数据，还要配置OpenGL如何解释这些内存，并且指定其如何发送给显卡。顶点着色器接着会处理我们在内存中指定数量的顶点。

我们通过顶点缓冲对象(Vertex Buffer Objects, VBO)管理这个内存，它会在GPU内存(通常被称为显存)中储存大量顶点。

可以使用glGenBuffers函数和一个缓冲ID生成一个VBO对象：

    GLuint VBO;
    glGenBuffers(1, &VBO);  

OpenGL允许我们同时绑定多个缓冲，只要它们是不同的缓冲类型。顶点缓冲对象的缓冲类型是GL_ARRAY_BUFFER。我们可以使用glBindBuffer函数把新创建的缓冲绑定到GL_ARRAY_BUFFER目标上：

	glBindBuffer(GL_ARRAY_BUFFER, VBO);  

从这一刻起，我们使用的任何（在GL_ARRAY_BUFFER目标上的）缓冲调用都会用来配置当前绑定的缓冲(VBO)。然后我们可以调用glBufferData函数，它会把之前定义的顶点数据复制到缓冲的内存中：

	glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

glBufferData是一个专门用来把用户定义的数据复制到当前绑定缓冲的函数。它的第一个参数是目标缓冲的类型：顶点缓冲对象当前绑定到GL_ARRAY_BUFFER目标上。第二个参数指定传输数据的大小(以字节为单位)；用一个简单的sizeof计算出顶点数据大小就行。第三个参数是我们希望发送的实际数据。

第四个参数指定了我们希望显卡如何管理给定的数据。它有三种形式：

- GL_STATIC_DRAW ：数据不会或几乎不会改变。
- GL_DYNAMIC_DRAW：数据会被改变很多。
- GL_STREAM_DRAW ：数据每次绘制时都会改变。

如果，比如说一个缓冲中的数据将频繁被改变，那么使用的类型就是GL_DYNAMIC_DRAW或GL_STREAM_DRAW，这样就能确保显卡把数据放在能够高速写入的内存部分。

----------
> 顶点着色器

非常基础的GLSL顶点着色器的源代码：

	// 版本声明，和OpenGL版本匹配
	#version 330 core

	// 顶点是三维的所以是vec3
	layout (location = 0) in vec3 position;

	void main()
	{
    	gl_Position = vec4(position.x, position.y, position.z, 1.0);
	}

----------
> 编译顶点着色器

	// 创建一个ID
    GLuint vertexShader;
	// 用这个ID和一个顶点着色器对象绑定
    vertexShader = glCreateShader(GL_VERTEX_SHADER);
	// 将着色器源码和对象绑定，第一个参数是要附加的着色器对象，第二个参数是源码的数量，第三个参数是源码名
	glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
	// 编译
	glCompileShader(vertexShader);

----------
> 片段着色器

片段着色器是用来计算最后的像素颜色输出。

基本源码：

	// 也是版本绑定
	#version 330 core

	// 输出的颜色是4维向量也就是RGBA（红绿蓝和透明度）
	out vec4 color;

	void main()
	{
		// 具体的颜色，这里是橘黄色
	    color = vec4(1.0f, 0.5f, 0.2f, 1.0f);
	}

----------
> 编译片段着色器

	// 和顶点着色器一样也是先创建一个ID
	GLuint fragmentShader;
	// 和顶点着色器一样，创建着色器对象，区别是创建的类型不一样，这里类型是片段着色器
	fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
	// 一样，绑定对应源码，然后编译
	glShaderSource(fragmentShader, 1, &fragmentShaderSource, null);
	glCompileShader(fragmentShader);

----------
> 着色器程序

着色器程序对象是多个着色器合并之后经过链接完成的版本。

	// 创建着色器程序对象，也是通过ID来引用
	GLuint shaderProgram;
	shaderProgram = glCreateProgram();
	// 将之前编译好的着色器程序添加到新建的着色器程序对象中
	glAttachShader(shaderProgram, vertexShader);
	glAttachShader(shaderProgram, fragmentShader);
	// 链接到源程序上
	glLinkProgram(shaderProgram);
	// 激活这个对象
	glUseProgram(shaderProgram);

	// 在使用完了之后需要删除
	glDeleteShader(vertexShader);
	glDeleteShader(fragmentShader);


----------
> 链接顶点属性

顶点着色器允许我们指定任何以顶点属性为形式的输入。这使其具有很强的灵活性的同时，它还的确意味着我们必须手动指定输入数据的哪一个部分对应顶点着色器的哪一个顶点属性。所以，我们必须在渲染前指定OpenGL该如何解释顶点数据。

使用glVertexAttribPointer函数告诉OpenGL该如何解析顶点数据（应用到逐个顶点属性上）：

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid*)0);
    glEnableVertexAttribArray(0);

glVertexAttribPointer函数的参数：

- 第一个参数指定我们要配置的顶点属性。layout(location = 0)定义了position顶点属性
- 第二个参数指定顶点属性的大小。顶点属性是一个vec3，它由3个值组成，所以大小是3。
- 第三个参数指定数据的类型，这里是GL_FLOAT(GLSL中vec*都是由浮点数值组成的)。
- 下个参数定义我们是否希望数据被标准化(Normalize)。如果我们设置为GL_TRUE，所有数据都会被映射到0（对于有符号型signed数据是-1）到1之间。我们把它设置为GL_FALSE。
- 第五个参数叫做步长(Stride)，也就是一个顶点数据的大小是3个GLfloat。
- 最后一个参数表示位置数据在缓冲中起始位置的偏移量(Offset)。


----------
> 顶点数组对象

顶点数组对象(Vertex Array Object, VAO)可以像顶点缓冲对象那样被绑定，任何随后的顶点属性调用都会储存在这个VAO中。这样的好处就是，当配置顶点属性指针时，你只需要将那些调用执行一次，之后再绘制物体的时候只需要绑定相应的VAO就行了。这使在不同顶点数据和属性配置之间切换变得非常简单，只需要绑定不同的VAO就行了。刚刚设置的所有状态都将存储在VAO中

创建一个VAO和创建一个VBO很类似：

    GLuint VAO;
    glGenVertexArrays(1, &VAO);  

要想使用VAO，要做的只是使用glBindVertexArray绑定VAO。从绑定之后起，我们应该绑定和配置对应的VBO和属性指针，之后解绑VAO供之后使用。当我们打算绘制一个物体的时候，我们只要在绘制物体前简单地把VAO绑定到希望使用的设定上就行了。这段代码应该看起来像这样：

<pre><code>
// ..:: 初始化代码（只运行一次 (除非你的物体频繁改变)） :: ..
// 1. 绑定VAO
glBindVertexArray(VAO);
    // 2. 把顶点数组复制到缓冲中供OpenGL使用
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    // 3. 设置顶点属性指针
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(GLfloat), (GLvoid*)0);
    glEnableVertexAttribArray(0);
//4. 解绑VAO
glBindVertexArray(0);

[...]

// ..:: 绘制代（游戏循环中） :: ..
// 5. 绘制物体
glUseProgram(shaderProgram);
glBindVertexArray(VAO);
someOpenGLFunctionThatDrawsOurTriangle();
glBindVertexArray(0);

</code></pre>

----------
> 绘图

    glUseProgram(shaderProgram);
    glBindVertexArray(VAO);
    glDrawArrays(GL_TRIANGLES, 0, 3);
    glBindVertexArray(0);  

glDrawArrays函数第一个参数是我们打算绘制的OpenGL图元的类型。由于我们在一开始时说过，我们希望绘制的是一个三角形，这里传递GL_TRIANGLES给它。第二个参数指定了顶点数组的起始索引，我们这里填0。最后一个参数指定我们打算绘制多少个顶点，这里是3（我们只从我们的数据中渲染一个三角形，它只有3个顶点长）。


----------
> 索引缓冲对象

