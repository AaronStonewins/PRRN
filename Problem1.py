# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:06:08 2018

@author: Abhishek
"""

import numpy as np
import csv
import random

def read_file(s):
    X=[]
    with open(s,'r') as f:
        reader=csv.reader(f)
        for row in reader:
            temp=[]
            for i in range(len(row)):
                if i==(len(row)-1):
                    temp.append(int(row[i]))
                else:
                    temp.append(float(row[i]))
            temp.insert(0,1)
            X.append(temp)
    return X


def read_filetest(s):
    X=[];y=[]
    with open(s,'r') as f:
        reader=csv.reader(f)
        for row in reader:
            temp=[]
            for i in range(len(row)):
                if i==(len(row)-1):
                    y.append(int(row[i]))
                else:
                    temp.append(float(row[i]))
            temp.insert(0,1)
            X.append(temp)
    return X,y


def perceptron(X):
    Wprev=np.zeros(11)
    W=np.ones(11)
    diff=np.linalg.norm(W-Wprev)
    thres=1e-8
    while diff>thres:
        Wprev=W
        for x in X:
            label=np.array(x[11])
            Y=np.array(x[0:11])
            prod=np.dot(W,Y)
            sign_dot=np.sign(prod)
            measure=label*sign_dot
            if measure<0:
                W=W+(label*Y)
        diff=np.linalg.norm(W-Wprev)
        print(W)
    return W

def LMS(X,eta=0.4):
    W=np.zeros(10)
    W=np.ones(10)
    for x in X:
        y=x.pop()
        mul=np.dot(W,x)-y
        mul=mul*eta
        Y=mul*np.array(x)
        W=W-(eta*mul)*Y
        
    return W


s='.\dataset_linear_classifier\P1\with margin\P1a_training_data'
stest='.\dataset_linear_classifier\P1\with margin\P1a_test_data'

X_train=read_file(s)
X_test,y_test=read_filetest(stest)


#print(LMS(X))
W=perceptron(X_train)
Z=np.array(np.transpose(X_test))
print(np.sum(np.sign(np.matmul(W,Z))==np.array(y_test)))