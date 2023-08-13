-- PREVIOUSE RESULT
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
)

SELECT
    title,
    count(userId) as num_votes,
    avg(rating) as rating_mean, 
FROM
    MOVIES_RATING
GROUP BY
    movieId, title
ORDER BY
    num_votes DESC,
    rating_mean DESC
LIMIT
    10
