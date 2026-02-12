Вопросы с выбором варианта: 62/100%  
# Вопрос 1. Тема: Сложные запросы
  
**1. Какой оператор используется для объединения двух таблиц в SQL?**
  
Варианты ответов:
1) COMBINE
2) ✅ JOIN
3) UNION
4) MERGE
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 2. Тема: Сложные запросы
  
**2. Как объединить таблицы Customers и Orders по полю CustomerID и выбрать все строки из таблицы Customers, даже если нет соответствующих записей в таблице Orders?**
  
Варианты ответов:
1) SELECT * FROM Customers FULL JOIN Orders ON Customers.CustomerID = Orders.CustomerID
2) SELECT * FROM Customers RIGHT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
3) ❌ SELECT * FROM Customers INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
4) SELECT * FROM Customers LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 3. Тема: Сложные запросы
  
**3. Что вернёт запрос `SELECT Customers.Name, Orders.OrderID FROM Customers LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID;`, если в таблице Customers есть клиенты без заказов?**
  
Варианты ответов:
1) Запрос вернёт только заказы, без клиентов
2) ✅ Запрос вернёт всех клиентов (включая тех, у кого нет заказов) с пустыми значениями для OrderID
3) Запрос вернёт только клиентов с заказами
4) Запрос не вернёт результатов
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 4. Тема: Сложные запросы
  
**4. Какой результат вернёт следующий SQL-запрос?**

```
SELECT Name FROM Customers
UNION
SELECT Name FROM Suppliers;
```
  
Варианты ответов:
1) Вернёт только уникальные имена из таблиц Customers и Suppliers
2) Объединит результаты обеих таблиц, включая дубликаты
3) Вернёт только совпадающие значения из обеих таблиц
4) ❌ Объединит результаты, но добавит NULL вместо отсутствующих значений
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
  
# Вопрос 5. Тема: Сложные запросы
  
**5. Какой результат вернёт следующий SQL-запрос?**

```
SELECT ProductName FROM Products
EXCEPT
SELECT ProductName FROM DiscontinuedProducts;
```
  
Варианты ответов:
1) Вернёт список всех товаров, включая устаревшие
2) Вернёт только товары, которые присутствуют в обеих таблицах
3) ✅ Вернёт товары, которые есть в Products, но отсутствуют в DiscontinuedProducts
4) Вернёт только устаревшие товары
  
### ИИ анализ <img src="https://github.com/Pau1R/python2026/blob/main/misc/loading.gif" width="36" height="12">
