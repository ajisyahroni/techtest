import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


df_movie = pd.read_parquet('./db/movie.parquet')
df_rating = pd.read_parquet('./db/rating.parquet')


# sdf = pd.merge(df_movie, df_rating , on=['movieId'], how='left')
# print(sdf.shape)

# print(df_rating['rating'].value_counts())
# print(df_rating['rating'].describe())
# df_rating['rating'].plot.hist(bins=30).get_figure().savefig('./result/rating_hist.png')
# doc :  rating 4 memiliki freq tertinggi sebesar 75%

# print(df_rating.userId.value_counts().describe())


# JOINING DATA 
df = pd.merge(df_movie, df_rating , on=['movieId'], how='inner', validate='one_to_many')


# AGGREGATE
x = df.groupby('movieId', as_index=False).agg({'rating' :['mean','count']  }).reset_index()

# Memberi score dari masing-masing film
v = x['rating']['count']
R = x['rating']['mean']
C = R.mean()
m = x['rating']['count'].quantile(0.8)
x['score'] = (v/(v+m)*R + m/(v+m)*C) #rumus IMDB

topMovie = x.sort_values(by=['score'], ascending=False).head(10)

print(topMovie)