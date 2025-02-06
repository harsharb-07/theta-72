final_ml_v=smf.ols('MPG~VOL +SP+HP',data= car1).fit()

(final_ml_v.rsquared,final_ml_v.aic)

final_ml_w=smf.ols('VOL~WT+SP+HP',data=car1).fit()

(final_ml_w.rsquared,final_ml_v.aic)

import matplotlib.pyplot as plt
import statsmodels.api as sm
fig = plt.figure(figsize=(15,8))
fig = sm.graphics.plot_regress_exog(model, "VOL", fig=fig)
plt.show()

final_ml_v=smf.ols('MPG~VOL+SP+HP',data=car1).fit()

model_influence =final_ml_v.get_influence()
(c_V, _) = model_influence.cooks_distance

model_influence =final_ml_v.get_influence()
(c_V, _) = model_influence.cooks_distance

fig=plt.subplots(figsize=(20,7))
plt.stem(np.arange(len(car1)),np.round(c_V,3))
plt.xlabel('Row Index')
plt.ylabel('Cooks Distance')
plt.show()

final_ml_v=smf.ols('MPG~VOL+SP+HP',data=car1).fit()

model_influence =final_ml_v.get_influence()
(c_V, _) = model_influence.cooks_distance

(np.argmax(c_V),np.max(c_V))

car2=car1.drop(car1.index[[76,77]],axis=0)
car2