import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.regressionplots import influence_plot
import statsmodels.formula.api as smf
import numpy as np

import pandas as pd
from google.colab import files
uploaded = files.upload()
file_name = list(uploaded.keys())[0]
df = pd.read_csv(file_name)
print(df.head())
df
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
print(ml_w1.tvalues,'\n',ml_w1.pvalues)
(ml_w1.rsquared,ml_w1.rsquared_adj)
ml_wv=smf.ols('MPG~WT+VOL',data=df).fit()
print(ml_wv.tvalues,'\n',ml_wv.pvalues)
#add scatter plots for the above code
import matplotlib.pyplot as plt
plt.scatter(df['WT'],df['MPG'])
plt.scatter(df['VOL'],df['MPG'])
plt.scatter(df['SP'],df['MPG'])
plt.scatter(df['HP'],df['MPG'])
rsq_hp=smf.ols('HP~WT+VOL+SP',data=df).fit().rsquared
vif_hp=1/(1-rsq_hp)
rsq_wt=smf.ols('WT~HP+VOL+SP',data=df).fit().rsquared
vif_wt=1/(1-rsq_wt)
rsq_vol=smf.ols('VOL~HP+WT+SP',data=df).fit().rsquared
vif_vol=1/(1-rsq_vol)
rsq_sp=smf.ols('SP~HP+WT+VOL',data=df).fit().rsquared
vif_sp=1/(1-rsq_sp)
d1={'variables':['HP','WT','VOL','SP'],'VIF':[vif_hp,vif_wt,vif_vol,vif_sp]}
vif_frame=pd.DataFrame(d1)
vif_frame
import statsmodels.api as sm
qqplot=sm.qqplot(model.resid,line='q')
plt.title("Normal Q-Q plot of residuals")
plt.show()
import numpy as np
list(np.where(model.resid>10))