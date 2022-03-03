import numpy as np
from matplotlib import pyplot as plt

samples1 = np.random.normal(2, 3, size=1000)

a = np.linspace(-4, 8, 30)
histogram1, bins = np.histogram(samples1, bins=a)
plt.figure(figsize=(6, 4))
plt.hist(samples1, bins=a, label="Histogram from samples")
plt.legend(loc='best')
plt.show()
