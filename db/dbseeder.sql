-- Seed (Insert Data Into) The various tables
START TRANSACTION;

-- Customers
INSERT INTO customers (name, email, country) VALUES
('Alice Smith', 'alice@example.com', 'USA'),
('Bob Jones', 'bob@example.com', 'Canada'),
('Charlie Zhang', 'charlie@example.com', 'UK');

-- Products
INSERT INTO products (name, category, price) VALUES
('Laptop', 'Electronics', 1200.00),
('Smartphone', 'Electronics', 800.00),
('Desk Chair', 'Furniture', 150.00),
('Coffee Maker', 'Appliances', 85.50);

-- Orders
INSERT INTO orders (customer_id, order_date, status) VALUES
(1, '2023-11-15', 'Shipped'),
(2, '2023-11-20', 'Pending'),
(1, '2023-12-01', 'Delivered'),
(3, '2023-12-03', 'Cancelled');

-- Order Items
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 1200.00), -- Laptop
(1, 4, 2, 85.50), -- Coffee Maker
(2, 2, 1, 800.00), -- Smartphone
(3, 3, 2, 150.00); -- Desk Chair

COMMIT;