-- Top Customers by Spending
SELECT 
    c.customer_id,
    c.name,
    c.email,
    SUM(oi.quantity * oi.unit_price) AS total_spent
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
JOIN 
    order_items oi ON o.order_id = oi.order_id
GROUP BY 
    c.customer_id, c.name, c.email
ORDER BY 
    total_spent DESC;


-- Monthly Sales Report (Only Shipped/Delivered Orders)

SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS month,
    SUM(oi.quantity * oi.unit_price) AS monthly_sales,
    COUNT(DISTINCT o.order_id) AS number_of_orders
FROM 
    orders o
JOIN 
    order_items oi ON o.order_id = oi.order_id
WHERE 
    o.status IN ('Shipped', 'Delivered')
GROUP BY 
    DATE_FORMAT(o.order_date, '%Y-%m')
ORDER BY 
    month;

--  Products Never Ordered
SELECT 
    p.product_id,
    p.name,
    p.category,
    p.price
FROM 
    products p
LEFT JOIN 
    order_items oi ON p.product_id = oi.product_id
WHERE 
    oi.order_item_id IS NULL;


-- Average Order Value by Country
SELECT 
    c.country,
    AVG(order_total.total) AS average_order_value
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
JOIN 
    (SELECT 
        order_id, 
        SUM(quantity * unit_price) AS total
     FROM 
        order_items
     GROUP BY 
        order_id) AS order_total ON o.order_id = order_total.order_id
GROUP BY 
    c.country
ORDER BY 
    average_order_value DESC;

-- Frequent Buyers 

SELECT 
    c.customer_id,
    c.name,
    c.email,
    COUNT(o.order_id) AS order_count
FROM 
    customers c
JOIN 
    orders o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_id, c.name, c.email
HAVING 
    COUNT(o.order_id) > 1
ORDER BY 
    order_count DESC;
