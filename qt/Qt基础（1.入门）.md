# QT基础 ==> 1.入门
> Hello Qt

    //导入包含QApplication和QLabel的头文件
    #include<QApplication>  
    #include<QLabel>
    
    int main(int argc, char *argv)
    {
    	QApplication app(argc, argv);// 用来管理整个应用程序所用到的资源，后面的参数是Qt支持的一些命令行参数
    	QLabel *label = new QLabel("Hello Qt!");//创建一个QLabel窗口部件
    	label->show();//使创建的部件可见
    	return app.exec();//进入事件循环状态，等待用户动作
    }



----------
> 响应用户动作
    
    #include <QApplication>
    #include <QPushButton>
    
    int main(int argc, char *argv)
    {
    	QApplication app(argc, argv);
    	QPushButton *button = new QPushButton("Quit");//创建一个quit按钮
    	QObject::connect(button, SIGNAL(clicked()), &app, SLOT(quit()));//将信号和槽绑定
    	button->show();//使按钮可见
    	return app.exec();//进入事件循环状态，等待用户动作
    }

点击按钮会发送clicked()信号，将信号和槽绑定后，收到信号就会执行对应的槽。


----------
> 窗口部件的布局

