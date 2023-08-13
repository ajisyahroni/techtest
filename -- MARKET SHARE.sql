-- MARKET SHARE
WITH MOVIE_WITH_CAT AS (
    SELECT
        movieId,
        title,
        genres,
        splitByString('|', assumeNotNull(genres)) as categories
    from
        movies
),
CATEGORIES AS (
    SELECT
        groupUniqArrayArray(categories) AS unique_category
    FROM
        MOVIE_WITH_CAT
)
SELECT
    categories as kategori,
    count(categories) as jumlah
from
    MOVIE_WITH_CAT array
    join categories
group by
    categories