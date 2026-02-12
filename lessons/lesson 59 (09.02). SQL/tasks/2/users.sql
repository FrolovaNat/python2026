Drop TABLE users; 
CREATE TABLE users (
    id INTEGER,
    name TEXT,
    age INTEGER
);
INSERT INTO users (id, name, age)
VALUES
    (1, 'Иван', 20),
    (2, 'Мария', 22),
    (3, 'Петр', 19);
	
Drop TABLE users1; 
CREATE TABLE users1 (
    id INTEGER,
    name TEXT,
    position TEXT,
	salary INTEGER
);
INSERT INTO users1 (id, name, position, salary)
VALUES
    (1, 'Анна', 'Разработчик', 50000),
    (2, 'Олег', 'Менеджер', 60000),
    (3, 'Елена', 'Дизайнер', 45000);
UPDATE users1
SET salary = 65000
WHERE id = 2;

Drop TABLE users2; 
CREATE TABLE users2 (
    id INTEGER,
    name TEXT,
    price INTEGER,
	quantity INTEGER
);
INSERT INTO users2 (id, name, price, quantity)
VALUES
    (1, 'Ноутбук', 45000, 10),
    (2, 'Мышь', 1500, 50),
    (3, 'Клавиатура', 3000, 25),
	(3, 'Монитор', 12000, 15);
DELETE FROM users2
WHERE id = 3;