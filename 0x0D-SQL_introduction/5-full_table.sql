-- Script to print full table description without using DESCRIBE or EXPLAIN
SELECT `CREATE TABLE` FROM information_schema.tables 
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
