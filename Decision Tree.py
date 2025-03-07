import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn import preprocessing
from google.colab import drive
drive.mount('/content/drive')
file_name='/content/iris.csv'
data=r"/content/iris.csv"
import pandas as pd
df=pd.read_csv(file_name)
df
df.head()
le=preprocessing.LabelEncoder()
df['Species']=le.fit_transform(df['Species'])
df['Species']
x=df.iloc[:,0:4]
y=df['Species']
x
y
df['Species'].unique()
df.Species.value_counts()
colnames=list(df.columns)
colnames
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=40)
model=DecisionTreeClassifier(criterion='entropy',max_depth=3)
model.fit(X_train,y_train)
tree.plot_tree(model);
fn=['sepal length(cm)','sepal width(cm)','petal length(cm)','petal width(cm)']
cn=['setosa','versicolor','virginica']
fig,axes=plt.subplots(nrows=1,ncols=1,figsize=(4,4),dpi=300)
tree.plot_tree(model,
               feature_names=fn,
               class_names=cn,
               filled=True);
preds=model.predict(X_test)
pd.Series(preds).value_counts()
preds
pd.crosstab(y_test,preds)
np.mean(preds==y_test)