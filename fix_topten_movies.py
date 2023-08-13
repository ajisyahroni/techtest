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

def set_score (df : pd.DataFrame, var = .8) : 
    agg = df.groupby(['movieId', 'title'], as_index=False).agg({'rating' :['mean','count']  })
    agg.columns  = ['movieId', 'title', 'rating_mean', 'num_votes']
    v = agg['num_votes']
    R = agg['rating_mean']
    C = R.mean()
    m = agg['num_votes'].quantile(var)
    agg['score'] = (v/(v+m)*R + m/(v+m)*C) #rumus IMDB
    return agg

top_ten_movies = set_score(df).sort_values(by=['score'], ascending=False).head(10)
top_ten_movies.to_json('result/res_top_ten.json', orient='records')
print(top_ten_movies)