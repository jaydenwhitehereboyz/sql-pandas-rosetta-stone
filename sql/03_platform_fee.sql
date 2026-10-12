SELECT
    EXTRACT(MONTH FROM created_at)  AS month,
    ROUND(SUM(platform_fee_amount)) AS platform_revenue,
    COUNT(*)                        AS payments_count,
    ROUND(AVG(amount))              AS avg_amount
FROM payments
WHERE status = 'succeeded'
  AND NOT is_deleted
  AND created_at >= '2025-01-01'
  AND created_at <  '2026-01-01'
GROUP BY month
ORDER BY month;