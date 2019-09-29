import numpy as np
from dataextraction import (df, X)
import matplotlib.pyplot as plt
import seaborn as sns

df = df.drop("names", axis=1)
corr = df.corr()

plt.matshow(corr)
plt.xticks(range(df.shape[1]), df.columns, fontsize=14, rotation=30)
plt.yticks(range(df.shape[1]), df.columns, fontsize=14)
cb = plt.colorbar()
cb.ax.tick_params(labelsize=14)
plt.title('Correlation Matrix', fontsize=12, y=1.1)
plt.show()