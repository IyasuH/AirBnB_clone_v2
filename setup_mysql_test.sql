-- Script that prepares A MySQL server for the project
-- create a database 'hbnb_test_db' if not exist
-- create a new user if not exist 'hbnb_test' in localhost with password hbnb_test_pwd
-- And hbnb_test have all privileges on the database hbnb_test_db
-- And hbnb_test have 'SELECT' provilages on the database performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
