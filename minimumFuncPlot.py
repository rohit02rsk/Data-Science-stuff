import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as spop

def f(x):
    return x**2+15*np.cos(x)

plt.figure()
x = np.arange(-10,10,0.1)
plt.plot(x,f(x))
plt.show()

result = spop.minimize(f, x0=0)
print(result)
print('Minima is at: %.4f' %result.x)
plt.plot(result.x,f(result.x),'o')
plt.show()