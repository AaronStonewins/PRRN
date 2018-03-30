#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:56:56 2018

@author: abhishek
"""

import numpy as np
import sklearn.linear_model as slm
import csv
from readFile import read_filetest
from linearClassifiers import LMS

        
logreg=slm.LogisticRegression(C=1e5)

s1='.\dataset_linear_classifier\P2\P2_training_data'

X_train,y=read_filetest(s1)
logreg.fit(X_train,y)

s2='.\dataset_linear_classifier\P2\P2_test_data'
X_test,y_test=read_filetest(s2)

print(np.sum(logreg.predict(X_test)==y_test))







    

