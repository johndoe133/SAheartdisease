# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:49:53 2019

@author: Morten Bjerre
"""

# PCA component coefficients 
from dataextraction import (X, df, attributeNames)
import matplotlib.pyplot as plt
import numpy as np

from scipy.linalg import svd

N,M = X.shape
Y = X - np.ones((N,1))*X.mean(0)
U,S,Vh = svd(Y,full_matrices=False)
V=Vh.T


pcs = [0,1,2,3]
legendStrs = ['PC'+str(e+1) for e in pcs]
c = ['r','g','b']
bw = .2
r = np.arange(1,M+1)
plt.figure(figsize=(7,5))
for i in pcs:    
    plt.bar(r+i*bw, V[:,i], width=bw)
plt.xticks(r+bw, attributeNames, rotation = 30)
plt.xlabel('Attributes')
plt.ylabel('Component coefficients')
plt.legend(legendStrs)
plt.grid()
plt.title('PCA Component Coefficients')
plt.tight_layout()
plt.savefig('PCA_Component_Coefficients')
plt.show()