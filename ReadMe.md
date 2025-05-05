# Programming, Ops and Database Exercise API Project

This project implements an Programming, Ops and Database Exercise API system with a Flask backend and AWS RDS MySQL database. It provides various endpoints for analyzing customer behavior, sales patterns, and product performance.

## Project Structure

```
├── api/               
├── db/               
└── screenshots/      
```

## Key Features

- Top customers by spending analysis
- Monthly sales reporting
- Products inventory analysis
- Geographic order value analysis
- Customer loyalty tracking

## Components

- **API Service**: Flask-based REST API with multiple analytical endpoints
- **Database**: MySQL database with e-commerce schema
- **Docker Support**: Containerized deployment with Docker and Docker Compose

## Getting Started

1. Setup the database:
   ```bash
   cd db
   # Follow instructions in db/ReadMe.md
   ```

2. Start the API:
   ```bash
   cd api
   docker-compose up
   ```

3. Access the API at `http://52.18.99.211:5000`

## API Endpoints

- `/api/top-customers` - View top spending customers
- `/api/monthly-sales` - Monthly sales analysis
- `/api/products-never-ordered` - Inventory analysis
- `/api/avg-order-by-country` - Geographic order analysis
- `/api/frequent-buyers` - Customer loyalty metrics