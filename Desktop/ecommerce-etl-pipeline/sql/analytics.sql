SELECT country,
       SUM(revenue) AS total_revenue
FROM analytics.orders_clean
GROUP BY country
ORDER BY total_revenue DESC;