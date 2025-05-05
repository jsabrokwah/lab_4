from flask import Flask, jsonify
import mysql.connector
import os
from datetime import datetime

app = Flask(__name__)

# Database connection function
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get('DB_HOST', 'localhost'),
            port=os.environ.get('DB_PORT', 'localhost'),
            user=os.environ.get('DB_USER', 'root'),
            password=os.environ.get('DB_PASSWORD', ''),
            database=os.environ.get('DB_NAME', 'ecommerce')
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

# Helper function to convert MySQL result to JSON-serializable format
def format_results(cursor):
    columns = [desc[0] for desc in cursor.description]
    results = []
    for row in cursor.fetchall():
        row_dict = {}
        for i, column in enumerate(row):
            # Convert decimal and datetime types to standard Python types
            if isinstance(column, datetime):
                row_dict[columns[i]] = column.strftime('%Y-%m-%d %H:%M:%S')
            elif str(type(column)) == "<class 'decimal.Decimal'>":
                row_dict[columns[i]] = float(column)
            else:
                row_dict[columns[i]] = column
        results.append(row_dict)
    return results

# 1. Top Customers by Spending
@app.route('/api/top-customers', methods=['GET'])
def top_customers():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = connection.cursor()
    query = """
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
        total_spent DESC
    """
    
    cursor.execute(query)
    results = format_results(cursor)
    
    cursor.close()
    connection.close()
    
    return jsonify({"top_customers": results})

# 2. Monthly Sales Report (Only Shipped/Delivered)
@app.route('/api/monthly-sales', methods=['GET'])
def monthly_sales():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = connection.cursor()
    query = """
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
        month
    """
    
    cursor.execute(query)
    results = format_results(cursor)
    
    cursor.close()
    connection.close()
    
    return jsonify({"monthly_sales": results})

# 3. Products Never Ordered
@app.route('/api/products-never-ordered', methods=['GET'])
def products_never_ordered():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = connection.cursor()
    query = """
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
        oi.order_item_id IS NULL
    """
    
    cursor.execute(query)
    results = format_results(cursor)
    
    cursor.close()
    connection.close()
    
    return jsonify({"products_never_ordered": results})

# 4. Average Order Value by Country
@app.route('/api/avg-order-by-country', methods=['GET'])
def avg_order_by_country():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = connection.cursor()
    query = """
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
        average_order_value DESC
    """
    
    cursor.execute(query)
    results = format_results(cursor)
    
    cursor.close()
    connection.close()
    
    return jsonify({"avg_order_by_country": results})

# 5. Frequent Buyers (More Than One Order)
@app.route('/api/frequent-buyers', methods=['GET'])
def frequent_buyers():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = connection.cursor()
    query = """
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
        order_count DESC
    """
    
    cursor.execute(query)
    results = format_results(cursor)
    
    cursor.close()
    connection.close()
    
    return jsonify({"frequent_buyers": results})

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API is running"})

# Root endpoint
@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "message": "Programming, Ops and Database Exercise API",
        "endpoints": [
            "/api/top-customers",
            "/api/monthly-sales",
            "/api/products-never-ordered",
            "/api/avg-order-by-country",
            "/api/frequent-buyers",
            "/health"
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))