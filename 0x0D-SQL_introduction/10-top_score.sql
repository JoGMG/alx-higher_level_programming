-- Script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- Database name is first passed as argument of the mysql command.
-- Results should display both the score and the name (in this order)
-- Records should be ordered by score (top first)
SELECT score, name FROM second_table ORDER BY score DESC;