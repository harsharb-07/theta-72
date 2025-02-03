import statsmodels.formula.api as smf
import pandas as pd
# Assuming your DataFrame is named 'df', replace it if it's different
model = smf.ols('MPG~WT+VOL+SP+HP', data=df).fit()

model.params

print(model.tvalues, '\n', model.pvalues)
(model.rsquared,model.rsquared_adj)
ml_v=smf.ols('MPG~VOL',data=df).fit()
print(ml_v.tvalues,'\n',ml_v.pvalues)
ml_w1=smf.ols('VOL~WT',data=df).fit()
print(ml_w.tvalues,'\n',ml_w.pvalues)
(ml_w1.rsquared,ml_w1.rsquared_adj) 
ml_wv=smf.ols('MPG~WT+VOL',data=df).fit()
print(ml_wv.tvalues,'\n',ml_wv.pvalues)
(ml_wv.rsquared,ml_wv.rsquared_adj)

import matplotlib.pyplot as plt
plt.scatter(df['WT'],df['MPG'])
plt.scatter(df['VOL'],df['MPG'])
plt.scatter(df['SP'],df['MPG'])
plt.scatter(df['HP'],df['MPG'])