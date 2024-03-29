import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dataextraction
import random



X = dataextraction.X
attributeNames = dataextraction.attributeNames
df = dataextraction.df
N, M = X.shape

# 0: sbp, 1: tobacco, 2: ldl, 3: adiposity, 4: famhist, 5: typea
# 6: obesity, 7: alcohol, 8: age, 9: chd
# Select which two factors you wish to plot against each other (except chd)
x = 8

#Separating dataframe into chd==1 and chd==0, aka has heart disease and not
df0 = df[df['chd'] == 0]
df1 = df[df['chd'] == 1]

#Getting the columns we want (for ex. obesity and age) and turning that data into arrays
x0 = np.asarray(df0[attributeNames[x]])
x1 = np.asarray(df1[attributeNames[x]])

chd0 = np.empty(0)
for i in range(len(x0)):
    chd0 = np.append(chd0, (random.random()-0.5)/2.0)

chd1 = np.empty(0)
for i in range(len(x1)):
    chd1 = np.append(chd1, (random.random()+1.5)/2.0)

titlestring =  "chd vs. " + attributeNames[x]
plt.figure()
plt.title(titlestring)

plt.scatter(chd0, x0, c='g', s=50, alpha=0.5, label="chd negative")
plt.scatter(chd1, x1, c='r', s=50, alpha=0.5, label="chd positive")

plt.legend()
plt.xlabel("chd")
plt.ylabel(attributeNames[x])
plt.xticks([0,1])
plt.show()

# 7 alcohol
x2 = np.asarray(df0[attributeNames[7]])
x3 = np.asarray(df1[attributeNames[7]])

# 6 obesity
x4 = np.asarray(df0[attributeNames[6]])
x5 = np.asarray(df1[attributeNames[6]])

# 1 tobacco
x6 = np.asarray(df0[attributeNames[1]])
x7 = np.asarray(df1[attributeNames[1]])


plt.figure(figsize=(10,8))
plt.subplot(2,2,1)
plt.boxplot([x0,x1])
title = "chd vs age"
plt.title(title)
plt.xticks((1,2),("chd negative","cdh positive"))
plt.ylabel("Age")

plt.subplot(2,2,2)
plt.boxplot([x2,x3])
title = "chd vs alcohol consumption"
plt.title(title)
plt.xticks((1,2),("chd negative","cdh positive"))
plt.ylabel("Alcohol")

plt.subplot(2,2,3)
plt.boxplot([x4,x5])
title = "chd vs obesity"
plt.title(title)
plt.xticks((1,2),("chd negative","cdh positive"))
plt.ylabel("Obesity")

plt.subplot(2,2,4)
plt.boxplot([x6,x7])
title = "chd vs tobacco"
plt.title(title)
plt.xticks((1,2),("chd negative","cdh positive"))
plt.ylabel("tobacco")

plt.tight_layout()
plt.savefig("boxplot of chd vs 4 attri.")

plt.show()
