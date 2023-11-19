-- create table and add multiple rows

USE hbtn_0c_0;

CREATE TABLE IF NOT EXISTS second_table (
    id INT AUTO_INCREMENT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (name, score) VALUES ( “John”, 10), (“Alex”, 3), (“Bob”, 14), (“George”, 8);