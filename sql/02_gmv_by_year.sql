SELECT
    EXTRACT(YEAR FROM created_at)::int AS year,
    ROUND(SUM(amount))             AS gmv
FROM payments
WHERE status = 'succeeded'
  AND NOT is_deleted
GROUP BY year
ORDER BY year;