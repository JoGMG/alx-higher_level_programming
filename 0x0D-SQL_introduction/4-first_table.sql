-- Script that creates a table called first_table in the current database in your MySQL server.
-- If the table first_table already exists, script still doesn't fail.
-- Database name is first passed as argument of the mysql command.
CREATE TABLE IF NOT EXISTS first_table (id INT,
name VARCHAR(256));
