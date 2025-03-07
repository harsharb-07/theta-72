from pandas import read_csv
from sklearn.tree import DecisionTreeClassifier

filename="/content/pima-indians-diabetes.data.csv"
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
df=read_csv(filename,names=names)
array=dataframe.values
X=array[:,0:8]
Y=array[:,8]
model=DecisionTreeClassifier()
model.fit(X,Y)
print(names)
print(model.feature_importances_)