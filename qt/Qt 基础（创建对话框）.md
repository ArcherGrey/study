# Qt 基础（创建对话框）

> 子类化 Dialog

也就是自定义一个 dialog，例子是一个查找对话框。

先来写头文件 finddialog.h

<pre>
// 防止对头文件的多重包含
 #ifndef FINDDIALOG_H
 #define FINDDIALOG_H

// QDialog是基类，所以要导入
 #include < QDialog>

// 前置声明一些用于该对话框实现的Qt类，编译速度更快
class QCheckBox;
class QLabel;
class QLineEdit;
class QPushButton;

// 定义FindDialog类，继承于QDialog
class FindDialog : public QDialog
{

//对于所有定义了信号和槽的类，类定义开始处的Q_OBJECT宏都是必须的
    Q_OBJECT

public:

// 典型的Qt窗口部件类的定义方式。parent指定了它的父类窗口部件，默认值是一个空指针，意味着该对话框没有父对象
    FindDialog(QWidget *parent = 0);

// signals实际上是一个宏，这里声明了两个信号，对应向前查询和向后查询，第二个参数是一个枚举类型，表示可能的情况。
signals:
    void findNext(const QString &str, Qt::CaseSensitivity cs);
    void findPrevious(const QString &str, Qt::CaseSensitivity cs);

// slots也是一个宏
private slots:
    void findClicked();
    void enableFindButton(const QString &text);

private:
    QLabel *label;
    QLineEdit *lineEdit;
    QCheckBox *caseCheckBox;
    QCheckBox *backwardCheckBox;
    QPushButton *findButton;
    QPushButton *closeButton;
};

#endif

</pre>

在来看看对应的源文件，其中包含了类的实现：

<pre>
// 包含了所有需要使用的控件，不过实际开发中应该针对性选择
#include < QtGui>

#include "finddialog.h"

FindDialog::FindDialog(QWidget *parent)
    : QDialog(parent)
{
    label = new QLabel(tr("Find &what:"));// tr()是翻译中间的文字
    lineEdit = new QLineEdit;
    label->setBuddy(lineEdit);

    caseCheckBox = new QCheckBox(tr("Match &case"));// &是快捷键
    backwardCheckBox = new QCheckBox(tr("Search &backward"));

    findButton = new QPushButton(tr("&Find"));
    findButton->setDefault(true);
    findButton->setEnabled(false);

    closeButton = new QPushButton(tr("Close"));

    connect(lineEdit, SIGNAL(textChanged(const QString &)),
            this, SLOT(enableFindButton(const QString &)));
    connect(findButton, SIGNAL(clicked()),
            this, SLOT(findClicked()));
    connect(closeButton, SIGNAL(clicked()),
            this, SLOT(close()));

    QHBoxLayout *topLeftLayout = new QHBoxLayout;
    topLeftLayout->addWidget(label);
    topLeftLayout->addWidget(lineEdit);

    QVBoxLayout *leftLayout = new QVBoxLayout;
    leftLayout->addLayout(topLeftLayout);
    leftLayout->addWidget(caseCheckBox);
    leftLayout->addWidget(backwardCheckBox);

    QVBoxLayout *rightLayout = new QVBoxLayout;
    rightLayout->addWidget(findButton);
    rightLayout->addWidget(closeButton);
    rightLayout->addStretch();

    QHBoxLayout *mainLayout = new QHBoxLayout;
    mainLayout->addLayout(leftLayout);
    mainLayout->addLayout(rightLayout);
    setLayout(mainLayout);

    setWindowTitle(tr("Find"));
    setFixedHeight(sizeHint().height());
}

void FindDialog::findClicked()
{
    QString text = lineEdit->text();
    Qt::CaseSensitivity cs =
            caseCheckBox->isChecked() ? Qt::CaseSensitive
                                      : Qt::CaseInsensitive;
    if (backwardCheckBox->isChecked()) {
        emit findPrevious(text, cs);
    } else {
        emit findNext(text, cs);
    }
}

void FindDialog::enableFindButton(const QString &text)
{
    findButton->setEnabled(!text.isEmpty());
}
</pre>


