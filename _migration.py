import pandas as pd 
from sqlalchemy import create_engine
import numpy as np
from concurrent.futures import ThreadPoolExecutor



engine = create_engine('mariadb+pymysql://jik:1122@localhost:33064/movies_db?charset=utf8mb4', echo=False)

df_movie = pd.read_parquet('./db/movie.parquet')
df_rating = pd.read_parquet('./db/rating.parquet')
df_movie_rating = pd.merge(df_movie, df_rating , on=['movieId'])



def insert_movies(chunk):
    chunk.to_sql(name='movies', con=engine, if_exists='replace', index=False)

def insert_rating(chunk):
    chunk.to_sql(name='ratings', con=engine, if_exists='replace', index=False)

with ThreadPoolExecutor() as executor:
    executor.map(insert_movies, np.array_split(df_movie, 10))
    executor.map(insert_rating, np.array_split(df_rating, 10))