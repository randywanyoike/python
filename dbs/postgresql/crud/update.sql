UPDATE student 
SET
marks=0
WHERE marks IS NULL;

SELECT name,marks
FROM student

UPDATE student
SET email='johndoe@gmail.com'
WHERE email='john@john.com'