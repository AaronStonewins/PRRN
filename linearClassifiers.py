# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:25:01 2018

@author: Abhishek
"""


import numpy as np
import random
from scipy.linalg import eig

#Returns the accuracy of the linear classifier for a given W
def accuracyLC(W,X,y):
    Z=np.array(np.transpose(X))
    accuracy = np.sum(np.sign(np.matmul(W,Z))==np.array(y))
    return accuracy


# Perceptron
def perceptron(X):
    Wprev=np.zeros(11)
    W=np.ones(11)
    diff=np.linalg.norm(W-Wprev)
    thres=1e-5
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
    return W
# Least Mean Squares
def LMS(X,eta=0.008):
    Wprev=np.zeros(11)
    W=np.ones(11)
    diff=np.linalg.norm(W-Wprev)
    thres=1e-8
    while diff>thres:
        Wprev=W
        for x in X:
            label=np.array(x[11])
            Y=np.array(x[0:11])
            prod=np.dot(Y,W)
            prod=prod-label
            W=W-(eta*prod*Y)
        diff=np.linalg.norm(W-Wprev)
    return W

def fisher_train(X,Y):
    index = np.where(Y==1)
    c1 = X[index]
    index = np.where(Y==-1)
    c0 = X[index]
    M0 = np.mean(c0,axis=0)
    M1 = np.mean(c1,axis=0)
    s_w=np.zeros([X.shape[1],X.shape[1]])
    for i in c1:
        tmp = (i-M1).reshape(-1,1)
        tmp1 = np.dot(tmp,tmp.T)
        s_w += tmp1
    for i in c0:
        tmp = (i-M0).reshape(-1,1)
        tmp1 = np.dot(tmp,tmp.T)
        s_w += tmp1
    #print np.linalg.det(s_w)
    A=(M1-M0).reshape(-1,1)
    s_b = np.dot(A,A.T)
    #print np.linalg.matrix_rank(s_w)
    eigvals, eigvecs = eig(s_w,s_b)
    emax =0
    maxval = findj(eigvecs[:,0],s_w,s_b)
    for i in range(1,eigvecs.shape[1]):
        tmp = findj(eigvecs[:,i],s_w,s_b)
        if(tmp>maxval):
            emax=i
            maxval=tmp
        
    return eigvecs[:,emax]

def findj(w,sw,sb):
    if(np.dot(np.dot(w.T,sw),w)!=0):
        return np.dot(np.dot(w.T,sb),w)/np.dot(np.dot(w.T,sw),w)
    else:
        return 0




#Generalized Inverse    
def genInverse(X,y):
    W=np.zeros(11)
    X=np.array(X)
    y=np.array(y)
    W_inv=np.linalg.pinv(np.matmul(np.transpose(X),X))
    W_xty=np.matmul(np.transpose(X),y)
    W=np.matmul(W_inv,W_xty)
    return W