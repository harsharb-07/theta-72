import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('/content/drive')
file_path = "/content/Movie.csv"
df = pd.read_csv(file_path)
movies_df=pd.read_csv('/content/Movie.csv')
movies_df[0:5]
len(movies_df.userId.unique())
user_movies_df=movies_df.pivot(index='userId',columns='movie',values='rating').reset_index(drop=True)
user_movies_df
user_movies_df.index=movies_df.userId.unique()
user_movies_df.fillna(0,inplace=True)
user_movies_df
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine,correlation
from scipy.spatial.distance import correlation
vec1=[5,6,0,0]
vec2=[6,2,3,0]
correlation_distance=correlation(vec1,vec2)
print(correlation_distance)
user_sim=1-pairwise_distances(user_movies_df.values,metric='cosine')
user_sim
user_sim_df=pd.DataFrame(user_sim)
user_sim_df
user_sim_df.index=movies_df.userId.unique()
user_sim_df.columns=movies_df.userId.unique()
user_sim_df.iloc[0:5,0:5]
