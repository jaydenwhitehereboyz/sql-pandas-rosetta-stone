SELECT
    status,
    COUNT(*) AS status_count,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS share_pct
FROM payments
GROUP BY status
ORDER BY status_count DESC;