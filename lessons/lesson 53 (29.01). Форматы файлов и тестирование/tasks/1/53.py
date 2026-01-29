#1
import csv
with open('students.csv', 'r', encoding='utf-8') as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)
#2
import json
with open('employees.json', mode='r', encoding='utf-8') as file:
    data = json.load(fp=file)
print(data)

import json
data = {
    {
 "ИТ": 9500,
 "HR": 8200,
 "Финансы": 5200
}
}
with open('employees.json', mode='w', encoding='utf-8') as file:
    json.dump(obj=data,
              fp=file,
              indent=4
    )

#3
import csv
with open('products.csv', 'r', encoding='utf-8') as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)
import json
with open('prices.json', mode='r', encoding='utf-8') as file:
    data = json.load(fp=file)
print(data)

import json
data = {
 "Яблоки": {
 "количество": 10,
 "общая_цена": 25,0
 },
 "Апельсины": {
 "количество": 5,
 "общая_цена": 15,0
 },
 "Бананы": {
 "количество": 7,
 "общая_цена": 10,5
 }
}
with open('prices.json', mode='w', encoding='utf-8') as file:
    json.dump(obj=data,
              fp=file,
              indent=4
