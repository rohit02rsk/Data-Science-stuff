import pandas as pd
data = { 'y1': [10, 5, 7, 19, 11, 8, 9, 11, 10, 12],
'y2': [15, 9, 3, 25, 7, 13, 12, 13, 7, 10],
'x1': [12, 10, 7, 5, 12, 20, 7, 8, 12, 13],
'x2': [10, 8, 6, 23, 12, 11, 13, 11, 10, 12]
}
df_manova = pd.DataFrame(data)

from statsmodels.multivariate.manova import MANOVA
maov = MANOVA.from_formula("y1 + y2 ~ x1 + x2", data = df_manova)
print(maov.mv_test())

