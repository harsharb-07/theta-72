import pandas as pd
from google.colab import files
uploaded=files.upload()
file_name=list(uploaded.keys())[0]
cars=pd.read_csv(file_name)

car1 = cars.drop(cars.index[[70, 76]], axis=0).reset_index()
car1=car1.drop(['index'],axis=1)
car1

import statsmodels.formula.api as smf
final_ml_v= smf.ols('MPG~VOL+SP+HP',data=car1).fit()

final_ml_v.rsquared,final_ml_v.aic