# scikit-learn 0.17 （使用手册）
## 第一章 监督学习
## 1.1 广义线性模型(Generalized Linear Models)
下面是一套用于回归目标值的方法，预测值是输入变量的线性组合。

![](http://i.imgur.com/QUPqcra.png)

根据这个模型，我们可以指定向量 `w` 是回归系数（相当于斜率）`coef_`，<img src="http://www.forkosh.com/mathtex.cgi? w_{0}"> 是截距 `intercept_`（正则化项）。

### 1.1.1 普通最小二乘法(Ordinary Least Squares)
线性回归通过回归系数来拟合一个线性模型需要最小化预测值和观测值的残差平方和，通过下面的数学方式来解决的：

![](http://i.imgur.com/CBSB6X7.png)

线性回归模型可以通过输入变量，计算得到相应的回归系数并存储到 `coef_`中：

    >>> from sklearn import linear_model
    >>> clf = linear_model.LinearRegression()
    >>> clf.fit ([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
    LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    >>> clf.coef_
    array([ 0.5,  0.5])

然而，通过普通最小二乘法来进行回归系数估计依赖于模型样本的独立性。当样本相关时，设计矩阵的列会有近似线性关系，设计矩阵会变得接近奇异，作为结果，最小二乘法估计值会变得对观测值的随机误差异常敏感，会产生一个很大的方差。就会产生多重共线性的情况。例如，当采集数据的时候没有一个实验设计。

#### 1.1.1.1 普通最小二乘法的复杂度
如果需要计算的矩阵大小是（n,p），那么时间复杂度会是 <img src="http://www.forkosh.com/mathtex.cgi? O(np^2{})"> ，假设 n >= p

### 1.1.2 岭回归(Ridge Regression)
岭回归通过对回归系数添加一个二范数惩罚（l2 惩罚项）来解决最小二乘法的一些问题，岭系数最小化惩罚的残差平方和。

![](http://i.imgur.com/NP4xvfK.png)

这里 <img src="http://www.forkosh.com/mathtex.cgi? \alpha "> （大于等于 0 ）是一个来控制特征缩减总量的复杂变量：随着它增大，特征总量收缩越明显，回归系数对于共线性更为稳健。



> （回归系数和 alpha 的关系图）
![](http://i.imgur.com/PO1sMxg.png)



和其他线性模型一样，岭回归模型可以通过输入变量，计算得到相应的回归系数并存储到 `coef_`中：

    >>> from sklearn import linear_model
    >>> clf = linear_model.Ridge (alpha = .5)
    >>> clf.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1]) 
    Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None,
      normalize=False, random_state=None, solver='auto', tol=0.001)
    >>> clf.coef_
    array([ 0.34545455,  0.34545455])
    >>> clf.intercept_ 
    0.13636...

例子：

- [画出岭回归系数和正则化项关系的函数图像](http://blog.csdn.net/gr47725812/article/details/51879782)
- [利用稀疏特征的文本文档分类](http://blog.csdn.net/gr47725812/article/details/51882000)

#### 1.1.2.1 岭回归复杂度
和普通最小二乘法相同。

#### 1.1.2.2 设置正则化参数：广义交叉验证

 `RidgeCV` 使用岭回归交叉验证正则化项。这个和 `GridSearchCV `（网格搜索交叉验证）是一样的工作方式都是基于默认的广义交叉验证，是一种有效的 `leave-one-out` （留一法）交叉验证形式。

    >>> from sklearn import linear_model
    >>> clf = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
    >>> clf.fit([[0, 0], [0, 0], [1, 1]], [0, .1, 1])   
    RidgeCV(alphas=[0.1, 1.0, 10.0], cv=None, fit_intercept=True, scoring=None,normalize=False)
    >>> clf.alpha_
    0.1

#### 1.1.3 套索(Lasso)
 `Lasso` 是一个用来估计稀疏回归系数的线性模型。它在某些特定的场合很有效是因为它的策略是倾向于处理更少的参数，有效的减少结果对参数数量的依赖。由于这个原因， `Lasso` 以及它的变种是压缩感知领域（compressed sensing）的基础。在一定条件下，它可以恢复非零权重的设置（见[Compressive sensing: tomography reconstruction with L1 prior (Lasso)](http://blog.csdn.net/gr47725812/article/details/51885030)）。

数学上，它一个添加了 `l1` 惩罚项的线性模型，损失函数：

![](http://i.imgur.com/rPhYBri.png)

套索估计解决了最小二乘最小化通过添加一个惩罚项，其中 <img src="http://www.forkosh.com/mathtex.cgi? \alpha "> 是一个常数，<img src="http://www.forkosh.com/mathtex.cgi? \left \| w \right \|_{1} "> 是参数向量的曼哈顿距离。

 `Lasso`类使用坐标下降算法来拟合回归系数：

    >>> from sklearn import linear_model
    >>> clf = linear_model.Lasso(alpha = 0.1)
    >>> clf.fit([[0, 0], [1, 1]], [0, 1])
    Lasso(alpha=0.1, copy_X=True, fit_intercept=True, max_iter=1000,
       normalize=False, positive=False, precompute=False, random_state=None,
       selection='cyclic', tol=0.0001, warm_start=False)
    >>> clf.predict([[1, 1]])
    array([ 0.8])

 `lasso_path` 可以用来计算回归系数沿着完整路径的可能值。

例子：

- [Lasso and Elastic Net for Sparse Signals](待补)
- [Compressive sensing: tomography reconstruction with L1 prior (Lasso)](http://blog.csdn.net/gr47725812/article/details/51885030)

#### 1.1.3.1 设置正则化参数
α 参数控制回归系数估计的稀疏性。

##### 1.1.3.1.1 使用交叉验证

 `scikit-learn` 通过交叉验证来设置 `Lasso` 的 `alpha` 参数： `LassoCV` 和 `LassoLarsCV`。`LassoLarsCV`是基于最小角回归算法的。

对于有共线性回归量的高维度数据集， `LassoCV` 常常是更好的选择。然而， `LassoLarsCV` 的优点是能够获得更多 `alpha` 参数的相关值，而且如果样本的数量相对于测试数据显得很少的话，它通常要比 `LassoCV` 要快。

##### 1.1.3.1.2 基于模型选择的信息准则
另外，`LassoLarsIC` 评估器使用 `AIC` 和 `BIC`。相比使用 `k-fold` 交叉验证需要计算 `k+1` 次这种方法只需要计算一次就能找到作为正则化项的 `alpha` 的最优解。然而，使用这种方法需要对解决方案的自由度有适当的估计，并且能够适用于大规模样本（渐进结果），同时要假设模型正确，即数据是通过这个模型产生的，还有在条件很差的情况下也不能使用（特征数量比样本多）。

例子： [Lasso 模型选择：交叉验证/AIC/BIC]()

### 1.1.4 弹性网（Elastic Net）
 `Elastic Net` 是将 L1，L2惩罚项混合作为正则化项的线性回归模型。这种方法可以像 `Lasso` 一样学习稀疏矩阵，同时也有 `Ridge` 的特点。我们用 `l1_ratio` 来表示正则化项。

`Elastic Net`对于处理多重特征相关的数据很有效， `Lasso` 是随机选择了其中某个特征，而 `Elastic Net` 是保留了所有特征。作为两者的折中方案还继承了 `Ridge` 对于旋转的稳定性。

损失函数：

![](http://i.imgur.com/L8D1UXp.png)

 `ElasticNetCV` 可以用来通过交叉验证设置正则化项。

例子：

- [Lasso and Elastic Net for Sparse Signals]()
- [Lasso and Elastic Net]()

### 1.1.5 多任务 Lasso
多任务 Lasso 是用来对多元回归问题的稀疏回归系数进行评估的线性模型。对于所有回归问题的约束是选择相同的特征。

