import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dataextraction


X = dataextraction.X
attributeNames = dataextraction.attributeNames
df = dataextraction.df
N, M = X.shape

# 0: sbp, 1: tobacco, 2: ldl, 3: adiposity, 4: famhist, 5: typea
# 6: obesity, 7: alcohol, 8: age, 9: chd
# Select which two factors you wish to plot against each other (except chd)
x = 6
y = 8

#Separating dataframe into chd==1 and chd==0, aka has heart disease and not
df0 = df[df['chd'] == 0]
df1 = df[df['chd'] == 1]

#Getting the columns we want (for ex. obesity and age) and turning that data into arrays
x0 = np.asarray(df0[attributeNames[x]])
x1 = np.asarray(df1[attributeNames[x]])
y0 = np.asarray(df0[attributeNames[y]])
y1 = np.asarray(df1[attributeNames[y]])

titlestring = attributeNames[x] + " vs. " + attributeNames[y]
plt.title(titlestring)

plt.scatter(x0, y0, c='g', s=50, alpha=0.5, label="chd negative")
plt.scatter(x1, y1, c='r', s=50, alpha=0.5, label="chd positive")

plt.legend()
plt.xlabel(attributeNames[x])
plt.ylabel(attributeNames[y])
plt.show()

