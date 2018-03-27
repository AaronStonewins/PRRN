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
#bagOfWords=[]


def getFreq(word,d,count):
    if word in d:
        return math.log(d[word]/count)
    else:
        return math.log(1/count)
    
    
class1={};class2={}
label=[]
countPos=0;countNeg=0
with open(s,'r') as csvfile:
     readCSV=csv.reader(csvfile,delimiter=',')
     for row in readCSV:
         b=re.findall(r'\w+',row[0])
         label=b.pop(0)
         if label=='Pos':
             for word in b:
                 if word not in class1:
                     class1[word]=2
                 else:
                     class1[word]=class1[word]+1
             countPos=countPos+len(b)
         else:
             for word in b:
                 if word not in class2:
                     class2[word]=2
                 else:
                     class2[word]=class2[word]+1
             countNeg=countNeg+len(b)
             
             
lenOfClass1=len(class1)
lenOfClass2=len(class2)
countTotal=countPos+countNeg  
lenTotal=lenOfClass1+lenOfClass2   
s1=".\P3_test_data.csv"
L=[];countOne=0;countZero=0
with open(s1,'r') as csvfile:
     readCSV=csv.reader(csvfile,delimiter=',')
     for row in readCSV:
         P1=0;P2=0
         b=re.findall(r'\w+',row[0])
         for word in b:
             P1=P1+getFreq(word,class1,countPos)
             P2=P2+getFreq(word,class2,countNeg)
         if P1>P2:
             L.append(1)
             countOne=countOne+1
         else:
             L.append(0)
             countZero=countZero+1


print(countOne)
print(countZero)
             
file=open("Assignment1Problem.txt",'w')

for i in range(len(L)):
    file.write(str(L[i])+'\n')
    
    








#with open(s1,'r') as csvfile:
#     readCSV=csv.reader(csvfile,delimiter=',')
#     for row in readCSV:
#         b=re.findall(r'\b\w+\b',row[0])
#         bagOfWordsTest.append(b[1:len(b)])
#
#
#N=len(bagOfWordsTest)
#P1=1;P2=1
#for j in range(N):
#    if bagOfWordsTest[j] in d1 and bagOfWordsTest[j] in d2:
#        P1=P1*d1[bagOfWordsTest[j]]
#        P2=P2*d2[bagOfWordsTest[j]]
#    else:
#        P1=P1/C1
#        P2=P2/C2
#











        