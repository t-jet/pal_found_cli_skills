CREATE TABLE `/Demo/customer_totals` AS
SELECT
    o.customer_id AS customer_id,
    c.region AS region,
    CAST(SUM(COALESCE(o.amount, 0)) AS DECIMAL(12,2)) AS total_amount,
    COUNT(*) AS order_count
FROM `/Demo/orders` o
JOIN `/Demo/customers` c ON o.customer_id = c.customer_id
GROUP BY o.customer_id, c.region
