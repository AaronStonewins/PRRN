# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:49:54 2018

@author: Abhishek
"""

import csv
import re
import math
import numpy as np
s=".\datasets_assignement1\P3_training_data.csv"
bagOfWords=[]
label=[]
with open(s,'r') as csvfile:
     readCSV=csv.reader(csvfile,delimiter=',')
     for row in readCSV:
         b=re.findall(r'\b\w+\b',row[0])
         label.append(b[0])
         bagOfWords.append(b[1:len(b)])


numOfPos=0
n=len(label)
for i in range(n):
    if label[i]=='Pos':
        numOfPos=numOfPos+1
        
Class1=[];Class2=[]      
for i in range(numOfPos):
    m=len(bagOfWords[i])
    for j in range(m):
        Class1.append(bagOfWords[i][j])
        
        
for i in range(numOfPos,n,1):
    m=len(bagOfWords[i])
    for j in range(m):
        Class2.append(bagOfWords[i][j])



m1=len(Class1)
d1={}
for i in range(m1):
    d1[Class1[i]]=0
V1=len(d1)
C1=V1+m1
for i in range(m1):
    d1[Class1[i]]=(1/C1)
for i in range(m1):
    d1[Class1[i]]=d1[Class1[i]]+(1/C1)

d2={};m2=len(Class2)
for i in range(m2):
    d2[Class2[i]]=0
V2=len(d2)
C2=V2+m2
for i in range(m2):
    d2[Class2[i]]=(1/C2)
for i in range(m2):
    d2[Class2[i]]=d2[Class2[i]]+(1/C2)
    
print(d1) 


s1=input("Enter the file's destination:")

bagOfWordsTest=[]


with open(s1,'r') as csvfile:
     readCSV=csv.reader(csvfile,delimiter=',')
     for row in readCSV:
         b=re.findall(r'\b\w+\b',row[0])
         bagOfWordsTest.append(b[1:len(b)])


N=len(bagOfWordsTest)
P1=1;P2=1
for j in range(N):
    if bagOfWordsTest[j] in d1 and bagOfWordsTest[j] in d2:
        P1=P1*d1[bagOfWordsTest[j]]
        P2=P2*d2[bagOfWordsTest[j]]
    else:
        P1=P1/C1
        P2=P2/C2


Z=math.log(P1/P2)
if np.sign(Z):
    print("Positive")
else:
    print("Negative")













        