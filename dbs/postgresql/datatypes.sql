CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    dob DATE,
    phone INTEGER,
    marks REAL,
    is_married BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--INSERT INTO student (name, email, dob, phone, marks) 
--VALUES ('Randy','randy@gmail.com','2007-05-25',25479280,93.7);

--SELECT * FROM student