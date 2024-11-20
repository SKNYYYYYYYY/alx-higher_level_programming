-- average
ALTER TABLE second_table
ADD COLUMN average DECIMAL(10,4);
INSERT INTO second_table (average) SELECT SUM(score) / COUNT(scores) FROM second_table;