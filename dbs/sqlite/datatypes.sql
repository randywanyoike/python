CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL
)

--INSERT INTO student (name, email, dob, phone, marks) 
--VALUES ('Randy','randy@gmail.com','2007-05-25',254791999280,93.7);

--SELECT * FROM student