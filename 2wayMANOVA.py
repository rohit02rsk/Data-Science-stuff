import pandas as pd
data = { 'y1': [30,25,27,39,31,28,29,31,30,32],
'y2': [35,29,23,45,27,33,32,33,27,30],
'x1': [32,30,27,25,32,40,27,28,32,33],
'x2': [30,28,26,43,32,31,33,31,30,32]
}
df_manova = pd.DataFrame(data)

from statsmodels.multivariate.manova import MANOVA
maov = MANOVA.from_formula("y1 + y2 ~ x1 + x2", data = df_manova)
print(maov.mv_test())


