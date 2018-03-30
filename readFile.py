# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:18:50 2018

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


def read_file_simple(s):
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