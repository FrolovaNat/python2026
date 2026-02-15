DROP TABLE Students;
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    birth_date DATE,
    email TEXT UNIQUE,
    course_name TEXT,
    enrollment_date DATE
);
INSERT INTO Students (id, name, birth_date, email, course_name, enrollment_date) 
VALUES (1, "Наталья", "03-11-1992", "rov@mail.ru", "Программирование", "01-09-2025"),
       (2, "Артем", "03-11-2015", "ov@mail.ru", "Программирование", "01-03-2026"),
	   (3, "Софья", "09-03-2020", "v@mail.ru", "Вокал", "15-03-2027");

SELECT name 
FROM Students 
WHERE course_name = "Программирование"
AND id IN (
    SELECT id 
    FROM Students
    WHERE course_name = "Программирование"
);
