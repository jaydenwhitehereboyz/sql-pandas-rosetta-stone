SELECT
    account_id,
    ROUND(SUM(amount)) AS gmv
FROM payments
WHERE status = 'succeeded'
  AND NOT is_deleted
GROUP BY account_id
ORDER BY gmv DESC
LIMIT 10;