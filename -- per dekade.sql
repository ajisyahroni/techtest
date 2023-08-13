-- belajar
with MOVIE_WITH_DECADE AS (
    select
        movieId,
        title,
        toInt64OrZero(
            concat(
                toString(
                    intDiv(
                        toInt64OrZero(
                            replace(
                                replace(
                                    splitByWhitespace(assumeNotNull(title)) [-1],
                                    '(',
                                    ''
                                ),
                                ')',
                                ''
                            )
                        ),
                        10
                    )
                ),
                '0'
            )
        ) as decade
    from
        movies
    where
        decade != 0
)
SELECT
    decade,
    count(*) as jumlah_film
FROM
    MOVIE_WITH_DECADE
GROUP BY
    decade;