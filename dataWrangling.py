import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None) 
print("The given data is:\n",data)

data.columns = ["S"+str(i) for i in range(1, len(data.columns)+1)]
data.S1 = data.S1.astype(str)
X = data.loc[:, "S2":]
y = data.S1
print("After modifying the data:\n",data)

pd.plotting.scatter_matrix(data.loc[:, "S4":"S8"], diagonal="kde")
plt.tight_layout()
plt.show()