Drop table Students;

CREATE TABLE "Students" (
	"StudentID" INTEGER PRIMARY KEY AUTOINCREMENT,
	"FirstName"	TEXT,
	"LastName"	TEXT
);

Drop table Courses;

CREATE TABLE "Courses" (
	"CourseID" INTEGER PRIMARY KEY AUTOINCREMENT,
	"CourseName"	TEXT,
	"Credits"	INTEGER
);

Drop table Enrollments;

CREATE TABLE "Enrollments" (
	"StudentID" INTEGER,
	"CourseID"	INTEGER
);

INSERT INTO Students (StudentID, FirstName, LastName)
VALUES (1,"Наталья", "Фролова"),
       (2, "Артем", "Иванов"),
	   (3, "Софья", "Петрова");
	   
INSERT INTO Courses (CourseID, CourseName, Credits)
VALUES (1,"Информатика", 3),
       (2, "Математика", 4),
	   (3, "История", 3);
	   
INSERT INTO Enrollments (StudentID, CourseID)
VALUES (1,1),
       (2,2);
	   
SELECT 
    Students.LastName,
    Students.FirstName,
    Courses.CourseName
FROM Students
JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
JOIN Courses ON Enrollments.CourseID = Courses.CourseID;

DELETE FROM Enrollments;
DELETE FROM Students;
DELETE FROM Courses;

