import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
from mlxtend.preprocessing import TransactionEncoder
from google.colab import drive
drive.mount('/content/drive')
file_name="/content/Titanic.csv"
df=pd.read_csv(file_name)
df
df1=pd.get_dummies(df)
df1.head()
frequent_itemsets=apriori(df1,min_support=0.1,use_colnames=True)
frequent_itemsets
rules=association_rules(frequent_itemsets,metric='lift',min_threshold=0.7)
rules
rules.sort_values('lift',ascending=False)[0:20]
rules[rules.lift>1]
