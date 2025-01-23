from google.colab import files
import pandas as pd
upload=files.upload()
aaa=list(upload.keys())[0]
df=pd.read_csv(aaa)
df.head(20)