/*
/*
BigQuery Standard SQL Solution
Author @j450h1
*/
SELECT
  number,
  CASE
    WHEN MOD(number, 15) = 0 THEN 'Fizz Buzz'
    WHEN MOD(number, 3) = 0 THEN 'Fizz'
    WHEN MOD(number, 5) = 0 THEN 'Buzz'
  ELSE number || '' --alternative to CAST
END
  AS answer
FROM (
  SELECT
    *
  FROM
    UNNEST(GENERATE_ARRAY(1, 100)) AS number)