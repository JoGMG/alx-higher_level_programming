-- Script that displays the max temperature of each state (ordered by State name).
-- Import in hbtn_0c_0 database this table dump: https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
