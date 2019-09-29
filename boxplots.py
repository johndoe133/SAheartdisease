#box plot

# to see outliers

from dataextraction import (df, X)
import matplotlib.pyplot as plt

plt.figure(figsize=(10,8))
for i,j in enumerate([0,1,2,3,5,6,7,8]):
    plt.subplot(4,2,i+1)
    plt.title(df.columns.values[j+1])
    plt.boxplot(X[:,j])
    
plt.tight_layout()
plt.savefig("outliers plot appendix")
plt.show()
    