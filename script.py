# Project 1

# What is the problem of interest? (describe what your data is about in
# general terms, i.e. “to someone who knows nothing of machine learning”)

# To investigate corrolation between heart decease and factors such as 
# smoking, obesity, etc. 


# Who made the data and why? Did they, or somebody else, work with the
# data and report results? If so, what were their results?

# Rousseauw et al, 1983, South African Medical Journal


# What is the primary machine learning modelling aim? (Is it primarily
# a classification, a regression, a clustering, an association mining, or an
# anomaly detection problem?)


# Which attributes are relevant when carrying out a classification, a regression, a clustering, an association mining, and an anomaly detection?
# Specifically: Which attribute do you wish to explain in the regression
# based on which other attributes? Which class label will you predict based
# on which other attributes in the classification task?

# Are there any data issues? Either directly reported in the accompanying
# dataset description or apparent by inspection of the data? (such as missing
# values or incorrect/corrupted values)


# Info on the data set
# https://web.stanford.edu/~hastie/ElemStatLearn/

# Data set
# https://web.stanford.edu/~hastie/ElemStatLearn/

# exercise 1.5.1
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris csv data using the Pandas library
filename = 'heartdata.csv'
df = pd.read_csv(filename)

# Changing 'Present' and 'Absent' to 1 and 0 (true and false)
df.famhist = df.famhist.replace('Present',1)
df.famhist = df.famhist.replace('Absent',0)

raw_data = df.get_values()

cols = range(1, 11) # Getting rid of the first column since it's column numbers
X = raw_data[:, cols]

# We can extract the attribute names that came from the header of the csv
attributeNames = np.asarray(df.columns[cols])

classLabels = raw_data[:,-1] # -1 takes the last column

classNames = np.unique(classLabels)

classDict = dict(zip(classNames,range(len(classNames))))

y = np.array([classDict[cl] for cl in classLabels])

N, M = X.shape

C = len(classNames)


X_c = X.copy();
y_c = y.copy();

attributeNames_c = attributeNames.copy();

# missing values?

missing_idx = np.isnan(X)
plt.title('Visual inspection of missing values')
plt.imshow(missing_idx)
plt.ylabel('Observations'); plt.xlabel('Attributes');
plt.show()


# 0: sbp, 1: tobacco, 2: ldl, 3: adiposity, 4: famhist, 5: typea
# 6: obesity, 7: alcohol, 8: age, 9: chd

i = 6; j = 8;
color = ['g','r']
titlestring = attributeNames[i] + " vs. " + attributeNames[j]
plt.title(titlestring)
for c in range(len(classNames)):
    idx = y_c == c
    plt.scatter(x = X_c[idx, i],
                y = X_c[idx, j], 
                c = color[c], 
                s = 50, 
                alpha = 0.5,
                label = classNames[c])
plt.legend()
plt.xlabel(attributeNames_c[i])
plt.ylabel(attributeNames_c[j])
plt.show()

