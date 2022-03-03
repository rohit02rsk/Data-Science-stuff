import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256)
C2, S2, S3 = np.cos(2*X), np.sin(2*X), np.sin(3*X)

plt.subplot(2,2,3)
plt.plot(X, S2)
plt.title("sin(2x)")

plt.subplot(2,2,2)
plt.plot(X, C2)
plt.title("cos(2x)")

plt.subplot(2,2,1)
plt.plot(X, S3)
plt.title("sin(3x)")

plt.show()



