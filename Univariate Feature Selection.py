from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd

filename="/content/pima-indians-diabetes.data.csv"
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
df=read_csv(filename,names=names)
print(df)
array=df.values
X=array[:,0:8]
Y=array[:,8]
test=SelectKBest(score_func=chi2,k=4)
fit=test.fit(X,Y)
print(names)
set_printoptions(precision=3)
print(fit.scores_)
features=fit.transform(X)