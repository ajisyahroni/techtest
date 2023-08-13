-- IMDB SCORE
WITH MOVIES_RATING AS (
    SELECT
        r.userId,
        r.rating,
        m.movieId AS movieId,
        m.title,
        m.genres
    FROM
        ratings r
        INNER JOIN movies m ON r.movieId = m.movieId
),
RATING_MEAN AS (
    SELECT
        AVG(rating) as rating_avg
    from
        MOVIES_RATING
    group by
        movieId
),
TOP_TEN AS (
    SELECT
        title,
        count(userId) as num_votes,
        -- v --
        avg(rating) as rating_mean,
        -- R --
        (
            select
                AVG(rating_avg)
            from
                RATING_MEAN
        ) as C,
        (num_votes /(num_votes + 346.0) * rating_mean) + (346.0 /(num_votes + 346.0) * C) as score
    FROM
        MOVIES_RATING
    GROUP BY
        movieId,
        title
    ORDER BY
        score DESC
    LIMIT
        10
)
SELECT title, num_votes, score FROM TOP_TEN