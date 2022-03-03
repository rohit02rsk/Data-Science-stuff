import numpy as np

x = [1,1.9,2.8,3.6,4.3,5.4,6.2,7.1,7.5,8.4]
y = [6.9,6.4,5.4,5.6,4.5,4.7,3.8,3.8,3.4,2.5]
A = np.array([[1, 6.9], [1.9, 6.4], [2.8, 5.4], [3.6, 5.6],
[4.3, 4.5], [5.4, 4.7], [6.2, 3.8], [7.1, 3.8], [7.5, 3.4],
[8.4, 2.5]])

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()

plt.plot(x, y, 'o', color='black')
plt.show()

from sklearn.decomposition import PCA
pca = PCA(2)
pca.fit(A)

print("The PCA components are:")
print(pca.components_)

print("The eigen values for PCA are:")
print(pca.explained_variance_)
