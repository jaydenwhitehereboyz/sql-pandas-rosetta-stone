SELECT
    EXTRACT(YEAR  FROM created_at)                       AS year,
    EXTRACT(MONTH FROM created_at)                       AS month,
    COUNT(*) FILTER (WHERE status = 'failed')            AS failed_count,
    COUNT(*)                                             AS payments_count,
    ROUND(100.0 * COUNT(*) FILTER (WHERE status = 'failed')
          / COUNT(*), 1)                                 AS failed_pct
FROM payments
GROUP BY year, month
HAVING 100.0 * COUNT(*) FILTER (WHERE status = 'failed') / COUNT(*) > 4
ORDER BY year, month;