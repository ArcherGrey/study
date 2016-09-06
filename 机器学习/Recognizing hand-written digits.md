# （手写数字识别）Recognizing hand-written digits

这个例子是用来展示 使用`scikit-learn` 是如何用来进行手写数字识别的。


----------
python code:

    # 导入各种需要的模块
    import matplotlib.pyplot as plt
    from sklearn import datasets, svm, metrics
    
    # 需要使用的数字数据集
    digits = datasets.load.digits()
    
    # 这个数据集是模块自带的，都是 8X8 大小的数字图片。如果是直接读取图片文件可以使用pylab.imread。在自带的数据集中target代表每个图片实际的数字。


    # 图片矩阵和图片实际代表数字对应存成list
    images_and_labels = list(zip(digit.images, digit.target))
    
    # 输出数据集中前四个图片,enumerate函数用于遍历序列中的下标以及元素
    for index,(image, label) in enumerate(images_and_labels[:4]):

    # 每行4个输出2行
        plt.subplot(2, 4, index + 1)
        plt.axis('off')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Training: %i' % label)

    # 为了能够使用分类器来处理数据，需要使图片变成（样本，特征）的矩阵
    
    # 样本数量
    n_sample = len(digits.images)

    # 根据样本数量新建一个同样列数的矩阵，（n_samples,-1）代表是n_samples列，行数根据images推断
    data = digits.images.reshape((n_samples,-1))

    # 创建一个支持向量分类器
    classifier = svm.SVC(gamma=0.001)
    
    # 通过前一半数据集进行学习
    classifier.fit(data[:n_samples / 2], digits.target[:n_samples / 2])

    # 对后面一半数据集进行预测
    expected = digits.target[n_samples / 2:]
    predicted = classifier.predict(data[n_samples / 2:])
    
    # 输出分类器相关信息
    print("Classification report for classifier %s:\n%s\n"
      % (classifier, metrics.classification_report(expected, predicted)))

    # 输出混淆矩阵
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))
    

    # 输出对后半部分预测结果的前4张图
    images_and_predictions = list(zip(digits.images[n_samples / 2:], predicted))
    for index, (image, prediction) in enumerate(images_and_predictions[:4]):
        plt.subplot(2, 4, index + 5)
        plt.axis('off')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Prediction: %i' % prediction)

    plt.show()


> 补充：


> 混淆矩阵（Confusion Matrix）:
在图像精度评价中，主要用于比较分类结果和实际测得值，可以把分类结果的精度显示在一个混淆矩阵里面。混淆矩阵是通过将每个实测像元的位置和分类与分类图像中的相应位置和分类像比较计算的。混淆矩阵的每一列代表了预测类别[1]  ，每一列的总数表示预测为该类别的数据的数目；每一行代表了数据的真实归属类别[1]  ，每一行的数据总数表示该类别的数据实例的数目。每一列中的数值表示真实数据被预测为该类的数目
> 
![](http://i.imgur.com/nA1B8EX.png)