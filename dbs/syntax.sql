-- SQL SYNTAX IT IS  NOT CASE SENSITIVE
-- CREATE TABLE
-- create table
-- CreatE Table 

-- SQL KEYWORDS <RESERVED KEYWORD>

-- CREATE TABLE IF NOT EXIST <table_name> ()

-- SQL KEYWORDS , <values>

-- CREATE TABLE IF NOT EXISTS 'table'(
-- )

--PREFERENCE ALL SQL KEYWORDS WILL BE CAPITALIZED

--EACH SQL STATEMENT SHOULD TERMINTATE WITH A COLON EXCEPT THE LAST ONE

-- comment 
-- Comment

CREATE TABLE IF NOT EXISTS student(
    id BIGSERIAL PRIMARY KEY,
    name TEXT,
    email TEXT
);

DROP TABLE IF EXISTS student;

CREATE TABLE IF NOT EXISTS teacher(
    id BIGSERIAL PRIMARY KEY,
    name TEXT,
    email TEXT
)



--ATOMIC,  <file>
-- EITHER ALL OF THEM QUERY(Question) EXECUTE ALL OF THEM FAIL

--Table Columns
-- COLUMNS DATATYPES:
-- sqlite,mysql

--Datatype:int:number,string:text,boolean:true,false
