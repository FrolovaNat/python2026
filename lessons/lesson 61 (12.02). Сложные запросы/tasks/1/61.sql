Drop table Customers;

CREATE TABLE "Customers" (
	"Customer_ID" INTEGER,
	"FirstName"	TEXT,
	"LastName"	TEXT,
	"Email"	TEXT
);
Drop table Orders;
CREATE TABLE "Orders" (
	"Order_ID" INTEGER,
	"Customer_ID" INTEGER PRIMARY KEY,
	"OrderDate"	TEXT,
	"TotalAmount"	REAL
);
INSERT INTO Customers (Customer_ID, FirstName, LastName, Email)
VALUES (1, "John", "Doe", "johndoe@example.com"),
       (2, "Jane", "Smith", "janesmith@example.com");
	   
INSERT INTO Orders (Order_ID, Customer_ID, OrderDate, TotalAmount)
VALUES (101, 1, "2025-02-01", 100.50),
       (102, 2, "2025-02-02", 200.75);
	   
SELECT*FROM Customers;
SELECT*FROM Orders;

SELECT Customers.FirstName, Customers.LastName, Orders.Order_ID, Orders.TotalAmount
FROM Customers
INNER JOIN Orders ON Customers.Customer_ID = Orders.Customer_ID;


SELECT Customers.FirstName, Customers.LastName, Orders.Order_ID, Orders.TotalAmount
FROM Customers
LEFT JOIN Orders ON Customers.Customer_ID = Orders.Customer_ID;

SELECT FirstName, LastName, NULL AS Order_ID, NULL AS TotalAmount
FROM Customers
UNION
SELECT NULL, NULL, Order_ID, TotalAmount
FROM Orders;

SELECT Order_ID, Customer_ID, OrderDate, TotalAmount
FROM Orders


