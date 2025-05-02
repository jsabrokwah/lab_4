- CREATE DATABASE online_store;

- CREATE USER 'ec2dbUser'@'%' IDENTIFIED BY 'ec2userpAss';

- GRANT ALL PRIVILEGES ON online_store.* TO 'ec2dbUser'@'%';

- FLUSH DATABASES;

- SHOW GRANTS FOR 'ec2dbUser'@'%'
