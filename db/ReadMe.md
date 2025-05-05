# Database Setup Guide

## Setup an AWS RDS MySQL Database
- Follow this [AWS RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html) to setup a Database service

## Initial Setup

1. Create database:
```sql
CREATE DATABASE online_store;
```

2. Create database user:
```sql
CREATE USER 'ec2dbUser'@'%' IDENTIFIED BY 'examplepassword';
```

3. Grant privileges:
```sql
GRANT ALL PRIVILEGES ON online_store.* TO 'ec2dbUser'@'%';
```

4. Apply changes:
```sql
FLUSH PRIVILEGES;
```

5. Verify setup:
```sql
SHOW GRANTS FOR 'ec2dbUser'@'%';
```

## Schema Setup

1. Run schema creation script:
```bash
mysql -u ec2dbUser -p online_store < dbdefinition.sql
```

2. Load sample data:
```bash
mysql -u ec2dbUser -p online_store < dbseeder.sql
```

## Available Queries

The `queries.sql` file contains various analytical queries:
- Top customers by spending
- Monthly sales reporting
- Products never ordered
- Average order value by country
- Frequent buyers analysis