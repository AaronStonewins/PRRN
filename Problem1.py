# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:06:08 2018

@author: Abhishek
"""

import numpy as np
import csv
import random
from readFile import read_file
from readFile import read_filetest
import linearClassifiers as LC

s='.\dataset_linear_classifier\P1\with margin\P1a_training_data'
stest='.\dataset_linear_classifier\P1\with margin\P1a_test_data'

X_train=read_file(s)
X_test,y_test=read_filetest(stest)
X_traingen,Y=read_filetest(s)

#W=LMS(X_train)
#W=perceptron(X_train)
#W=genInverse(X_traingen,Y)
#print(accuracyLC(W,X_test,y_test))