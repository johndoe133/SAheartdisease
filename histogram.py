import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataextraction import (X, df, attributeNames)
from statsmodels.graphics.gofplots import qqplot

N, M = X.shape

# 0: sbp, 1: tobacco, 2: ldl, 3: adiposity, 4: famhist, 5: typea
# 6: obesity, 7: alcohol, 8: age, 9: chd
# Select which two factors you wish to plot against each other (except chd)
plt.figure(figsize=(10,7))
#plt.suptitle("Histogram of select attributes")
for c,i in enumerate([0,1,2,3,5,6,7,8]):
    plt.subplot(2, 4, c+1)
    x = np.asarray(df[attributeNames[i]])
    titlestring = attributeNames[i]
    if (c == 0 or c == 4):
        plt.ylabel("Number of occurrences")
    plt.title(titlestring)
    plt.hist(x,bins=20)
    plt.subplots_adjust(left=0.1, bottom=None, right=0.9, top=0.9, wspace=0.5, hspace=0.3)
    plt.xlabel(attributeNames[i])
    
 
    
plt.tight_layout()
plt.savefig("histograms_of_attributes")
plt.show()

#qqplot
plt.figure()
for c,i in enumerate([0,2,3,5,6]):
    qqplot(X[:,i],line='s')
    plt.title("qqplot of " + str(attributeNames[i]))
    plt.savefig("qqplot_of_" + str(attributeNames[i]))
    plt.show()

