# summary statistics

import dataextraction
X = dataextraction.X
N,M = X.shape

# 0: sbp, 1: tobacco, 2: ldl, 3: adiposity, 4: famhist, 5: typea
# 6: obesity, 7: alcohol, 8: age, 9: chd

# table 1
famhist_true = sum(X[:,4]==1)
famhist_false = sum(X[:,4]==0)
chd_true = sum(X[:,9]==1)
chd_false = sum(X[:,9]==0)
print("famhist_true",famhist_true)
print("famhist_false",famhist_false)
print("chd_true",chd_true)
print("chd_false",chd_false)

#table 2
# chd,famhist
ff = 0
tt = 0
tf = 0
ft = 0

#boxplot
plt.figure()
plt.boxplot(X[:,5])
plt.title("Boxplot of typea")
plt.savefig("boxplot")
plt.show()

N,M = X.shape

for i in range(N):
    if (X[i,9] == 1 and X[i,4] == 1):
        tt += 1
    elif (X[i,9] == 1 and X[i,4] == 0):
        tf += 1
    elif (X[i,9] == 0 and X[i,4] == 1):
        ft += 1
    else:
        ff += 1

print("ff",ff)
print("tt",tt)
print("tf",tf)
print("ft",ft)


