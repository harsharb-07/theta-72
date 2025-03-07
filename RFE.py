from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

filename="/content/pima-indians-diabetes.data.csv"
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=read_csv(filename,names=names)
array=dataframe.values
X=array[:,0:8]
Y=array[:,8]
model=LogisticRegression(max_iter=400)
rfe=RFE(estimator=model, n_features_to_select=3)
fit=rfe.fit(X,Y)
fit.n_features_
fit.support_fit.ranking_