import pandas as pd
import numpy as np

data = { 'y': [0,0,0,0,0,1,1,1,1,1],
'x1': [7,9,6,7,7,13,10,6,4,8],
'x2': [5,4,6,6,9,6,9,8,7,5]
}
df_discrim = pd.DataFrame(data)

Y = np.array([0,0,0,0,0,1,1,1,1,1])
X = np.array([[7,5], [9,4], [6,6], [7,6], [7,9], [13,6], [10,9], [6,8], [4,7], [8,5]])

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components=1)
model = lda.fit(X, Y)
