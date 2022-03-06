-- Script that prepares A MySQL server for the project
-- create a database if not exists 'hbnb_dev_db'
-- create a new user if not exists 'hbnb_dev' in localhost with password hbnb_dev_pwd
-- And hbnb_dev have all privileges on the database hbnb_dev_db
-- And hbnb_dev have 'SELECT' provilages on the database performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
