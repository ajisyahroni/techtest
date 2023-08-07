import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


df_movie = pd.read_parquet('./db/movie.parquet')
df_rating = pd.read_parquet('./db/rating.parquet')


# analisa 
# movie columns : (movieId', 'title', 'genres')
# rating columns : '#', 'userId', 'movieId', 'rating', 'timestamp'
# merge based on movieId
df = pd.merge(df_movie, df_rating , on=['movieId'])

# print('c', len(df_movie))
# print('c', len(df_rating))
# print('c', len(df))
# df_filter = df[['userId', 'movieId', 'rating', 'timestamp']]

# avail rating [0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5 5. ]
# print(np.unique(df_filter['rating']))

# out 
# GOAL : get top 10 most watch movie 
df_g1 = df.groupby(['movieId','title',]).agg({'userId' : 'count', 'rating' : 'mean' }).reset_index().rename(columns={'userId' : 'jumlah_reviewer', 'rating' : 'avg_rating', }).sort_values(by=['jumlah_reviewer', 'avg_rating'], ascending=False)
print(df_g1[:10])
df_g1[:10].to_json(r'./web/src/data/best-top-ten-movies.json', orient='records')

# GOAL : get market share based on genre
df_f = df_movie[['movieId', 'genres']]
df_f.loc[df_f['genres'].str.contains(' ') , 'genres'] = 'Unknown' # renaming no genres
df_c = pd.concat([df_f, df_f['genres'].str.get_dummies(sep='|')], axis=1)
cat = pd.Categorical(df_f['genres'].str.get_dummies(sep='|'))

sums  = df_c[cat].sum().rename('SUMS')
total_mov_all_cat = sums[cat].sum()

## draft
ddd = df_c[cat].agg(['sum']).transpose()
ddd['pct'] = round(ddd['sum'] / total_mov_all_cat * 100, 2)

y = list(ddd['sum'])
print(ddd)
ddd['sum'].to_json(r'./web/src/data/genres-market-share.json', )
plt.pie(y , labels=cat ,autopct='%1.2f%%', pctdistance=0.4)
plt.show() 
