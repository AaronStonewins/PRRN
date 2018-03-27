#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:56:56 2018

@author: abhishek
"""

import numpy as np
import sklearn.linear_model as slm
import csv

def read_file(s):
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
            X.append(temp)
    return X,y
        
logreg=slm.LogisticRegression(C=1e5)

s1='P2_training_data'

X=read_file(s1);X_training=X[0];y=X[1]
logreg.fit(X_training,y)

s2='P2_test_data'
X_test=read_file(s2)
y_test=X_test[1]
X_test=X_test[0]
#logreg.predict(X_test)







    

