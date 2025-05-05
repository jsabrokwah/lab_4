# Programming, Ops and Database Exercise API

Flask-based REST API providing endpoints the following queries.

- Top Customers by Spending
- Monthly Sales Report (Only Shipped/Delivered)
- Products Never Ordered
- Average Order Value by Country
- Frequent Buyers (More Than One Order)

## Setup

1. Configure environment variables in `.env`:
   ```
   DB_HOST=mysqldb2.cdgs4qkmwl1f.eu-west-1.rds.amazonaws.com
   DB_PORT=3117
   DB_USER=ec2dbUser
   DB_PASSWORD=****
   DB_NAME=online_store
   PORT=5000
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run with Docker:
   ```bash
   docker-compose up
   ```

## API Endpoints

### GET /api/top-customers
Returns customers ranked by total spending

### GET /api/monthly-sales
Shows monthly sales for shipped/delivered orders

### GET /api/products-never-ordered
Lists products with no orders

### GET /api/avg-order-by-country
Shows average order value by customer country

### GET /api/frequent-buyers
Lists customers with multiple orders

### GET /health
API health check endpoint

## Docker Support

- Multi-stage build process
- Environment variable support
- Network configuration
- Automatic restarts