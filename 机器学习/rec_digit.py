# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 16:07:00 2016

@author: Grey
"""

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
        
        for i in range(1,len(result)):  
            tmp=[i,result[i]]  
            myWriter.writerow(tmp)
            
            
# 学习测试部分
from sklearn import svm
#trainData, trainLaber = loadTrainData()
#testData = loadTestData()
#classifier = svm.SVC(kernel='linear')
#classifier.fit(trainData, ravel(trainLaber))
#predicted = classifier.predict(testData)
saveResult(predicted,'SVC_test.csv') 