# Kaggle 101 - Digit Recognizer
机器学习的书也看了一段时间了，还是觉得要实际操作下才能有更深的体会，kaggle 正好提供了一个练习的平台，先从 101 开始学习。。

## 数据部分
它提供了训练数据和测试数据，还有一个样本提交的例子。

这些数据是手写数字1-9的灰度图。每个图是 28X28 共 784 个像素。存在一个 `.csv` 文件中。灰度值的范围是 0-255。

训练集有785列，第一列是数据项的名称，从第二列开始是具体的数据，每一列第一个是 `label` 也就是对应数字的正确答案，后面的是每一个图片具体的像素值（按行存储）。

测试集就没有 `label` 了，其他的和训练集一个形式。

需要提交的文件形式如下：

![](http://i.imgur.com/OgXql96.png)

## 开始
[python CSV 文件读写](http://blog.csdn.net/gr47725812/article/details/51906814)

是根据网上看别人写的[例子](http://blog.csdn.net/u012162613/article/details/41978235)和[scikit-learn的例子](http://blog.csdn.net/gr47725812/article/details/51902493)，只使用了svc，用的自己的笔记本四核八线程 I7，算了将近20分钟。（之前没有归一化收敛不了）

代码：
<pre>
from numpy import *
import csv
# 数据处理部分
def toInt(array):  
    array=mat(array)  
    m,n=shape(array)  
    newArray=zeros((m,n))  
    for i in xrange(m):  
        for j in xrange(n):  
                newArray[i,j]=int(array[i,j])  
    return newArray  
    
def nomalizing(array):  
    m,n=shape(array)  
    for i in xrange(m):  
        for j in xrange(n):  
            if array[i,j]!=0:  
                array[i,j]=1  
    return array  
    
def loadTrainData():
    a=[]
    with open('train.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            a.append(line)
    a.remove(a[0])
    a = array(a)
    label = a[:,0]
    data = a[:,1:]
    return nomalizing(toInt(data)),toInt(label)
    
def loadTestData():
    a=[]
    with open('test.csv') as file:
        lines = csv.reader(file)
        for line in lines:
            a.append(line)
    a.remove(a[0])
    data = array(a)
    return nomalizing(toInt(data))

    
def saveResult(result,csvName):  
    with open(csvName,'wb') as myFile:      
        myWriter=csv.writer(myFile)
        myWriter.writerow(["ImageId","Label"])
        index = 1
        for i in result:  
            tmp=[index]  
            tmp.append(i)  
            myWriter.writerow(tmp) 
            index = index + 1
            
# 学习测试部分
from sklearn import svm
trainData, trainLaber = loadTrainData()
testData = loadTestData()
classifier = svm.SVC()
classifier.fit(trainData, ravel(trainLaber))
predicted = classifier.predict(testData)
saveResult(predicted,'SVC_Result.csv') 
</pre>

