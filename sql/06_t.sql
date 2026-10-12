SELECT
    CASE
        WHEN amount < 10000   THEN '<10k'
        WHEN amount < 100000  THEN '10-100k'
        WHEN amount >= 100000 THEN '>=100k'
        ELSE 'unknown'
    END                                                        AS amount_bucket,
    COUNT(*)                                                   AS payment_count,
    ROUND(SUM(amount) FILTER (WHERE status = 'succeeded'
                                AND NOT is_deleted))           AS gmv
FROM payments
GROUP BY amount_bucket
ORDER BY MIN(amount);