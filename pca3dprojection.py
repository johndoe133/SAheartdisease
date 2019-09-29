from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pca2dprojection import *

f = plt.figure()
ax = f.add_subplot(111, projection='3d')
ax.scatter(z0[:,0], z0[:,1], z0[:,2], c='g', label = "chd=0")
ax.scatter(z1[:,0], z1[:,1], z1[:,2], c='r', label = "chd=1")
plt.legend()
plt.xlabel('PCA1')
plt.ylabel('PCA2')
ax.set_zlabel('PCA3')
plt.show()