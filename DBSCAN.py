from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
file_path = "/content/Wholesale customers data.csv"
df = pd.read_csv(file_path)
df

df.drop(['Channel','Region'],axis=1,inplace=True)
df

array = df.values

arraystscaler = StandardScaler().fit(array)
X = stscaler.transform(array)
X

dbscan = DBSCAN(eps=0.8, min_samples=6)
dbscan.fit(X)